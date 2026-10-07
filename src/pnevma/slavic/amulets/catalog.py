"""
Slavic amulets / обереги — research catalog.
Status: FACT | HYPOTHESIS | RECONSTRUCTION | LATER_NEO
"""

from __future__ import annotations
from enum import Enum
from typing import Any, Dict, List


class AmuletStatus(str, Enum):
    FACT = "fact"
    HYPOTHESIS = "hypothesis"
    RECONSTRUCTION = "reconstruction"
    LATER_NEO = "later_neo"


AMULETS: Dict[str, Dict[str, Any]] = {
    "solar_rosette_amulet": {
        "name_ru": "Солярная розетка (амулет)",
        "status": AmuletStatus.FACT,
        "form": "круг с крестом или лучами, часто на пряслицах и подвесках",
        "function": ["защита", "связь с солнцем", "плодородие"],
        "materials_historical": ["металл", "кость", "глина"],
        "note": "Один из самых частых солярных знаков в археологии Восточной Европы.",
    },
    "axe_of_perun": {
        "name_ru": "Топорик Перуна / секира-амулет",
        "status": AmuletStatus.HYPOTHESIS,
        "form": "миниатюрный топор или секира",
        "function": ["воинская защита", "громовая сила", "клятва"],
        "materials_historical": ["бронза", "железо"],
        "note": "Находки миниатюрных топориков интерпретируются сравнительно-мифологически.",
    },
    "lunnitsa": {
        "name_ru": "Лунница",
        "status": AmuletStatus.FACT,
        "form": "подвеска в форме полумесяца",
        "function": ["женский оберег", "плодородие", "защита"],
        "materials_historical": ["серебро", "бронза"],
        "note": "Широко представлена в древнерусских кладах и погребениях.",
    },
    "komok_svyatoy": {
        "name_ru": "Комок / узелок с травами или землёй",
        "status": AmuletStatus.FACT,
        "form": "тканевый узелок",
        "function": ["защита в пути", "лечение", "связь с домом"],
        "note": "Этнографически засвидетельствован; содержимое варьировалось.",
    },
    "red_thread": {
        "name_ru": "Красная нить / поясок",
        "status": AmuletStatus.FACT,
        "form": "красная шерстяная или льняная нить на запястье / пояс",
        "function": ["защита от сглаза", "жизненная сила"],
        "note": "Очень устойчивый народный обычай; красный цвет — апотропеический.",
    },
    "horse_shoe": {
        "name_ru": "Подкова",
        "status": AmuletStatus.FACT,
        "form": "железная подкова над входом",
        "function": ["защита дома", "удача"],
        "note": "Поздний, но устойчивый славянский и общеевропейский оберег.",
    },
    "bereginya_doll": {
        "name_ru": "Кукла-берегиня / стрижка",
        "status": AmuletStatus.FACT,
        "form": "тряпичная кукла без лица или с условным лицом",
        "function": ["защита детей и дома", "плодородие"],
        "note": "Этнографически широко известна; лицо часто не прорисовывали.",
    },
    "kolovrat_modern": {
        "name_ru": "Коловрат (современный оберег)",
        "status": AmuletStatus.LATER_NEO,
        "form": "восьмилучевая свастика",
        "function": ["солярный цикл", "сила"],
        "note": "Преимущественно неоязыческий символ XX–XXI вв.",
    },
}


def get_amulet(key: str) -> Dict[str, Any]:
    return AMULETS.get(key, {})


def list_amulets() -> List[str]:
    return list(AMULETS.keys())
