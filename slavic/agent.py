"""
SlavicCognitiveAgent — полный пайплайн
ВЕДУН → ВОЛХВ → ВЕЩУН → ХАРАКТЕРНИК
ЗНАНИЕ → СЛОВО → ВОЛЯ → ДЕЙСТВИЕ
"""

from __future__ import annotations
from typing import Any, Dict, List, Optional
import json

from .knowledge import Vedun, KnowledgeType, KnowledgeUnit
from .interpretation import Volkhv
from .communication import Veshchun
from .agency import Kharakternik


# Историко-лингвистические семена (fact / hypothesis чётко помечены)
LEXEME_SEEDS = [
    {
        "content": "Волхв ← *vъlxvъ; наиболее убедительно связано с влъснѫти «бормотать». Внутренняя форма: носитель особой ритуальной речи.",
        "type": KnowledgeType.ЭТИМОЛОГИЯ,
        "status": "hypothesis",
        "tags": ["волхв", "этимология", "влъснѫти"],
        "source": "Vasmer / academic consensus",
    },
    {
        "content": "Ведун ← *vědati ← и.-е. *weyd- / wid- («видеть → знать»). Родственно veda, vidēre, οἶδα.",
        "type": KnowledgeType.ЭТИМОЛОГИЯ,
        "status": "fact",
        "tags": ["ведун", "этимология", "vědati"],
        "source": "Indo-European comparative",
    },
    {
        "content": "Характерник — позднее (XV–XVI вв.) казацкое слово от греч. χαρακτήρ «знак, печать». Не праславянский термин.",
        "type": KnowledgeType.ЭТИМОЛОГИЯ,
        "status": "fact",
        "tags": ["характерник", "этимология", "казачество"],
        "source": "Ukrainian historical lexicography",
    },
    {
        "content": "Слово, правильно произнесённое, в архаической модели участвует в изменении реальности (заговор, обет, благословение).",
        "type": KnowledgeType.СЛОВО,
        "status": "interpretation",
        "tags": ["слово", "заговор", "бая"],
        "source": "folklore semantics",
    },
    {
        "content": "Огонь очищает и преображает",
        "type": KnowledgeType.ПРИРОДА,
        "status": "interpretation",
        "tags": ["огонь", "сила"],
        "source": "symbolic",
    },
    {
        "content": "Болезнь — нарушение баланса (народная модель)",
        "type": KnowledgeType.БОЛЕЗНЬ,
        "status": "interpretation",
        "tags": ["лечение", "баланс"],
        "source": "folk medicine semantics",
    },
]


class SlavicCognitiveAgent:
    """
    Когнитивный агент на основе славянской семантической системы ролей.
    Строго разделяет:
    - историко-лингвистический уровень (fact / hypothesis)
    - смысловую интерпретацию
    Не утверждает существование единой «праславянской религии» или сверхъестественных способностей.
    """

    def __init__(self, name: str = "Славянский Семантический Агент"):
        self.name = name
        self.vedun = Vedun()
        self.volkhv = Volkhv(self.vedun)
        self.veshchun = Veshchun(self.volkhv)
        self.kharakternik = Kharakternik(self.veshchun)
        self._seed()

    def _seed(self):
        for s in LEXEME_SEEDS:
            self.vedun.learn(
                content=s["content"],
                ktype=s["type"],
                tags=s["tags"],
                status=s["status"],
                source=s["source"],
            )

    def perceive_and_act(self, observation: str, goal: str) -> Dict[str, Any]:
        knowledge = self.vedun.recognize(observation)
        interpretation = self.volkhv.interpret(knowledge)
        proclamation = self.veshchun.proclaim(interpretation, style="ритуальный")
        intention = self.kharakternik.set_intention(goal, priority=0.8)
        action = self.kharakternik.act(intention)

        return {
            "observation": observation,
            "knowledge_found": [k.to_dict() for k in knowledge],
            "interpretation": interpretation,
            "proclamation": proclamation,
            "intention": {"goal": intention.goal, "priority": intention.priority},
            "action": {
                "name": action.name,
                "success": action.success,
                "feedback": action.feedback,
                "description": action.description,
            },
            "pipeline": "ВЕДУН → ВОЛХВ → ВЕЩУН → ХАРАКТЕРНИК",
            "formula": "ЗНАНИЕ → СЛОВО → ВОЛЯ → ДЕЙСТВИЕ",
            "disclaimer": (
                "Историко-лингвистический уровень и смысловая интерпретация разделены. "
                "Не претендует на сверхъестественные способности или единую праславянскую религию."
            ),
        }

    def analyze_lexeme(self, lexeme: str) -> Dict[str, Any]:
        knowledge = self.vedun.know(lexeme)
        facts = [k for k in knowledge if k.status == "fact"]
        hyps = [k for k in knowledge if k.status == "hypothesis"]
        interps = [k for k in knowledge if k.status == "interpretation"]
        interpretation = self.volkhv.interpret(knowledge)
        proclamation = self.veshchun.proclaim(interpretation)

        return {
            "lexeme": lexeme,
            "historical_linguistic": {
                "facts": [k.to_dict() for k in facts],
                "hypotheses": [k.to_dict() for k in hyps],
            },
            "semantic_interpretation": {
                "items": [k.to_dict() for k in interps],
                "volkhv": interpretation,
                "proclamation": proclamation,
            },
            "disclaimer": "Dual-level analysis: fact/hypothesis vs interpretation. No magical claims.",
        }

    def status(self) -> Dict[str, Any]:
        return {
            "name": self.name,
            "knowledge": self.vedun.stats(),
            "character": self.kharakternik.character_traits,
            "actions": len(self.kharakternik.actions_history),
            "proclamations": len(self.veshchun.history),
        }
