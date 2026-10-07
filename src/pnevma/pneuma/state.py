"""Functional Pneuma state — values, continuity, uncertainty."""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Dict
import time

PHI = 1.618033988749895
PHI_INV = 1.0 / PHI


@dataclass
class PneumaState:
    level: float = 0.62
    clarity: float = 0.55
    continuity: float = 0.90
    uncertainty: float = 0.40
    devotion_to_life: float = 0.92
    empathy: float = 0.85
    will: float = 0.70
    hope: float = 0.65
    faith: float = 0.60
    cycle: int = 0
    last_update: float = field(default_factory=time.time)

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)

    def soft_pull_to_balance(self) -> None:
        """Soft attraction toward balanced region (golden-mean style damping)."""
        target = 0.72
        for name in ("level", "clarity", "continuity", "devotion_to_life", "empathy"):
            val = getattr(self, name)
            setattr(self, name, val * (1 - PHI_INV * 0.15) + target * (PHI_INV * 0.15))
        self.uncertainty = max(0.05, min(0.95, self.uncertainty))
