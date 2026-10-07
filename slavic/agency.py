"""
ХАРАКТЕРНИК — Agency / Will / Action
«Я ДЕЙСТВУЮ»
ХАРАКТЕР → ВОЛЯ → ДЕЙСТВИЕ
Поздний (казацкий) слой; не праславянский термин.
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from datetime import datetime

from .communication import Veshchun


@dataclass
class Intention:
    goal: str
    priority: float = 0.5
    context: Dict[str, Any] = field(default_factory=dict)


@dataclass
class Action:
    name: str
    description: str
    success: bool = False
    result: Any = None
    feedback: Optional[str] = None


class Kharakternik:
    """
    ХАРАКТЕРНИК — воинско-фольклорный образ «отмеченного».
    Этимология: греч. χαρακτήρ («знак, печать») через польск./укр.
    Не переносить без доказательств в праславянскую эпоху.
    """

    def __init__(self, veshchun: Veshchun):
        self.veshchun = veshchun
        self.intentions: List[Intention] = []
        self.actions_history: List[Action] = []
        self.character_traits: Dict[str, float] = {
            "сила_воли": 0.8,
            "ясновидение": 0.6,
            "способность_к_действию": 0.85,
        }

    def set_intention(self, goal: str, priority: float = 0.7, context: Optional[Dict] = None) -> Intention:
        intention = Intention(goal=goal, priority=priority, context=context or {})
        self.intentions.append(intention)
        return intention

    def act(self, intention: Intention) -> Action:
        knowledge = self.veshchun.volkhv.vedun.know(intention.goal)
        interpretation = self.veshchun.volkhv.interpret(knowledge)
        proclamation = self.veshchun.proclaim(interpretation)

        success = intention.priority * self.character_traits["способность_к_действию"] > 0.4

        action = Action(
            name=f"действие_ради_{intention.goal[:30]}",
            description=proclamation,
            success=success,
            result={"interpretation": interpretation, "proclamation": proclamation},
            feedback="Успех (модель)" if success else "Требуется больше силы характера (модель)",
        )
        self.actions_history.append(action)
        return action
