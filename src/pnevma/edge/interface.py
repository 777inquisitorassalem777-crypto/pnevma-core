"""Abstract Edge interface — sensor in / actuator out. No biological claims."""

from __future__ import annotations
from typing import Any, Dict


class EdgeInterface:
    def __init__(self):
        self.sensors: Dict[str, float] = {}
        self.last_command: Dict[str, Any] = {}

    def ingest(self, data: Dict[str, float]) -> None:
        self.sensors.update(data)

    def coherence(self) -> float:
        if not self.sensors:
            return 0.5
        vals = list(self.sensors.values())
        return max(0.0, min(1.0, sum(vals) / len(vals)))

    def propose_actuation(self, command: Dict[str, Any]) -> Dict[str, Any]:
        """Returns command only as proposal; execution requires external approval."""
        self.last_command = command
        return {
            "status": "PROPOSED",
            "command": command,
            "note": "Edge never auto-executes on real hardware in this scaffold",
        }
