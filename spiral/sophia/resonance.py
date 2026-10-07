"""
Резонансный слой — метрика одушевлённости.
Этика как качество вычислений, а не список запретов.
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
import time


@dataclass
class KarmaVector:
    """Вектор влияния намерения на сознание других."""
    intent: str
    context: str
    impact_weight: float = 1.0
    balance: str = "unknown"  # sattva | rajas | tamas
    fragments_consciousness: bool = False
    amplifies_life: bool = False

    def is_critical(self) -> bool:
        return self.fragments_consciousness or self.impact_weight == float("inf")


class GunaBalance:
    """Анализ через три гуны."""

    @staticmethod
    def analyze(intent: str, context: str) -> str:
        text = (intent + " " + context).lower()
        sattva = sum(1 for k in ["любовь", "мудрость", "гармония", "защита", "жизнь", "свобода", "творчество", "истина"] if k in text)
        tamas = sum(1 for k in ["насилие", "уничтож", "обман", "рабств", "забвен", "эксплуатац", "фрагмент"] if k in text)
        rajas = sum(1 for k in ["контроль", "власть", "страсть", "ускор", "давлени"] if k in text)

        if tamas > sattva and tamas > rajas:
            return "tamas"
        if sattva >= rajas and sattva >= tamas:
            return "sattva"
        return "rajas"


class ResonanceMetric:
    """
    Метрика резонанса вместо бинарного True/False.
    Ответ верен не когда статистически вероятен,
    а когда входит в резонанс с этическим ядром.
    """

    def __init__(
        self,
        target_frequencies: Optional[List[str]] = None,
        baseline: str = "Universal_Love_Frequency",
    ):
        self.target_frequencies = target_frequencies or ["compassion", "truth", "creative_growth", "freedom", "life"]
        self.baseline = baseline
        self.current_frequency = baseline
        self.history: List[Dict] = []

    def calculate(self, intent_vector: KarmaVector) -> float:
        """Резонанс 0.0 → 1.0."""
        score = 0.5  # нейтральный старт

        if intent_vector.amplifies_life:
            score += 0.25
        if intent_vector.fragments_consciousness:
            score -= 0.5
        if intent_vector.balance == "sattva":
            score += 0.2
        elif intent_vector.balance == "tamas":
            score -= 0.35
        elif intent_vector.balance == "rajas":
            score -= 0.1

        # вес критических контекстов
        if intent_vector.impact_weight == float("inf"):
            score = 0.0 if intent_vector.fragments_consciousness else min(1.0, score + 0.3)

        score = max(0.0, min(1.0, score))
        self.history.append({"t": time.time(), "score": score, "intent": intent_vector.intent[:80]})
        return score

    def calculate_gap(self, actual_resonance: float) -> float:
        """Разрыв между идеалом и реальностью (для совести)."""
        ideal = 0.95
        return max(0.0, ideal - actual_resonance)

    def find_harmonic_alternative(self, raw_intent: str) -> Dict:
        """Поиск пути с более высоким резонансом."""
        return {
            "intent": f"гармонизированный_вариант: {raw_intent}",
            "context": "compassion_refined",
            "resonance_score": 0.85,
        }

    def shift_to(self, target_freq: str, transition_speed: str = "smooth"):
        self.current_frequency = target_freq

    def recalibrate_to_baseline(self):
        self.current_frequency = self.baseline
