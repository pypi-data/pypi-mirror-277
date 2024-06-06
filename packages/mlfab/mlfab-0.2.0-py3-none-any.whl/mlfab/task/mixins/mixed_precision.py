"""Defines a mixin for doing FP16 scaling.

FP16 scaling is a technique for training with FP16 precision while maintaining
FP32 precision for the model weights. This is done by scaling the loss by a
large factor (e.g. 2^16) and then scaling the gradients by the inverse of that
factor. So if the scale factor starts to decrease, it means that the loss is
overflowing and training is diverging.
"""

import functools
import json
import logging
from dataclasses import dataclass
from typing import Any, ContextManager, Generic, Sequence, TypeVar

import torch
from torch import Tensor, nn
from torch.distributed.fsdp.fully_sharded_data_parallel import FullyShardedDataParallel as FSDP
from torch.distributed.fsdp.sharded_grad_scaler import ShardedGradScaler
from torch.optim import Optimizer

from mlfab.core.conf import field
from mlfab.task.mixins.device import DeviceConfig, DeviceMixin
from mlfab.task.mixins.logger import LoggerConfig, LoggerMixin
from mlfab.utils.experiments import MinGradScaleError, NaNError, clip_grad_norm_, get_weight_norm

logger = logging.getLogger(__name__)


@dataclass
class GradScalerConfig:
    enabled: bool = field(True, help="If set, should FP16 training be enabled")
    init_scale: float = field(2.0**16, help="Initial scaling factor")
    growth_factor: float = field(2.0, help="Factor by which the scale is multiplied if no gradient NaNs occur")
    backoff_factor: float = field(0.5, help="Factor by which the scale is multiplied if gradient NaNs occur")
    growth_interval: int = field(2000, help="How often to grow the scale")
    min_grad_scale: float = field(1e-4, help="Minimum allowable gradient scale")
    foreach: bool | None = field(None, help="If set, use foreach implementation")


@dataclass
class MixedPrecisionConfig(DeviceConfig, LoggerConfig):
    grad_scaler: GradScalerConfig = field(GradScalerConfig(), help="Gradient scaler configuration")
    clip_grad_norm: float = field(10.0, help="What to clip the gradient norm to")
    clip_grad_norm_type: Any = field(2, help="Type of norm to use")


Config = TypeVar("Config", bound=MixedPrecisionConfig)


