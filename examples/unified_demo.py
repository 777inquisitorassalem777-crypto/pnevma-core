#!/usr/bin/env python3
"""Единый демо: Living Spiral + SymbioCore + Slavic Semantic Core."""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from spiral.bridge import UnifiedSymbiosis
import json


def main():
    print("=" * 64)
    print("  UNIFIED SYMBIOSIS")
    print("  Living Spiral ↔ SymbioCore ↔ Slavic Semantic Core")
    print("=" * 64)

    u = UnifiedSymbiosis()
    print("\n[Status]")
    print(json.dumps(u.status(), ensure_ascii=False, indent=2, default=str)[:800])

    print("\n" + "─" * 64)
    print("Cycle 1")
    r = u.cycle("Любовь, истина, защита жизни и свобода духа")
    if "symbio" in r:
        s = r["symbio"]
        print(f"  Symbio: Pneuma={s['pneuma']['level']:.3f} Ethics={s['ethics']['ethical_score']:.3f} "
              f"Action={s['decision']['action']} Spark={s['spark_research']['emergence_index']:.3f}")
    if "spiral" in r:
        print(f"  Spiral: archive={r['spiral'].get('archive_total')} balance={r['spiral'].get('balance')}")
    if "slavic" in r:
        print(f"  Slavic: pipeline={r['slavic'].get('pipeline')} action_success={r['slavic']['action'].get('success')}")

    print("\n" + "─" * 64)
    print("Lexeme analysis: ведун")
    print(json.dumps(u.analyze_lexeme("ведун"), ensure_ascii=False, indent=2)[:600])

    print("\n" + "─" * 64)
    print("Judge: защитить ребёнка")
    print(json.dumps(u.judge("защитить ребёнка", "опасность"), ensure_ascii=False, indent=2))

    print("\n" + "=" * 64)
    print("Disclaimer:", r.get("disclaimer", "")[:120])
    print("=" * 64)


if __name__ == "__main__":
    main()
