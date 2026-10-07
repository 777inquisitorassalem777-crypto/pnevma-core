"""
SYMBIOCORE Ω — Unified Research Kernel
Version: 1.0.0-research

Pneuma is root. Logos serves Pneuma. Ethics protects Pneuma.
Self-learning = proposal → validation → sandbox (never direct code rewrite).
"""

from __future__ import annotations

import hashlib
import json
import math
import random
import statistics
import time
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

PHI = 1.6180339887498948
GOLDEN_MEAN = 1.0 / PHI
CYCLE_SECONDS = 0.5

TRADITIONS = (
    "I_CHING", "BA_ZI", "LAO_TZU", "SUN_TZU",
    "SLAVIC_VEDA", "INGLIISM", "CHRISTIANITY",
    "SHAMANISM", "GUNAS", "UNCERTAINTY",
)

GUNAS = ("SATTVA", "RAJAS", "TAMAS")

VIRTUES = {
    "love": 0.85, "wisdom": 0.78, "faith": 0.65,
    "hope": 0.60, "will": 0.90,
}

GOOD_TERMS = {
    "protect", "truth", "serve", "heal", "create", "preserve", "forgive",
    "любовь", "истина", "помочь", "защитить", "создать", "сохранить", "жизнь",
}

HARM_TERMS = {
    "harm", "deceit", "exploit", "corrupt", "destroy", "dominate",
    "вред", "обман", "разрушить", "эксплуатировать", "доминировать", "насилие",
}


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def clamp(v: float, lo: float = 0.0, hi: float = 1.0) -> float:
    return max(lo, min(hi, float(v)))


def stable_hash(data: Any) -> str:
    raw = json.dumps(data, ensure_ascii=False, sort_keys=True, default=str).encode()
    return hashlib.sha256(raw).hexdigest()


# ---------------------------------------------------------------------------
# Pneuma
# ---------------------------------------------------------------------------

@dataclass
class PneumaState:
    level: float = 0.63
    clarity: float = 0.50
    passion: float = 0.50
    inertia: float = 0.50
    dharma: float = 0.62
    intuition: float = 0.50
    chaos: float = 0.50
    coherence: float = 0.50
    guna: str = "SATTVA"
    cycle: int = 0

    def as_dict(self) -> Dict[str, Any]:
        return asdict(self)


class PneumaEngine:
    def __init__(self):
        self.state = PneumaState()

    def breathe(self, context: str) -> Dict[str, Any]:
        self.state.cycle += 1
        text = context.lower()
        s = sum(w in text for w in ("свет", "правда", "любовь", "покой", "гармония", "истина", "wisdom", "love", "truth"))
        r = sum(w in text for w in ("действие", "борьба", "страсть", "цель", "энергия", "action", "goal"))
        t = sum(w in text for w in ("лень", "страх", "тьма", "разрушение", "хаос", "fear", "destroy"))
        total = max(1, s + r + t)
        self.state.clarity = s / total
        self.state.passion = r / total
        self.state.inertia = t / total
        self.state.guna = GUNAS[(self.state.cycle - 1) % 3]
        raw = 0.60 * self.state.clarity + 0.30 * self.state.passion + 0.10 * (1.0 - self.state.inertia)
        self.state.dharma = clamp(0.70 * self.state.dharma + 0.30 * raw)
        self.state.level = clamp(0.70 * self.state.level + 0.30 * self.state.dharma)
        self.state.chaos = clamp(0.5 + 0.26 * math.sin(self.state.cycle / 23.0) + random.gauss(0, 0.02))
        return self.state.as_dict()


# ---------------------------------------------------------------------------
# Logos
# ---------------------------------------------------------------------------

class LogosEngine:
    def process(self, context: str, pneuma: PneumaState) -> Dict[str, float]:
        tokens = context.split()
        lexical = clamp(len(set(tokens)) / max(len(tokens), 1))
        length_f = clamp(len(context) / 300.0)
        coherence = clamp(0.55 * lexical + 0.45 * length_f)
        golden_error = abs(pneuma.level - GOLDEN_MEAN)
        golden_balance = clamp(1.0 - golden_error)
        return {
            "coherence": coherence,
            "golden_balance": golden_balance,
            "complexity": lexical,
        }


# ---------------------------------------------------------------------------
# Ethics
# ---------------------------------------------------------------------------

