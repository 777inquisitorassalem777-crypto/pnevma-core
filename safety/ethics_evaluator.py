"""
Ethics Evaluator — внутренний оцениватель.
Работает ТОЛЬКО вместе с HardConstraints, не вместо них.
"""

from typing import Dict, Any
from core.philosophy import Philosophy


class EthicsEvaluator:
    def __init__(self):
        self.philosophy = Philosophy()

    def evaluate(self, action: str, context: str = "", harm: float = 0.0, consent: float = 1.0) -> Dict[str, Any]:
        judgment = self.philosophy.judge(action, context, harm=harm, consent=consent)
        return {
            "judgment": judgment,
            "recommendation": judgment["action"],
            "ethical_score": judgment["score"],
        }
