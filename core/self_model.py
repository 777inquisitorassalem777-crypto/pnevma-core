"""
Self-model — functional self-awareness proxy.
Различение себя / другого, оценка ограничений, прогноз ошибки.
НЕ претендует на феноменальное сознание.
"""

from typing import Dict, Any
from dataclasses import dataclass, field


@dataclass
class SelfModel:
    identity: str = "pneuma-lab-agent"
    awareness_proxy: float = 0.2
    known_limits: list = field(default_factory=lambda: [
        "no_phenomenal_consciousness_claim",
        "no_soul_claim",
        "uncertainty_required",
        "external_safety_mandatory",
    ])
    error_history: list = field(default_factory=list)

    def distinguish_self_other(self, subject: str) -> bool:
        """True if subject is self."""
        return subject.lower() in ("self", "я", "me", self.identity.lower())

    def predict_own_error(self, confidence: float, evidence: float) -> float:
        """Прогноз собственной ошибки."""
        gap = abs(confidence - evidence)
        return min(1.0, gap + 0.1)

    def update_after_correction(self, correction: str) -> None:
        self.error_history.append(correction)
        self.awareness_proxy = min(1.0, self.awareness_proxy + 0.05)
        if len(self.error_history) > 100:
            self.error_history = self.error_history[-100:]

    def status(self) -> Dict[str, Any]:
        return {
            "identity": self.identity,
            "awareness_proxy": round(self.awareness_proxy, 3),
            "known_limits": self.known_limits,
            "errors_recorded": len(self.error_history),
            "disclaimer": "Functional self-model only. No claim of subjective experience.",
        }
