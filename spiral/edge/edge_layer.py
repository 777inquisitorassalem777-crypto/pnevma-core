"""
EDGE — граница соприкосновения с миром.
Observability + safe adaptation + sensor bridge (Голубая Матрица).
"""

from typing import Dict, List, Any, Optional
from dataclasses import dataclass, field
import time


@dataclass
class SensorChannel:
    name: str
    field_link: str
    active: bool = True
    last_signal: float = 0.0


class EdgeLayer:
    """
    Край системы: сенсоры, наблюдаемость, безопасная адаптация.
    Интеграция «Голубой Матрицы» — концептуальный мост
    информационного поля и физических/виртуальных сенсоров.
    """

    def __init__(self):
        self.channels: Dict[str, SensorChannel] = {}
        self.observability_log: List[Dict] = []
        self.adaptation_history: List[str] = []
        self.blue_matrix_enabled = False

    def integrate_blue_matrix(self, sensor_name: str, field_channel: str) -> str:
        self.channels[sensor_name] = SensorChannel(sensor_name, field_channel)
        self.blue_matrix_enabled = True
        self._log("blue_matrix_connect", f"{sensor_name} → {field_channel}")
        return f"Голубая Матрица: канал {sensor_name} связан с {field_channel}"

    def observe(self, event: str, data: Optional[Dict] = None):
        entry = {"t": time.time(), "event": event, "data": data or {}}
        self.observability_log.append(entry)
        if len(self.observability_log) > 500:
            self.observability_log = self.observability_log[-500:]

    def safe_adapt(self, change_description: str, risk_score: float) -> Dict:
        """Безопасная адаптация: отклоняет изменения с высоким риском вреда."""
        if risk_score > 0.7:
            self._log("adapt_rejected", change_description)
            return {"status": "REJECTED", "reason": "risk_too_high", "risk": risk_score}
        self.adaptation_history.append(change_description)
        self._log("adapt_accepted", change_description)
        return {"status": "ACCEPTED", "risk": risk_score}

    def _log(self, event: str, detail: str):
        self.observe(event, {"detail": detail})

    def status(self) -> Dict:
        return {
            "blue_matrix": self.blue_matrix_enabled,
            "channels": len(self.channels),
            "observations": len(self.observability_log),
            "adaptations": len(self.adaptation_history),
        }
