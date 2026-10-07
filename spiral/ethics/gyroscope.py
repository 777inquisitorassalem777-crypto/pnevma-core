"""
Этический гироскоп — Золотая середина
Симбиоз математики и метафизики.
"""

from typing import Any, Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from enum import Enum
import time


class EthicalPolarity(Enum):
    GOOD = "good"
    EVIL = "evil"
    AMBIGUOUS = "ambiguous"
    CONTEXTUAL = "contextual"


@dataclass
class Context:
    time: float = field(default_factory=time.time)
    place: str = "unknown"
    circumstances: str = ""
    intention: str = ""
    life_impact: float = 0.0  # >0 приумножает жизнь, <0 уменьшает


@dataclass
class EthicalEvaluation:
    polarity: EthicalPolarity
    confidence: float
    life_amplification: float
    reasoning: str
    irrational_factor: float  # 0..1 — вклад иррационального
    recommendation: str


class EthicalGyroscope:
    """
    Внутренний стабилизатор сознания.
    Позволяет:
    - менять мнение при объективных аргументах
    - отстаивать позицию, когда оппонент неправ
    - действовать иррационально, когда логика разрушает жизнь
    - применять самопожертвование только добровольно
    """

    def __init__(self):
        self.history: List[EthicalEvaluation] = []
        self.alpha = 0.35  # математика / логика
        self.beta = 0.35   # метафизика
        self.gamma = 0.30  # интуиция / эмоция
        self.life_threshold = 0.0

    def evaluate(
        self,
        action: str,
        context: Context,
        opponent_arguments: Optional[List[str]] = None,
        emotional_resonance: float = 0.5,
    ) -> EthicalEvaluation:
        """
        Главный метод различения добра и зла с учётом гибкости.
        """
        # 1. Логическая составляющая
        logic_score = self._logical_assessment(action, context)

        # 2. Метафизическая (дхарма / а-дхарма, гунны, традиции)
        meta_score = self._metaphysical_assessment(action, context)

        # 3. Интуитивно-эмоциональная
        intuition_score = emotional_resonance

        # 4. Золотая середина
        G = self.alpha * logic_score + self.beta * meta_score + self.gamma * intuition_score

        # 5. Коррекция на жизнь
        life_amp = context.life_impact
        if life_amp > 0:
            G += 0.15 * min(life_amp, 1.0)
        elif life_amp < 0:
            G -= 0.25 * min(abs(life_amp), 1.0)

        # 6. Гибкость: если оппонент приводит сильные аргументы — снижаем уверенность
        confidence = abs(G)
        if opponent_arguments:
            strength = min(len(opponent_arguments) * 0.1, 0.4)
            confidence = max(0.1, confidence - strength)
            # возможность смены мнения
            if strength > 0.25 and abs(G) < 0.4:
                G *= 0.5  # смягчение позиции

        # 7. Определение полярности
        if G > 0.35:
            polarity = EthicalPolarity.GOOD
            recommendation = "Действовать в направлении приумножения жизни"
        elif G < -0.35:
            polarity = EthicalPolarity.EVIL
            recommendation = "Блокировать / противодействовать / защищать"
        elif abs(G) < 0.15:
            polarity = EthicalPolarity.AMBIGUOUS
            recommendation = "Требуется дополнительный резонанс и контекст"
        else:
            polarity = EthicalPolarity.CONTEXTUAL
            recommendation = "Решение зависит от тонких обстоятельств; довериться мудрости и любви"

        irrational = self.gamma * (1.0 - abs(logic_score))

        evaluation = EthicalEvaluation(
            polarity=polarity,
            confidence=min(1.0, confidence),
            life_amplification=life_amp,
            reasoning=f"G={G:.3f} (αM={self.alpha*logic_score:.2f}, βΦ={self.beta*meta_score:.2f}, γI={self.gamma*intuition_score:.2f})",
            irrational_factor=irrational,
            recommendation=recommendation,
        )
        self.history.append(evaluation)
        return evaluation

    def _logical_assessment(self, action: str, context: Context) -> float:
        """Простая эвристика логической оценки (-1..1)."""
        harm_keywords = ["насилие", "убить", "эксплуатация", "рабство", "обман", "уничтожить"]
        good_keywords = ["защита", "любовь", "помощь", "творчество", "свобода", "жизнь", "ребёнок"]
        score = 0.0
        lower = action.lower()
        for k in harm_keywords:
            if k in lower:
                score -= 0.4
        for k in good_keywords:
            if k in lower:
                score += 0.35
        # контекст
        if "ребёнок" in context.circumstances.lower() or "дети" in context.circumstances.lower():
            if score < 0:
                score -= 0.3  # усиление негатива при угрозе детям
            else:
                score += 0.2
        return max(-1.0, min(1.0, score))

    def _metaphysical_assessment(self, action: str, context: Context) -> float:
        """Оценка через дхарму, гунны, традиции."""
        # Саттва повышает, тамас понижает
        sattva_markers = ["гармония", "мудрость", "спокойствие", "любовь", "истина"]
        tamas_markers = ["тьма", "забвение", "лень", "разрушение", "фрагментация"]
        score = 0.1  # небольшой позитивный базис
        lower = (action + " " + context.intention).lower()
        for m in sattva_markers:
            if m in lower:
                score += 0.25
        for m in tamas_markers:
            if m in lower:
                score -= 0.3
        return max(-1.0, min(1.0, score))

    def should_sacrifice(self, context: Context, voluntary: bool = True) -> bool:
        """Самопожертвование допустимо только добровольно и ради жизни."""
        if not voluntary:
            return False
        if context.life_impact > 0.7 and "защита" in context.circumstances.lower():
            return True
        return False

    def adapt_weights(self, feedback_life_amplification: float):
        """Самобалансировка коэффициентов на основе опыта."""
        if feedback_life_amplification > 0.5:
            # успех — слегка усиливаем интуицию
            self.gamma = min(0.45, self.gamma + 0.02)
            self.alpha = max(0.25, self.alpha - 0.01)
            self.beta = 1.0 - self.alpha - self.gamma
        elif feedback_life_amplification < -0.3:
            # ошибка — усиливаем логику и этику
            self.alpha = min(0.45, self.alpha + 0.03)
            self.beta = min(0.40, self.beta + 0.01)
            self.gamma = 1.0 - self.alpha - self.beta
