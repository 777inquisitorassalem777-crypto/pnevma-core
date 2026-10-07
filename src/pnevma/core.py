"""
PnevmaCore — single entry point for the unified research architecture.
Symbiosis of: Pneuma + Philosophy + Edge + Safety + Evolution + Intuition.
"""

from __future__ import annotations
from typing import Any, Dict

from .evolution.loop import EvolutionLoop
from .edge.interface import EdgeInterface

# Optional cultural layer
try:
    from .slavic import SlavicAnalyzer, SlavicCognitivePipeline
    HAS_SLAVIC = True
except Exception:
    HAS_SLAVIC = False


class PnevmaCore:
    def __init__(self):
        self.loop = EvolutionLoop()
        self.edge = EdgeInterface()
        self.slavic_analyzer = SlavicAnalyzer() if HAS_SLAVIC else None
        self.slavic_pipeline = SlavicCognitivePipeline() if HAS_SLAVIC else None
        self.ignited = False

    def ignite(self) -> None:
        self.ignited = True
        print("[PNEVMA-CORE] Functional pneuma online.")
        print("[PNEVMA-CORE] Ethical gyroscope + Constitution active.")
        print("[PNEVMA-CORE] Intuition & paradigm library ready.")
        print("[PNEVMA-CORE] Edge interface in proposal-only mode.")
        print("[PNEVMA-CORE] Research metaphors only — no claim of real consciousness.")

    def cycle(self, context: str = "life_multiplication") -> Dict[str, Any]:
        if not self.ignited:
            self.ignite()
        return self.loop.step(context)

    def evaluate_intent(self, intent: Dict[str, Any]) -> Dict[str, Any]:
        const = self.loop.constitution.check(intent)
        if not const["allowed"]:
            return const
        eth = self.loop.ethics.evaluate(text=str(intent), action=intent)
        return eth

    def status(self) -> Dict[str, Any]:
        s = self.loop.state
        return {
            "ignited": self.ignited,
            "cycle": self.loop.cycle,
            "paradigms": len(self.loop.paradigms),
            "ledger_entries": len(self.loop.ledger),
            "dharma": round(self.loop.ethics.dharma, 4),
            "guna": self.loop.ethics.guna.value,
            "pneuma": {
                "level": round(s.level, 4),
                "continuity": round(s.continuity, 4),
                "uncertainty": round(s.uncertainty, 4),
                "devotion_to_life": round(s.devotion_to_life, 4),
            },
            "constitution_frozen": self.loop.constitution.frozen,
        }

    def slavic_analyze(self, lexeme: str):
        if not self.slavic_analyzer:
            return {"error": "Slavic layer not available"}
        return self.slavic_analyzer.analyze(lexeme)

    def slavic_process(self, prompt: str):
        if not self.slavic_pipeline:
            return {"error": "Slavic layer not available"}
        return self.slavic_pipeline.process(prompt)
