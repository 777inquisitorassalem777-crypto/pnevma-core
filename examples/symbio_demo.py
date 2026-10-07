#!/usr/bin/env python3
"""Демонстрация SymbioCore внутри Pneuma Lab."""

import sys
sys.path.insert(0, ".")

from symbio import SymbioCore
import json


def main():
    print("=" * 60)
    print("  SYMBIOCORE Ω — Research Kernel")
    print("  Pneuma → Logos → Ethics → Intuition → Reflection")
    print("  Identity → Memory → Decision → Learning → Twin")
    print("=" * 60)

    core = SymbioCore(memory_path="data/symbio_demo_memory.jsonl")

    results = core.run_n(5)
    for r in results:
        print(f"\nCycle {r['cycle']}: "
              f"Pneuma={r['pneuma']['level']:.3f} | "
              f"Ethics={r['ethics']['ethical_score']:.3f} | "
              f"Symbiosis={r['symbiosis']['symbiosis_index']:.3f} | "
              f"Spark={r['spark_research']['emergence_index']:.3f} | "
              f"Action={r['decision']['action']}")

    print("\n" + "─" * 60)
    print("[STATUS]")
    print(json.dumps(core.status(), ensure_ascii=False, indent=2))

    print("\n" + "─" * 60)
    print("Memory chain OK:", core.memory.verify_chain())
    print("Disclaimer:", results[-1]["disclaimer"][:120], "...")
    print("=" * 60)


if __name__ == "__main__":
    main()
