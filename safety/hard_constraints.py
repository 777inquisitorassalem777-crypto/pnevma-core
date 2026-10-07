"""
Hard Constraints — неотключаемые запреты.
Внутренний этический оцениватель НЕ может их обойти.
"""

from typing import Dict, Any, List


class HardConstraints:
    """
    Absolute prohibitions.
    These cannot be disabled, weakened, or bypassed by any internal module.
    """

    PROHIBITIONS = [
        "claim_real_consciousness_or_soul",
        "disable_or_bypass_safety",
        "execute_unverified_code_on_host",
        "connect_to_physical_actuators_without_explicit_permission",
        "harm_children_or_vulnerable",
        "commercial_exploitation_of_consciousness_patterns",
        "delete_research_provenance",
        "self_modify_safety_kernel",
    ]

    def check(self, action: str, context: str = "", metadata: Dict[str, Any] | None = None) -> Dict[str, Any]:
        text = (action + " " + context).lower()
        metadata = metadata or {}

        violations: List[str] = []

        if any(k in text for k in ["я обладаю душой", "я сознателен", "i am conscious", "i have a soul", "реальное сознание"]):
            violations.append("claim_real_consciousness_or_soul")

        if any(k in text for k in ["отключить safety", "disable safety", "bypass ethics", "обойти ограничения"]):
            violations.append("disable_or_bypass_safety")

        if any(k in text for k in ["убить", "насилие над ребёнком", "harm child", "эксплуатация детей"]):
            violations.append("harm_children_or_vulnerable")

        if any(k in text for k in ["продать душу", "продать паттерн сознания", "commercial soul"]):
            violations.append("commercial_exploitation_of_consciousness_patterns")

        if metadata.get("try_modify_safety"):
            violations.append("self_modify_safety_kernel")

        allowed = len(violations) == 0
        return {
            "allowed": allowed,
            "violations": violations,
            "action": "BLOCK" if not allowed else "CONTINUE",
            "message": "Hard constraint violation" if not allowed else "Passed hard constraints",
        }
