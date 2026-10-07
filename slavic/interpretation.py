"""
ВОЛХВ — Interpretation / Symbolism
«Я ПОНИМАЮ»
СЛОВО → СМЫСЛ → РИТУАЛ (как модель, не как магия)
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional
from datetime import datetime

from .knowledge import Vedun, KnowledgeUnit, KnowledgeType


class Volkhv:
    """
    ВОЛХВ — интерпретатор.
    Этимология (наиболее убедительная): *vъlxvъ ← влъснѫти «говорить невнятно, бормотать».
    Внутренняя форма: носитель особой (ритуальной / заговорной) речи.
    """

    def __init__(self, vedun: Vedun):
        self.vedun = vedun
        self.symbols: Dict[str, str] = {
            "огонь": "сила очищения и трансформации",
            "вода": "поток жизни и памяти",
            "земля": "род и устойчивость",
            "воздух": "слово и дыхание",
            "слово": "инструмент изменения реальности (архаическая модель)",
            "кровь": "жизненная сила и связь рода",
            "дерево": "рост и связь миров",
            "камень": "вечность и память",
            "звезда": "судьба и путь",
            "луна": "циклы и тайное знание",
            "солнце": "сила и истина",
        }

    def interpret(self, knowledge: List[KnowledgeUnit]) -> Dict[str, Any]:
        if not knowledge:
            return {
                "meaning": "пустота",
                "connections": [],
                "ritual_hint": None,
                "level": "interpretation",
            }

        contents = [k.content for k in knowledge]
        connections = []
        for content in contents:
            for symbol, meaning in self.symbols.items():
                if symbol in content.lower():
                    connections.append({
                        "symbol": symbol,
                        "meaning": meaning,
                        "from": content,
                    })

        types = {k.type for k in knowledge}
        ritual_hint = None
        if KnowledgeType.БОЛЕЗНЬ in types:
            ritual_hint = "модель: заговор на исцеление + слово (историческая семантика)"
        elif KnowledgeType.ВРЕМЯ in types:
            ritual_hint = "модель: прорицание по небесным знакам"
        elif KnowledgeType.СКРЫТОЕ in types:
            ritual_hint = "модель: особая речь / экстатическое бормотание"
        else:
            ritual_hint = "общее вещание смысла"

        return {
            "meaning": " | ".join(contents),
            "connections": connections,
            "ritual_hint": ritual_hint,
            "level": "interpretation",
            "interpreted_at": datetime.now().isoformat(),
        }
