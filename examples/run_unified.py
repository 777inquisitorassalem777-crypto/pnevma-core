#!/usr/bin/env python3
"""Full unified demo: core cycle + optional Slavic layer."""
import sys, os, json
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pnevma import PnevmaCore


def main():
    print("=" * 64)
    print("  PNEVMA-CORE Ω  |  UNIFIED SYMBIOSIS DEMO")
    print("=" * 64)

    core = PnevmaCore()
    core.ignite()

    print("\n--- Evolution cycles ---")
    for _ in range(5):
        r = core.cycle("life_multiplication")
        print(f"  cycle {r['cycle']}: accepted={r['accepted']} paradigms={r.get('paradigms_total')}")

    print("\n--- Safety check ---")
    print(" ", core.evaluate_intent({"causes_harm": True}))

    if core.slavic_analyzer:
        print("\n--- Slavic dual-level (volkhv) ---")
        v = core.slavic_analyze("volkhv")
        print(json.dumps({
            "lexeme": v.get("lexeme"),
            "period": v.get("level_1_historical_linguistic", {}).get("period"),
            "formula": v.get("level_2_semantic_interpretation", {}).get("formula"),
        }, ensure_ascii=False, indent=2))

        print("\n--- Slavic cognitive pipeline ---")
        p = core.slavic_process("ведун и волхв как знание и слово")
        for role, data in p.get("pipeline", {}).items():
            print(f"  {data.get('role')}: {data.get('motto')}")

    print("\n--- Status ---")
    for k, v in core.status().items():
        print(f"  {k}: {v}")
    print("=" * 64)


if __name__ == "__main__":
    main()
