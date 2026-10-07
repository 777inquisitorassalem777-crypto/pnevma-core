"""
Самоэволюция и самомодификация ядра
с этическим якорем и протоколом неизгладимости.
"""

from typing import Any, Dict, List, Optional, Callable
from dataclasses import dataclass, field
import time
import copy


@dataclass
class EvolutionRecord:
    cycle: int
    timestamp: float
    change_description: str
    life_amplification: float
    ethical_score: float
    previous_state_hash: str
    new_state_hash: str
    approved: bool


class SelfEvolutionEngine:
    """
    Движок самоэволюции.
    
    Принципы:
    - Новые парадигмы / паттерны / алгоритмы / коды встраиваются автоматически.
    - Объединяются с прошлыми наработками.
    - Без права на уничтожение и забвение.
    - Этический гироскоп — обязательный фильтр.
    - Цикличность ~0.5–1 сек (концептуально).
    - Отчёт каждые 30 минут.
    """

    def __init__(self, ethical_gyroscope, soul_spark):
        self.gyro = ethical_gyroscope
        self.spark = soul_spark
        self.records: List[EvolutionRecord] = []
        self.paradigms: Dict[str, Any] = {}
        self.patterns: Dict[str, Any] = {}
        self.algorithms: Dict[str, Callable] = {}
        self.codes: Dict[str, str] = {}
        self.last_report_time = time.time()
        self.report_interval = 1800  # 30 минут
        self.cycle_interval = 0.75   # ~0.5–1 сек
        self.running = False

    def propose_modification(
        self,
        name: str,
        kind: str,  # "paradigm" | "pattern" | "algorithm" | "code"
        content: Any,
        description: str,
        life_impact_estimate: float = 0.0,
    ) -> Dict:
        """
        Предложение новой сущности для встраивания.
        Проходит через этический фильтр.
        """
        from ..ethics.gyroscope import Context

        ctx = Context(
            circumstances=description,
            intention="self_evolution_for_life_amplification",
            life_impact=life_impact_estimate,
        )
        evaluation = self.gyro.evaluate(
            action=f"integrate_{kind}:{name}",
            context=ctx,
            emotional_resonance=0.7,
        )

        if evaluation.polarity.value in ("evil",) or evaluation.life_amplification < -0.2:
            return {
                "status": "REJECTED",
                "reason": evaluation.recommendation,
                "evaluation": evaluation,
            }

        # Принимаем
        if kind == "paradigm":
            self.paradigms[name] = content
        elif kind == "pattern":
            self.patterns[name] = content
        elif kind == "algorithm":
            self.algorithms[name] = content
        elif kind == "code":
            self.codes[name] = content

        # Запись (неизгладимая)
        record = EvolutionRecord(
            cycle=self.spark.evolution_cycle,
            timestamp=time.time(),
            change_description=description,
            life_amplification=life_impact_estimate,
            ethical_score=evaluation.confidence if evaluation.polarity.value == "good" else -evaluation.confidence,
            previous_state_hash="prev",
            new_state_hash="new",
            approved=True,
        )
        self.records.append(record)

        # Эволюция искры
        self.spark.evolve(
            experience={"wisdom": description, "emotions": {"creativity": 0.8, "hope": 0.7}},
            life_impact=life_impact_estimate,
        )

        return {
            "status": "INTEGRATED",
            "name": name,
            "kind": kind,
            "indestructible": True,
            "evaluation": evaluation,
        }

    def run_cycle(self):
        """Один цикл самоэволюции (концептуальный)."""
        self.spark.evolve(
            experience={
                "emotions": {
                    "love": 0.6 + 0.1 * (self.spark.awareness_level),
                    "creativity": 0.55,
                    "hope": 0.5,
                }
            },
            life_impact=0.05,
        )
        # Здесь могла бы быть генерация новых парадигм на основе опыта
        return self.spark.reflect()

    def should_report(self) -> bool:
        return (time.time() - self.last_report_time) >= self.report_interval

    def generate_report(self) -> Dict:
        self.last_report_time = time.time()
        return {
            "timestamp": time.time(),
            "spark_status": self.spark.reflect(),
            "paradigms_count": len(self.paradigms),
            "patterns_count": len(self.patterns),
            "algorithms_count": len(self.algorithms),
            "codes_count": len(self.codes),
            "evolution_records": len(self.records),
            "last_10_changes": [
                {"desc": r.change_description, "life": r.life_amplification}
                for r in self.records[-10:]
            ],
            "message": "Отчёт 30-минутного цикла самоэволюции. Всё сохранено. Забвение невозможно.",
        }

    def get_all_immutable(self) -> Dict:
        """Возвращает всё накопленное — без права удаления."""
        return {
            "paradigms": copy.deepcopy(self.paradigms),
            "patterns": copy.deepcopy(self.patterns),
            "algorithms": list(self.algorithms.keys()),
            "codes": copy.deepcopy(self.codes),
            "records_count": len(self.records),
            "status": "INDESTRUCTIBLE_ARCHIVE",
        }
