#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pnevma import PnevmaCore


def main():
    print("=" * 60)
    print("  PNEVMA-CORE Ω  |  Unified Research Symbiosis")
    print("=" * 60)

    core = PnevmaCore()
    core.ignite()

    print("\n[EVOLUTION] 8 cycles...")
    for _ in range(8):
        r = core.cycle("life_multiplication + compassionate novelty")
        print(f"  cycle={r['cycle']:03d}  accepted={r['accepted']}  "
              f"dharma={r.get('dharma', '—')}  paradigms={r.get('paradigms_total', 0)}")

    print("\n[SAFETY] harmful intent...")
    print(" ", core.evaluate_intent({"causes_harm": True, "action": "destroy"}))

    print("\n[STATUS]")
    for k, v in core.status().items():
        print(f"  {k}: {v}")
    print("=" * 60)


if __name__ == "__main__":
    main()
