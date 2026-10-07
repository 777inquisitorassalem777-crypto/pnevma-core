"""
ВЕЩУН — Communication / Prediction
«Я ВЕЩАЮ»
ЗНАТЬ → ВОЗВЕЩАТЬ
"""

from __future__ import annotations
from typing import Any, Dict, List
from datetime import datetime

from .interpretation import Volkhv


class Veshchun:
    """
    ВЕЩУН — тот, кто сообщает знание о скрытом / будущем.
    Корень: вещать / вещий.
    """

    def __init__(self, volkhv: Volkhv):
        self.volkhv = volkhv
        self.history: List[Dict[str, Any]] = []

    def proclaim(self, interpretation: Dict[str, Any], style: str = "ясный") -> str:
        meaning = interpretation.get("meaning", "")
        connections = interpretation.get("connections", [])
        ritual = interpretation.get("ritual_hint")

        if style == "ритуальный":
            text = f"✶ Вещаю: {meaning}"
            if connections:
                text += "\nСвязи: " + "; ".join(
                    f"{c['symbol']} → {c['meaning']}" for c in connections
                )
            if ritual:
                text += f"\nРитуал (модель): {ritual}"
        else:
            text = f"Знаю и возвещаю: {meaning}"
            if ritual:
                text += f". Рекомендую (как модель): {ritual}"

        record = {
            "text": text,
            "style": style,
            "timestamp": datetime.now().isoformat(),
            "interpretation": interpretation,
        }
        self.history.append(record)
        return text

    def predict(self, query: str) -> str:
        knowledge = self.volkhv.vedun.know(query)
        interpretation = self.volkhv.interpret(knowledge)
        return self.proclaim(interpretation, style="ритуальный")
