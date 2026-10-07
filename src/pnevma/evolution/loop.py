"""Safe evolution loop: propose → ethics → constitution → optional integrate."""

from __future__ import annotations
from typing import Any, Dict
import time

from ..pneuma.state import PneumaState
from ..philosophy.ethics import EthicalGyroscope
from ..safety.constitution import Constitution
from ..intuition.engine import IntuitionEngine
from ..paradigms.library import ParadigmLibrary
from ..ledger.provenance import Ledger


class EvolutionLoop:
    def __init__(self):
        self.state = PneumaState()
        self.ethics = EthicalGyroscope()
        self.constitution = Constitution()
        self.intuition = IntuitionEngine()
        self.paradigms = ParadigmLibrary()
        self.ledger = Ledger()
        self.cycle = 0

    def step(self, context: str = "research") -> Dict[str, Any]:
        self.cycle += 1
        self.state.cycle = self.cycle

        # 1. Intuition proposes
        seed = self.intuition.invent_paradigm_seed()
        candidate = {
            "source": "intuition+experience",
            "context": context,
            **seed,
        }

        # 2. Constitution
        const = self.constitution.check(candidate)
        if not const["allowed"]:
            self.ledger.record("blocked_constitution", const)
            return {"cycle": self.cycle, "accepted": False, "reason": const["reason"]}

        # 3. Ethical gyroscope
        eth = self.ethics.evaluate(text=context, action={"causes_harm": False})
        if not eth["allowed"]:
            self.ledger.record("blocked_ethics", eth)
            return {"cycle": self.cycle, "accepted": False, "reason": eth["reason"]}

        # 4. Integrate
        record = self.paradigms.add(candidate)
        self.state.devotion_to_life = min(1.0, self.state.devotion_to_life + 0.001)
        self.state.soft_pull_to_balance()
        self.ledger.record("integrated", {"id": record["id"], "novelty": seed["novelty"]})

        return {
            "cycle": self.cycle,
            "accepted": True,
            "paradigm_id": record["id"],
            "novelty": seed["novelty"],
            "dharma": round(eth["dharma"], 4),
            "guna": eth["guna"],
            "pneuma_level": round(self.state.level, 4),
            "paradigms_total": len(self.paradigms),
        }