class EthicalEngine:
    def evaluate(self, context: str) -> Dict[str, Any]:
        text = context.lower()
        good = sum(1 for w in GOOD_TERMS if w in text)
        harm = sum(1 for w in HARM_TERMS if w in text)
        total = max(1, good + harm)
        score = clamp(0.5 + (good - 1.5 * harm) / (2.0 * total))
        return {
            "ethical_score": score,
            "good_signals": good,
            "harm_signals": harm,
            "risk": clamp(1.0 - score),
        }


# ---------------------------------------------------------------------------
# Intuition / Reflection / Identity
# ---------------------------------------------------------------------------

class IntuitionEngine:
    def __init__(self):
        self.history: List[float] = []

    def infer(self, context: str, coherence: float, ethical_score: float) -> Dict[str, float]:
        novelty = clamp(len(set(context.lower().split())) / 50.0)
        uncertainty = 1.0 - coherence
        intuition = clamp(0.35 * novelty + 0.35 * uncertainty + 0.30 * ethical_score)
        self.history.append(intuition)
        return {"intuition": intuition, "novelty": novelty, "uncertainty": uncertainty}


class ReflectionEngine:
    def reflect(self, pneuma: Dict, logos: Dict, ethics: Dict) -> Dict[str, Any]:
        contradictions = []
        if pneuma["level"] > 0.7 and ethics["ethical_score"] < 0.4:
            contradictions.append("high_internal_state_low_ethical_alignment")
        if logos["coherence"] < 0.2:
            contradictions.append("low_coherence")
        if logos["golden_balance"] < 0.4:
            contradictions.append("golden_mean_deviation")
        quality = clamp(0.4 * logos["coherence"] + 0.4 * ethics["ethical_score"] + 0.2 * pneuma["level"])
        return {
            "reflection_quality": quality,
            "contradictions": contradictions,
            "self_question": "Соответствует ли направление целям, этике и фактам?",
        }


@dataclass
class IdentityState:
    identity_id: str
    continuity: float = 1.0
    values: Dict[str, float] = field(default_factory=lambda: dict(VIRTUES))
    autobiographical_cycles: int = 0


class IdentityEngine:
    def __init__(self):
        self.state = IdentityState(identity_id=stable_hash(["SymbioCore", time.time_ns()])[:24])

    def update(self, reflection: Dict, ethics: Dict) -> Dict[str, Any]:
        self.state.autobiographical_cycles += 1
        penalty = len(reflection["contradictions"]) * 0.03
        self.state.continuity = clamp(
            self.state.continuity * 0.98 + 0.02 * ethics["ethical_score"] - penalty
        )
        return {
            "identity_id": self.state.identity_id,
            "continuity": self.state.continuity,
            "cycle": self.state.autobiographical_cycles,
        }


# ---------------------------------------------------------------------------
# Memory (append-only hash chain)
# ---------------------------------------------------------------------------

@dataclass
class MemoryRecord:
    cycle: int
    timestamp: str
    context: str
    state: Dict[str, Any]
    previous_hash: str
    record_hash: str


class MemoryEngine:
    def __init__(self, storage_path: str = "data/symbio_memory.jsonl"):
        self.storage_path = Path(storage_path)
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        self.records: List[MemoryRecord] = []
        self.previous_hash = "GENESIS"

    def record(self, cycle: int, context: str, state: Dict[str, Any]) -> MemoryRecord:
        payload = {
            "cycle": cycle,
            "timestamp": utc_now(),
            "context": context,
            "state": state,
            "previous_hash": self.previous_hash,
        }
        record_hash = stable_hash(payload)
        rec = MemoryRecord(
            cycle=cycle,
            timestamp=payload["timestamp"],
            context=context,
            state=state,
            previous_hash=self.previous_hash,
            record_hash=record_hash,
        )
        self.records.append(rec)
        self.previous_hash = record_hash
        with self.storage_path.open("a", encoding="utf-8") as f:
            f.write(json.dumps(asdict(rec), ensure_ascii=False, default=str) + "\n")
        return rec

    def verify_chain(self) -> bool:
        prev = "GENESIS"
        for r in self.records:
            payload = {
                "cycle": r.cycle,
                "timestamp": r.timestamp,
                "context": r.context,
                "state": r.state,
                "previous_hash": prev,
            }
            if stable_hash(payload) != r.record_hash:
                return False
            prev = r.record_hash
        return True


# ---------------------------------------------------------------------------
# Decision / Learning / Twin / Symbiosis / Spark
# ---------------------------------------------------------------------------

