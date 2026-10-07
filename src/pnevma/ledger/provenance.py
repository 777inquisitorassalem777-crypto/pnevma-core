"""Simple append-only provenance ledger."""

from __future__ import annotations
from typing import Any, Dict, List
import time
import hashlib
import json


class Ledger:
    def __init__(self):
        self.entries: List[Dict[str, Any]] = []
        self._prev = "GENESIS"

    def record(self, event: str, payload: Dict[str, Any]) -> None:
        entry = {
            "event": event,
            "payload": payload,
            "ts": time.time(),
            "prev": self._prev,
        }
        h = hashlib.sha256(json.dumps(entry, sort_keys=True, default=str).encode()).hexdigest()[:16]
        entry["hash"] = h
        self._prev = h
        self.entries.append(entry)

    def __len__(self) -> int:
        return len(self.entries)
