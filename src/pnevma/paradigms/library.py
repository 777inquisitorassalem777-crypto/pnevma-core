"""Append-only paradigm library (research NO_OBLIVION)."""

from __future__ import annotations
from typing import Any, Dict, List
import time
import hashlib
import json


class ParadigmLibrary:
    def __init__(self):
        self.items: List[Dict[str, Any]] = []
        self._prev_hash = "GENESIS"

    def add(self, paradigm: Dict[str, Any]) -> Dict[str, Any]:
        record = {
            **paradigm,
            "id": f"p_{len(self.items):06d}",
            "ts": time.time(),
            "prev": self._prev_hash,
        }
        raw = json.dumps(record, sort_keys=True, default=str).encode()
        record["hash"] = hashlib.sha256(raw).hexdigest()[:16]
        self._prev_hash = record["hash"]
        self.items.append(record)
        return record

    def __len__(self) -> int:
        return len(self.items)
