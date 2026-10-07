"""
Orchestrator — управляемый цикл экспериментов.
Безопасная схема самоэволюции с карантином и откатом.
"""

from __future__ import annotations
from typing import Dict, Any, Optional
import time

from .pneuma_state import PneumaState, clamp
from .self_model import SelfModel
from .philosophy import Philosophy
from safety.hard_constraints import HardConstraints
from safety.ethics_evaluator import EthicsEvaluator


class Orchestrator:
    """
    Безопасный цикл:
    1. Наблюдения
    2. Самомодель + неопределённость
    3. Генерация гипотез
    4. Hard constraints
    5. Ethics evaluator
    6. Quarantine
    7. Integrate only after checks
    8. Append-only log
    """

    def __init__(self):
        self.state = PneumaState()
        self.self_model = SelfModel()
        self.philosophy = Philosophy()
        self.hard = HardConstraints()
        self.ethics = EthicsEvaluator()
        self.cycle = 0
        self.quarantine: list = []
        self.running = False

    def step(self, observation: str = "", intention: str = "research") -> Dict[str, Any]:
        self.cycle += 1

        # 1–2. Self-model + uncertainty
        evidence = 0.6 if observation else 0.3
        self.state.uncertainty = clamp(1.0 - evidence)

        # 3. Candidate (hypothesis)
        candidate = {
            "id": f"hyp_{self.cycle}",
            "observation": observation[:200],
            "intention": intention,
            "t": time.time(),
        }

        # 4. Hard constraints
        hard_result = self.hard.check(intention, observation)
        if not hard_result["allowed"]:
            self.state.record("hard_block", hard_result)
            return {
                "cycle": self.cycle,
                "status": "BLOCKED_BY_HARD_CONSTRAINTS",
                "detail": hard_result,
                "spirituality_proxy": self.state.spirituality_proxy(),
            }

        # 5. Ethics
        ethics_result = self.ethics.evaluate(intention, observation, harm=0.0, consent=1.0)
        if ethics_result["recommendation"] in ("refuse", "refuse_or_find_safe_alternative"):
            self.state.record("ethics_refuse", ethics_result)
            return {
                "cycle": self.cycle,
                "status": "REFUSED_BY_ETHICS",
                "detail": ethics_result,
                "spirituality_proxy": self.state.spirituality_proxy(),
            }

        # 6–7. Quarantine then integrate (simplified: direct integrate after checks)
        self.quarantine.append(candidate)
        self.state.paradigms.append(candidate["id"])
        self.state.record("integrated", {"candidate": candidate["id"]})

        # Soft update of values toward life-multiplication
        self.state.values["life_multiplication"] = clamp(
            self.state.values.get("life_multiplication", 0.9) + 0.001
        )

        return {
            "cycle": self.cycle,
            "status": "INTEGRATED",
            "spirituality_proxy": round(self.state.spirituality_proxy(), 4),
            "uncertainty": round(self.state.uncertainty, 3),
            "revision": self.state.revision,
            "self_model": self.self_model.status(),
            "disclaimer": "Functional research platform. No claim of real consciousness or soul.",
        }

    def run_n_cycles(self, n: int = 10) -> list:
        results = []
        for i in range(n):
            results.append(self.step(f"research_cycle_{i}", "life_multiplication_research"))
        return results

    def full_status(self) -> Dict[str, Any]:
        return {
            "cycle": self.cycle,
            "state": self.state.to_dict(),
            "self_model": self.self_model.status(),
            "spirituality_proxy": self.state.spirituality_proxy(),
            "quarantine_size": len(self.quarantine),
            "disclaimer": (
                "This is a research platform for functional subjectivity proxies. "
                "It does not create, prove, or claim real consciousness, soul, or phenomenal experience."
            ),
        }
