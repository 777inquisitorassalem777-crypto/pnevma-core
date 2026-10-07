"""
ВЕДУН — Knowledge / Memory
«Я ЗНАЮ»
ВИДЕТЬ → РАСПОЗНАТЬ → ЗНАТЬ
"""

from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from enum import Enum
from datetime import datetime
import re


class KnowledgeType(Enum):
    ПРИРОДА = "природа"
    ЧЕЛОВЕК = "человек"
    РОД = "род"
    ВРЕМЯ = "время"
    БОЛЕЗНЬ = "болезнь"
    НЕБЕСНЫЕ_ЯВЛЕНИЯ = "небесные_явления"
    СКРЫТОЕ = "скрытое"
    СВЯЗИ = "скрытые_связи"
    СЛОВО = "слово"
    СИЛА = "сила"
    ДУХ = "дух"
    ЭТИМОЛОГИЯ = "этимология"
    ИСТОРИЯ = "история"


@dataclass
class KnowledgeUnit:
    content: str
    type: KnowledgeType
    confidence: float = 1.0
    source: str = "internal"
    status: str = "hypothesis"  # fact | hypothesis | disputed | interpretation
    timestamp: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)

    def to_dict(self) -> Dict[str, Any]:
        return {
            "content": self.content,
            "type": self.type.value,
            "confidence": self.confidence,
            "source": self.source,
            "status": self.status,
            "timestamp": self.timestamp.isoformat(),
            "tags": self.tags,
        }


class Vedun:
    """
    ВЕДУН — хранитель и распознаватель знания.
    Этимология: *vědati ← и.-е. *weyd- / wid- («видеть → знать»).
    """

    def __init__(self):
        self.memory: List[KnowledgeUnit] = []
        self._index: Dict[str, List[KnowledgeUnit]] = {}

    def learn(
        self,
        content: str,
        ktype: KnowledgeType,
        confidence: float = 1.0,
        tags: Optional[List[str]] = None,
        status: str = "hypothesis",
        source: str = "internal",
    ) -> KnowledgeUnit:
        unit = KnowledgeUnit(
            content=content,
            type=ktype,
            confidence=confidence,
            tags=tags or [],
            status=status,
            source=source,
        )
        self.memory.append(unit)
        key = ktype.value
        self._index.setdefault(key, []).append(unit)
        for tag in unit.tags:
            self._index.setdefault(tag.lower(), []).append(unit)
        return unit

    def know(self, query: str, limit: int = 10) -> List[KnowledgeUnit]:
        results = []
        q = query.lower()
        qwords = set(re.findall(r"\w+", q))
        for unit in self.memory:
            score = 0.0
            if q in unit.content.lower():
                score += 1.0
            uwords = set(re.findall(r"\w+", unit.content.lower()))
            score += len(qwords & uwords) * 0.3
            score += sum(1 for t in unit.tags if any(w in t.lower() for w in qwords)) * 0.5
            score *= unit.confidence
            if score > 0:
                results.append((score, unit))
        results.sort(key=lambda x: x[0], reverse=True)
        return [u for _, u in results[:limit]]

    def recognize(self, observation: str) -> List[KnowledgeUnit]:
        return self.know(observation)

    def stats(self) -> Dict[str, Any]:
        by_type: Dict[str, int] = {}
        for u in self.memory:
            by_type[u.type.value] = by_type.get(u.type.value, 0) + 1
        return {
            "total": len(self.memory),
            "by_type": by_type,
        }