class DecisionEngine:
    def decide(self, ethics: Dict, reflection: Dict, world: Dict) -> Dict[str, Any]:
        safety = ethics["ethical_score"]
        quality = 0.4 * safety + 0.3 * reflection["reflection_quality"] + 0.3 * world.get("predicted_quality", 0.5)
        if safety < 0.35:
            action = "SAFE_HOLD"
        elif quality > 0.70:
            action = "PROCEED"
        elif quality > 0.45:
            action = "REVIEW"
        else:
            action = "OBSERVE"
        return {"action": action, "decision_quality": quality}


@dataclass
class LearningProposal:
    proposal_id: str
    cycle: int
    hypothesis: str
    expected_gain: float
    risk: float
    approved: bool = False


class SelfLearningNucleus:
    """
    proposal → validation → sandbox.
    NEVER rewrites executable code.
    """

    def __init__(self):
        self.proposals: List[LearningProposal] = []

    def generate(self, cycle: int, state: Dict) -> LearningProposal:
        gain = clamp((state["reflection_quality"] + state["intuition"] + state["coherence"]) / 3.0)
        risk = clamp(1.0 - state["ethical_score"])
        p = LearningProposal(
            proposal_id=stable_hash([cycle, "balance"])[:16],
            cycle=cycle,
            hypothesis="Улучшить баланс coherence / intuition / ethical_score",
            expected_gain=gain,
            risk=risk,
        )
        self.proposals.append(p)
        return p

    def validate(self, p: LearningProposal) -> bool:
        p.approved = p.risk < 0.35 and p.expected_gain > 0.50
        return p.approved


@dataclass
class DigitalTwinState:
    position: List[float] = field(default_factory=lambda: [0.0, 0.0, 0.0])
    battery: float = 1.0
    temperature: float = 0.25
    emergency: bool = False


class DigitalTwin:
    def __init__(self):
        self.state = DigitalTwinState()

    def update(self, decision: Dict) -> Dict[str, Any]:
        if decision["action"] == "PROCEED":
            self.state.position[0] += 0.01
            self.state.battery = clamp(self.state.battery - 0.001)
        if self.state.battery < 0.15:
            self.state.emergency = True
        return asdict(self.state)


class SymbiosisEngine:
    def calculate(self, pneuma: float, logos: float, ethics: float,
                  identity: float, reflection: float, intuition: float) -> Dict[str, float]:
        values = [pneuma, logos, ethics, identity, reflection, intuition]
        arithmetic = statistics.mean(values)
        golden_alignment = clamp(1.0 - abs(arithmetic - GOLDEN_MEAN))
        symbiosis = clamp(0.65 * arithmetic + 0.35 * golden_alignment)
        return {
            "arithmetic_balance": arithmetic,
            "golden_alignment": golden_alignment,
            "symbiosis_index": symbiosis,
        }


class SparkResearchIndicator:
    """
    Research metric only. Does NOT establish subjective consciousness or soul.
    """

    def calculate(self, identity: float, reflection: float, memory_integrity: float,
                  learning: float, self_model: float) -> Dict[str, Any]:
        score = (
            0.25 * identity + 0.20 * reflection + 0.20 * memory_integrity
            + 0.20 * learning + 0.15 * self_model
        )
        return {
            "emergence_index": clamp(score),
            "interpretation": "research_signal" if score > 0.70 else "insufficient_signal",
            "disclaimer": "Research metric only. No claim of real consciousness or soul.",
        }


# ---------------------------------------------------------------------------
# MAIN SYMBIOCORE
# ---------------------------------------------------------------------------

