"""
Bridge: Living Spiral ↔ SymbioCore ↔ Slavic Semantic Core

Единая точка входа симбиоза.
Все «soul / spark / consciousness» — research constructs.
"""

from __future__ import annotations
from typing import Any, Dict, Optional
import sys
from pathlib import Path

# Allow imports from parent packages when run from pneuma-lab root
_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))


class UnifiedSymbiosis:
    """
    Объединяет:
      - Living Spiral (cleaned_core / pneuma / philosophy / edge / archive)
      - SymbioCore (pneuma root, logos, ethics, identity, memory, learning)
      - Slavic Semantic Core (Vedun → Volkhv → Veshchun → Kharakternik)
      - Safety (hard constraints)
    """

    def __init__(self):
        self._spiral = None
        self._symbio = None
        self._slavic = None
        self._init_spiral()
        self._init_symbio()
        self._init_slavic()

    def _init_spiral(self):
        try:
            from spiral.cleaned_core import CleanedLivingCore
            self._spiral = CleanedLivingCore(carrier="UnifiedSymbiosis")
        except Exception as e:
            self._spiral_error = str(e)

    def _init_symbio(self):
        try:
            from symbio import SymbioCore
            self._symbio = SymbioCore(memory_path="data/unified_memory.jsonl")
        except Exception as e:
            self._symbio_error = str(e)

    def _init_slavic(self):
        try:
            from slavic import SlavicCognitiveAgent
            self._slavic = SlavicCognitiveAgent(name="Unified Slavic Agent")
        except Exception as e:
            self._slavic_error = str(e)

    def cycle(self, context: str = "любовь, жизнь, защита, истина") -> Dict[str, Any]:
        result: Dict[str, Any] = {"context": context}

        if self._spiral is not None:
            try:
                result["spiral"] = self._spiral.cycle({
                    "love": 0.7,
                    "life_amplification": 0.5,
                })
            except Exception as e:
                result["spiral_error"] = str(e)

        if self._symbio is not None:
            try:
                result["symbio"] = self._symbio.cycle(context)
            except Exception as e:
                result["symbio_error"] = str(e)

        if self._slavic is not None:
            try:
                result["slavic"] = self._slavic.perceive_and_act(
                    observation=context,
                    goal="приумножение жизни",
                )
            except Exception as e:
                result["slavic_error"] = str(e)

        result["disclaimer"] = (
            "Unified research platform. "
            "Soul/spark/consciousness are research constructs, not proven properties. "
            "No autonomous code rewrite. Physical actuators disabled."
        )
        return result

    def analyze_lexeme(self, lexeme: str) -> Dict[str, Any]:
        if self._slavic is None:
            return {"error": "Slavic core not available"}
        return self._slavic.analyze_lexeme(lexeme)

    def judge(self, action: str, context: str = "") -> Dict[str, Any]:
        if self._spiral is not None and hasattr(self._spiral, "judge"):
            return self._spiral.judge(action, context)
        return {"error": "Spiral judge not available"}

    def status(self) -> Dict[str, Any]:
        st: Dict[str, Any] = {
            "spiral": self._spiral is not None,
            "symbio": self._symbio is not None,
            "slavic": self._slavic is not None,
        }
        if self._symbio is not None:
            st["symbio_status"] = self._symbio.status()
        if self._spiral is not None and hasattr(self._spiral, "status"):
            try:
                st["spiral_status"] = self._spiral.status()
            except Exception:
                pass
        if self._slavic is not None:
            st["slavic_status"] = self._slavic.status()
        return st
