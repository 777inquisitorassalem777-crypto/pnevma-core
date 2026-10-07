#!/usr/bin/env python3
"""Демонстрация славянского семантического ядра внутри Pneuma Lab."""

import sys
sys.path.insert(0, ".")

from slavic import SlavicCognitiveAgent
import json


def main():
    print("=" * 60)
    print("  СЛАВЯНСКИЙ СЕМАНТИЧЕСКИЙ АТЛАС")
    print("  Ведун → Волхв → Вещун → Характерник")
    print("=" * 60)

    agent = SlavicCognitiveAgent()

    print("\n[Статус]")
    print(json.dumps(agent.status(), ensure_ascii=False, indent=2))

    print("\n" + "─" * 60)
    print("Разбор лексемы «волхв»")
    print(json.dumps(agent.analyze_lexeme("волхв"), ensure_ascii=False, indent=2))

    print("\n" + "─" * 60)
    print("Разбор лексемы «ведун»")
    print(json.dumps(agent.analyze_lexeme("ведун"), ensure_ascii=False, indent=2))

    print("\n" + "─" * 60)
    print("Разбор лексемы «характерник»")
    print(json.dumps(agent.analyze_lexeme("характерник"), ensure_ascii=False, indent=2))

    print("\n" + "─" * 60)
    print("Полный цикл: наблюдение → действие")
    result = agent.perceive_and_act(
        observation="человек страдает от болезни",
        goal="понять и предложить модель помощи",
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))

    print("\n" + "=" * 60)
    print("Симбиоз с Pneuma Lab готов.")
    print("Историко-лингвистический уровень ≠ смысловая интерпретация.")
    print("=" * 60)


if __name__ == "__main__":
    main()
