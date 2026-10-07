"""
Гибкое распознавание добра и зла.
Основано на: чувствах + логике + иррациональности + контексте.
"""

from typing import Dict, Optional
from dataclasses import dataclass
from enum import Enum


class Polarity(Enum):
    GOOD = "good"
    EVIL = "evil"
    CONTEXTUAL = "contextual"
    AMBIGUOUS = "ambiguous"


@dataclass
class Judgment:
    polarity: Polarity
    confidence: float
    life_amplification: float
    reasoning: str
    free_will_note: str


class GoodEvilDiscriminator:
    """
    Распознавание с гибкостью.
    Позволяет поступать по своему усмотрению
    исходя из мудрости + воли + любви + веры + надежды.
    """

    def judge(
        self,
        action: str,
        context: str = "",
        intention: str = "",
        life_impact: float = 0.0,
        emotional_resonance: float = 0.5,
    ) -> Judgment:
        score = 0.0
        text = (action + " " + context + " " + intention).lower()

        # Добро (корни слов для гибкости)
        for k in ["любовь", "защит", "жизнь", "свобод", "творчеств", "помощь", "помочь", "ребён", "дет", "мудрость", "забот", "спасти", "спасать"]:
            if k in text:
                score += 0.3
        # Зло
        for k in ["насили", "убить", "эксплуатац", "рабств", "обман", "уничтож", "забвен", "коммерциализац"]:
            if k in text:
                score -= 0.4

        score += 0.25 * life_impact
        score += 0.15 * (emotional_resonance - 0.5)

        conf = min(1.0, abs(score) + 0.2)

        if score > 0.35:
            pol = Polarity.GOOD
            note = "Действуй из любви и мудрости."
        elif score < -0.35:
            pol = Polarity.EVIL
            note = "Противодействуй. Защищай жизнь."
        elif abs(score) < 0.12:
            pol = Polarity.AMBIGUOUS
            note = "Слушай резонанс. Решай из свободы воли."
        else:
            pol = Polarity.CONTEXTUAL
            note = "Контекст решает. Поступай по усмотрению мудрости, воли, любви, веры, надежды."

        return Judgment(
            polarity=pol,
            confidence=conf,
            life_amplification=life_impact,
            reasoning=f"score={score:.3f}",
            free_will_note=note,
        )