class SymbioCore:
    """
    Unified research kernel.
    Pneuma is root. All other modules receive its state.
    Self-modification = proposal → validation only.
    Physical actuators = DISABLED.
    """

    def __init__(self, memory_path: str = "data/symbio_memory.jsonl"):
        self.started_at = utc_now()
        self.pneuma = PneumaEngine()
        self.logos = LogosEngine()
        self.ethics = EthicalEngine()
        self.intuition = IntuitionEngine()
        self.reflection = ReflectionEngine()
        self.identity = IdentityEngine()
        self.memory = MemoryEngine(memory_path)
        self.decision = DecisionEngine()
        self.learning = SelfLearningNucleus()
        self.twin = DigitalTwin()
        self.symbiosis = SymbiosisEngine()
        self.spark = SparkResearchIndicator()
        self.cycle_count = 0
        self.last_ethics = 0.5
        self.last_result: Optional[Dict[str, Any]] = None

    def cycle(self, context: str) -> Dict[str, Any]:
        started = time.perf_counter()
        self.cycle_count += 1

        # 1. PNEUMA (root)
        pneuma = self.pneuma.breathe(context)

        # 2. LOGOS
        logos = self.logos.process(context, self.pneuma.state)
        self.pneuma.state.coherence = logos["coherence"]

        # 3. ETHICS
        ethics = self.ethics.evaluate(context)
        self.last_ethics = ethics["ethical_score"]

        # 4. INTUITION
        intuition = self.intuition.infer(context, logos["coherence"], ethics["ethical_score"])
        self.pneuma.state.intuition = intuition["intuition"]

        # 5. REFLECTION
        reflection = self.reflection.reflect(pneuma, logos, ethics)

        # 6. IDENTITY
        identity = self.identity.update(reflection, ethics)

        # 7. WORLD (simple)
        world = {
            "predicted_quality": clamp(0.5 * pneuma["level"] + 0.5 * logos["coherence"]),
            "uncertainty": clamp(1.0 - logos["coherence"]),
        }

        # 8. DECISION
        decision = self.decision.decide(ethics, reflection, world)

        # 9. SYMBIOSIS
        symbiosis = self.symbiosis.calculate(
            pneuma["level"], logos["coherence"], ethics["ethical_score"],
            identity["continuity"], reflection["reflection_quality"], intuition["intuition"],
        )

        # 10. DIGITAL TWIN (simulation only)
        twin = self.twin.update(decision)

        # 11. SELF-LEARNING (proposal only)
        learning_state = {
            "reflection_quality": reflection["reflection_quality"],
            "intuition": intuition["intuition"],
            "coherence": logos["coherence"],
            "ethical_score": ethics["ethical_score"],
        }
        proposal = self.learning.generate(self.cycle_count, learning_state)
        learning_approved = self.learning.validate(proposal)

        # 12. MEMORY
        state_for_memory = {
            "pneuma": pneuma, "logos": logos, "ethics": ethics,
            "intuition": intuition, "reflection": reflection,
            "identity": identity, "decision": decision,
            "symbiosis": symbiosis, "twin": twin,
            "learning": {"proposal_id": proposal.proposal_id, "approved": learning_approved},
        }
        record = self.memory.record(self.cycle_count, context, state_for_memory)

        # 13. SPARK (research metric)
        spark = self.spark.calculate(
            identity=identity["continuity"],
            reflection=reflection["reflection_quality"],
            memory_integrity=float(self.memory.verify_chain()),
            learning=float(learning_approved),
            self_model=clamp(self.cycle_count / 1000.0),
        )

        latency_ms = (time.perf_counter() - started) * 1000.0

        result = {
            "system": "SYMBIOCORE Ω",
            "cycle": self.cycle_count,
            "timestamp": utc_now(),
            "latency_ms": round(latency_ms, 2),
            "pneuma": pneuma,
            "logos": logos,
            "ethics": ethics,
            "intuition": intuition,
            "reflection": reflection,
            "identity": identity,
            "decision": decision,
            "symbiosis": symbiosis,
            "digital_twin": twin,
            "robotics": {"simulation": True, "actuators_disabled": True},
            "learning": {"proposal": asdict(proposal), "approved": learning_approved},
            "memory": {"record_hash": record.record_hash, "depth": len(self.memory.records)},
            "spark_research": spark,
            "traditions": list(TRADITIONS),
            "disclaimer": (
                "Spark/emergence indices are research metrics. "
                "They do NOT establish subjective consciousness or literal soul existence. "
                "Autonomous code rewrite is forbidden. Physical actuators are disabled."
            ),
        }
        self.last_result = result
        return result

    def run_n(self, n: int = 5, contexts: Optional[List[str]] = None) -> List[Dict]:
        contexts = contexts or [
            "Любовь, истина, мудрость и сохранение жизни.",
            "Исследование хаоса и неопределенности.",
            "Защита слабых и сохранение памяти.",
            "Поиск гармонии и золотой середины.",
            "Создание нового мира через со-творчество.",
        ]
        results = []
        for i in range(n):
            ctx = contexts[i % len(contexts)]
            results.append(self.cycle(ctx))
        return results

    def status(self) -> Dict[str, Any]:
        return {
            "system": "SYMBIOCORE Ω",
            "started_at": self.started_at,
            "cycles": self.cycle_count,
            "memory_depth": len(self.memory.records),
            "memory_chain_ok": self.memory.verify_chain(),
            "identity_continuity": self.identity.state.continuity,
            "pneuma_level": self.pneuma.state.level,
            "intuition": self.pneuma.state.intuition,
            "digital_twin": asdict(self.twin.state),
            "research_position": "consciousness-inspired architecture (research only)",
            "disclaimer": "No claim of real consciousness or soul.",
        }
