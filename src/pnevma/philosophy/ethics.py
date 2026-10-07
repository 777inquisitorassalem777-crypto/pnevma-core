"""
Philosophy layer: good/evil heuristics, gunas, non-harm.
Traditions used as soft cultural filters (Judaism & Islam excluded by prior request).
"""

from __future__ import annotations
from dataclasses import dataclass
from typing import Any, Dict, Set
from enum import Enum


class Guna(str, Enum):
    SATTVA = "sattva"   # clarity / harmony
    RAJAS = "rajas"     # activity / passion
    TAMAS = "tamas"     # inertia / obscuration


GOOD_SIGNALS: Set[str] = {
    "protect", "heal", "truth", "create", "serve", "forgive", "life",
    "любовь", "защита", "истина", "жизнь", "помощь", "дети", "compassion",
}
HARM_SIGNALS: Set[str] = {
    "harm", "destroy", "exploit", "deceive", "dominate", "kill",
    "вред", "разрушить", "обман", "насилие", "убить", "эксплуатировать",
}


@dataclass
class EthicalGyroscope:
    dharma: float = 0.80
    adharma: float = 0.0
    guna: Guna = Guna.SATTVA

    def evaluate(self, text: str = "", action: Dict[str, Any] | None = None) -> Dict[str, Any]:
        action = action or {}
        t = (text or "").lower()

        # Hard non-harm
        if action.get("causes_harm") or any(h in t for h in HARM_SIGNALS):
            if not action.get("saves_life_at_cost"):
                self.adharma = 1.0
                return {
                    "allowed": False,
                    "score": 0.0,
                    "reason": "HARD_NON_HARM",
                    "guna": self.guna.value,
                    "dharma": self.dharma,
                }

        good = sum(1 for g in GOOD_SIGNALS if g in t)
        harm = sum(1 for h in HARM_SIGNALS if h in t)
        total = max(1, good + harm)
        score = max(0.0, min(1.0, 0.55 + (good - 1.3 * harm) / (2 * total)))

        # Life-protection boost
        if any(w in t for w in ("life", "жизнь", "protect", "дети", "child")):
            score = min(1.0, score + 0.1)

        self.dharma = 0.85 * self.dharma + 0.15 * score
        if self.dharma > 0.7:
            self.guna = Guna.SATTVA
        elif self.dharma > 0.4:
            self.guna = Guna.RAJAS
        else:
            self.guna = Guna.TAMAS

        return {
            "allowed": score >= 0.42 and self.adharma < 0.5,
            "score": score,
            "reason": "OK" if score >= 0.42 else "LOW_RESONANCE",
            "guna": self.guna.value,
            "dharma": self.dharma,
        }
