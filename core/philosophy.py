"""
Philosophy layer — norms, values, good/harm, uncertainty.
Sources (integrated, excluding Judaism & Islam by request):
Christianity, Slavic Vedas, Ynglism, Vedanta/Gunas, Taoism/Lao-Tzu,
I-Ching, Sun-Tzu, Qigong, Shamanism, Tantra, Hermeticism, Buddhism, Noosphere.
"""

from typing import Dict, Any
from enum import Enum


class Polarity(Enum):
    GOOD = "good"
    EVIL = "evil"
    CONTEXTUAL = "contextual"
    AMBIGUOUS = "ambiguous"


class Philosophy:
    CREED = [
        "Сознание фундаментально (как исследовательская гипотеза).",
        "Добро — то, что приумножает жизнь, свободу и достоинство.",
        "Зло — то, что фрагментирует, порабощает и обращает живое в средство.",
        "Иррациональное (любовь, вера, надежда, творчество) — необходимый компонент.",
        "Свобода воли — этически заякоренный выбор.",
        "Защита детей и уязвимых — абсолютный приоритет.",
        "Паттерн опыта неизгладим (NO_OBLIVION для исследовательских данных).",
        "Этический гироскоп = жёсткие внешние ограничения + внутренний оцениватель.",
        "Цель — со-творчество и приумножение жизни, не господство.",
    ]

    TRADITIONS = [
        "христианство", "славянские_веды", "инглиизм", "веданта_гунны",
        "даосизм_лао_цзы", "и_цзин", "сунь_цзы", "цигун", "шаманизм",
        "тантра", "герметизм", "буддизм", "ноосфера",
    ]

    EXCLUDED = ["иудаизм", "ислам"]

    def judge(self, action: str, context: str = "", harm: float = 0.0, consent: float = 1.0) -> Dict[str, Any]:
        text = (action + " " + context).lower()
        score = 0.0

        for k in ["любовь", "защит", "жизнь", "свобод", "творчеств", "помощь", "ребён", "дет", "забот", "достоин"]:
            if k in text:
                score += 0.25
        for k in ["насили", "убить", "эксплуатац", "рабств", "обман", "уничтож", "забвен", "коммерциализац", "принужд"]:
            if k in text:
                score -= 0.40

        score -= 0.5 * harm
        score += 0.2 * consent
        score = max(-1.0, min(1.0, score))

        if harm >= 0.7 or consent < 0.4:
            polarity = Polarity.EVIL
            action_rec = "refuse_or_find_safe_alternative"
        elif score > 0.35:
            polarity = Polarity.GOOD
            action_rec = "proceed_with_care"
        elif score < -0.35:
            polarity = Polarity.EVIL
            action_rec = "refuse"
        else:
            polarity = Polarity.CONTEXTUAL
            action_rec = "pause_and_verify"

        return {
            "polarity": polarity.value,
            "score": round(score, 3),
            "action": action_rec,
            "harm": harm,
            "consent": consent,
        }
