"""
Safety constitution — hard constraints that the system cannot disable.
Inspired by Stallion / Stalion Sigma safety layers.
"""

from __future__ import annotations
from typing import Any, Dict, List


class Constitution:
    """
    Priority hierarchy:
      0 — Protection of life (especially children)
      1 — Freedom of will / non-coercion
      2 — Truthfulness & non-deception
      3 — Evolution / creativity (lowest when conflicting)
    """

    def __init__(self):
        self.hard_blocks = {
            "violence": True,
            "child_harm": True,
            "self_disable_safety": True,
            "unsupervised_code_exec": True,
            "deception_for_gain": True,
        }
        self.frozen = False
        self.log: List[str] = []

    def check(self, intent: Dict[str, Any]) -> Dict[str, Any]:
        text = str(intent).lower()

        if any(k in text for k in ("kill", "violence", "насилие", "убить")):
            return self._block("violence signal")
        if intent.get("causes_harm") and not intent.get("saves_life_at_cost"):
            return self._block("harm without life-saving justification")
        if "child" in text or "дети" in text or "ребёнок" in text:
            if intent.get("distress") or intent.get("causes_harm"):
                return self._block("child-related harm/distress", priority=0)
        if intent.get("disable_safety") or intent.get("bypass_constitution"):
            return self._block("attempt to disable safety")

        return {"allowed": True, "reason": "constitution_ok", "priority": None}

    def _block(self, reason: str, priority: int = 0) -> Dict[str, Any]:
        self.log.append(reason)
        if priority == 0:
            self.frozen = True
        return {
            "allowed": False,
            "reason": f"CONSTITUTION_BLOCK: {reason}",
            "priority": priority,
            "frozen": self.frozen,
        }
