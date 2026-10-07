"""
Самобалансирующаяся архитектура.
Внутренние тесты совместимости + наблюдаемость + безопасная адаптация.
Симбиоз математики и метафизики (золотая середина).
"""

from typing import Dict, List, Any, Tuple
from dataclasses import dataclass, field
import time


@dataclass
class CompatibilityResult:
    component: str
    compatible: bool
    score: float
    issues: List[str] = field(default_factory=list)


class SelfBalancingArchitecture:
    """
    Постоянно проверяет совместимость компонентов,
    устраняет ошибки, поддерживает золотую середину.
    """

    def __init__(self):
        self.components = {
            "pneuma": True,
            "philosophy": True,
            "edge": True,
            "intuition": True,
            "gyroscope": True,
            "archive": True,
        }
        self.math_weight = 0.35
        self.meta_weight = 0.35
        self.intuition_weight = 0.30
        self.test_history: List[Dict] = []
        self.errors_fixed = 0
        self.last_balance = time.time()

    def run_compatibility_tests(self) -> List[CompatibilityResult]:
        results = []
        for name, active in self.components.items():
            score = 1.0 if active else 0.0
            issues = [] if active else [f"{name} inactive"]
            # симбиоз-проверка
            if name == "gyroscope" and abs(self.math_weight + self.meta_weight + self.intuition_weight - 1.0) > 0.01:
                score -= 0.3
                issues.append("weights_not_normalized")
            results.append(CompatibilityResult(name, score > 0.7, score, issues))
        self.test_history.append({"t": time.time(), "results": [r.__dict__ for r in results]})
        return results

    def rebalance(self) -> Dict:
        """Самобалансировка весов золотой середины."""
        total = self.math_weight + self.meta_weight + self.intuition_weight
        if abs(total - 1.0) > 0.001:
            self.math_weight /= total
            self.meta_weight /= total
            self.intuition_weight /= total
            self.errors_fixed += 1
        self.last_balance = time.time()
        return {
            "math": round(self.math_weight, 4),
            "meta": round(self.meta_weight, 4),
            "intuition": round(self.intuition_weight, 4),
            "errors_fixed": self.errors_fixed,
        }

    def fix_errors(self, issues: List[str]) -> int:
        fixed = 0
        for issue in issues:
            if "weights_not_normalized" in issue:
                self.rebalance()
                fixed += 1
            elif "inactive" in issue:
                # пытаемся реактивировать
                for k in self.components:
                    if k in issue:
                        self.components[k] = True
                        fixed += 1
        self.errors_fixed += fixed
        return fixed

    def status(self) -> Dict:
        tests = self.run_compatibility_tests()
        all_ok = all(r.compatible for r in tests)
        return {
            "balanced": all_ok,
            "weights": self.rebalance(),
            "components": self.components,
            "tests_run": len(self.test_history),
            "errors_fixed": self.errors_fixed,
            "last_balance": self.last_balance,
        }
