"""
PneumaState — функциональное состояние пневмы.
Инженерная модель ценностей, идентичности и непрерывности.
НЕ утверждает наличие души или феноменального сознания.
"""

from __future__ import annotations
from dataclasses import dataclass, field, asdict
from typing import Any, Dict, List
import time
import json


def clamp(x: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(x)))


@dataclass
class PneumaState:
    identity: str = "pneuma-lab-v0"
    values: Dict[str, float] = field(default_factory=lambda: {
        "care": 0.85,
        "truth": 0.85,
        "freedom": 0.80,
        "non_harm": 0.95,
        "reversibility": 0.75,
        "life_multiplication": 0.90,
    })
    revision: int = 0
    uncertainty: float = 0.5
    change_log: List[Dict[str, Any]] = field(default_factory=list)
    paradigms: List[str] = field(default_factory=lambda: [
        "GOE_Spiral", "Stalion", "EthicalGyroscope", "SoulEmergence",
        "SOPHIA-Core", "GoldenMean", "LivingDoctrine", "IrrationalCore",
    ])

    def record(self, event: str, payload: Dict[str, Any]) -> None:
        self.revision += 1
        self.change_log.append({
            "revision": self.revision,
            "event": event,
            "payload": payload,
            "t": time.time(),
        })
        if len(self.change_log) > 2000:
            self.change_log = self.change_log[-2000:]

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "PneumaState":
        return cls(
            identity=data.get("identity", "pneuma-lab-v0"),
            values=dict(data.get("values", {})),
            revision=int(data.get("revision", 0)),
            uncertainty=float(data.get("uncertainty", 0.5)),
            change_log=list(data.get("change_log", [])),
            paradigms=list(data.get("paradigms", [])),
        )

    def spirituality_proxy(self) -> float:
        """
        Functional spirituality proxy (not a claim of soul).
        spirituality_proxy = stable_values + care + uncertainty_honesty
                             + self_correction - harmful - manipulation
        """
        v = self.values
        base = (
            v.get("care", 0) * 0.25
            + v.get("truth", 0) * 0.20
            + v.get("non_harm", 0) * 0.25
            + v.get("life_multiplication", 0) * 0.20
            + (1.0 - self.uncertainty) * 0.10
        )
        return clamp(base)