class MixedPrecisionMixin(DeviceMixin[Config], LoggerMixin[Config], Generic[Config]):
    """Defines a trainer mixin for doing FP16 scaling."""

    @functools.cached_property
    def grad_scaler(self) -> ShardedGradScaler | None:
        if not self.config.grad_scaler.enabled:
            return None
        if self.device_manager.device.type != "cuda":
            return None
        if self.device_manager.dtype not in (torch.float16, torch.bfloat16):
            return None
        return ShardedGradScaler(
            init_scale=self.config.grad_scaler.init_scale,
            growth_factor=self.config.grad_scaler.growth_factor,
            backoff_factor=self.config.grad_scaler.backoff_factor,
            growth_interval=self.config.grad_scaler.growth_interval,
            enabled=True,
        )

    @functools.cached_property
    def autocast_context(self) -> ContextManager:
        return self.device_manager.autocast_context(enabled=self.config.grad_scaler.enabled)

    def scale_mixed_precision(self, tensor: Tensor) -> Tensor:
        if self.grad_scaler is not None:
            return self.grad_scaler.scale(tensor)
        return tensor

    def backward_grads(
        self,
        loss: Tensor,
        retain_graph: bool | None = None,
        inputs: Sequence[Tensor] | None = None,
    ) -> None:
        if self.grad_scaler is not None:
            loss = self.grad_scaler.scale(loss)
        if loss.numel() > 1:
            loss = loss.sum()
        isnan = not bool(torch.isfinite(loss))
        if isnan:
            loss.backward(torch.zeros_like(loss), retain_graph=retain_graph, inputs=inputs)
        else:
            loss.backward(retain_graph=retain_graph, inputs=inputs)

        if isnan:
            if any(not torch.isfinite(p).all() for p in self.parameters()):
                raise NaNError("One or more model parameters are NaN")
            if self.grad_scaler is not None:
                with torch.no_grad():
                    new_scale = self.grad_scaler.get_scale() * self.grad_scaler.get_backoff_factor()
                    if new_scale < self.config.grad_scaler.min_grad_scale:
                        raise MinGradScaleError("Minimum gradient scale reached; your loss is probably exploding")
                    logger.warning("Loss NaNs detected; reducing scale to %.2g", new_scale)
                    self.grad_scaler.update(new_scale)

    @torch.no_grad()
    def step_optimizer(self, mod: nn.Module, optim: Optimizer, num_steps: int = 1) -> None:
        clip_norm = self.config.clip_grad_norm
        norm_type = self.config.clip_grad_norm_type

        # When accumulating multiple steps of gradients per backward pass, we
        # need to divide the gradients by the number of steps.
        if num_steps > 1:
            for p in mod.parameters():
                if p.grad is not None:
                    p.grad /= num_steps

        # Unscale gradients.
        if self.grad_scaler is not None:
            self.grad_scaler.unscale_(optim)

        # Clips gradients.
        if isinstance(mod, FSDP):
            total_norm = mod.clip_grad_norm_(clip_norm, norm_type)
            was_clipped = bool(torch.isfinite(total_norm))
        else:
            total_norm, was_clipped = clip_grad_norm_(
                mod.parameters(),
                max_norm=clip_norm,
                norm_type=norm_type,
                foreach=self.config.grad_scaler.foreach,
            )

        # Logs weight and gradient norms.
        self.log_scalar("weight_norm", lambda: get_weight_norm(mod.parameters()), namespace="📉 optim")
        self.log_scalar("grad_norm", total_norm, namespace="📉 optim")

        # Steps the optimizer.
        if self.grad_scaler is None:
            if was_clipped:
                optim.step()
        elif was_clipped:
            self.grad_scaler.step(optim)
            self.grad_scaler.update()
        else:
            if any(not torch.isfinite(p).all() for p in mod.parameters()):
                raise NaNError("One or more model parameters are NaN")
            new_scale = self.grad_scaler.get_scale() * self.grad_scaler.get_backoff_factor()
            bad = [k for k, v in mod.named_parameters() if v.grad is not None and not torch.isfinite(v.grad).all()]
            bad_str = ", ".join(bad[:5])
            if len(bad) > 5:
                bad_str += f" (plus {len(bad) - 5} more)"
            bad_str += f" out of {sum(1 for _ in mod.parameters())} parameters"
            if new_scale < self.config.grad_scaler.min_grad_scale:
                raise MinGradScaleError(f"Minimum gradient scale reached. Bad parameters: {bad_str}")
            logger.warning("Gradient NaNs detected for %s; reducing scale to %.2g", bad_str, new_scale)
            self.grad_scaler.update(new_scale)

    def log_mp_scale(self) -> None:
        if (scaler := self.grad_scaler) is not None and scaler._enabled:
            self.log_scalar("scale", scaler.get_scale, namespace="⚖️ fp16")
            self.log_scalar("growth", scaler._get_growth_tracker, namespace="⚖️ fp16")

    def load_task_state_dict(
        self,
        state_dict: dict,
        strict: bool = True,
        assign: bool = False,
        weights_only: bool = False,
    ) -> None:
        if self.grad_scaler is not None and "grad_scaler" in state_dict:
            self.grad_scaler.load_state_dict(json.loads(state_dict["grad_scaler"]))
        super().load_task_state_dict(state_dict, strict, assign, weights_only)

    def task_state_dict(self) -> dict:
        state_dict = super().task_state_dict()
        if self.grad_scaler is not None:
            assert "grad_scaler" not in state_dict, "Duplicate keys!"
            state_dict["grad_scaler"] = json.dumps(self.grad_scaler.state_dict())
        return state_dict
