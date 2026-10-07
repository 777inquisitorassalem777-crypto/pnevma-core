"""Intuition & inventiveness heuristics — controlled novelty."""

from __future__ import annotations
from typing import Any, Dict
import random
from ..pneuma.state import PHI, PHI_INV


class IntuitionEngine:
    def __init__(self):
        self.history: list[float] = []

    def novelty_score(self, context: str = "") -> float:
        base = random.betavariate(PHI, PHI_INV)  # asymmetric, mild bias
        lexical = min(1.0, len(set((context or "").split())) / 40.0)
        score = 0.6 * base + 0.4 * lexical
        self.history.append(score)
        return score

    def invent_paradigm_seed(self, focus: str = "life_multiplication") -> Dict[str, Any]:
        return {
            "focus": focus,
            "novelty": round(self.novelty_score(focus), 4),
            "style": random.choice([
                "analogical", "inversion", "boundary_shift",
                "compassionate_reframing", "minimal_intervention",
            ]),
            "irrational_allowed": True,
        }
