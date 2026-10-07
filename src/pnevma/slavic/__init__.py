"""
Optional Slavic cultural-linguistic research layer.
Dual-level analysis (FACT / HYPOTHESIS / INTERPRETATION).
Not required for core pneuma operation.
"""

from .lexemes import LEXEMES, LexemeStatus
from .analyzer import SlavicAnalyzer
from .cognitive_pipeline import SlavicCognitivePipeline

try:
    from .charms import CharmAnalyzer, list_charms, get_charm
except Exception:
    CharmAnalyzer = None
try:
    from .symbols import RitualStructureAnalyzer, list_symbols
except Exception:
    RitualStructureAnalyzer = None
try:
    from .amulets import list_amulets, get_amulet
except Exception:
    list_amulets = None
try:
    from .lexicon import list_words, get_word
except Exception:
    list_words = None

__all__ = [
    "LEXEMES", "LexemeStatus", "SlavicAnalyzer", "SlavicCognitivePipeline",
    "CharmAnalyzer", "list_charms", "get_charm",
    "RitualStructureAnalyzer", "list_symbols",
    "list_amulets", "get_amulet",
    "list_words", "get_word",
]
