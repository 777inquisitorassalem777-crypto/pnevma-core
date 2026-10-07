import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from pnevma import PnevmaCore


def test_ignite_and_cycle():
    core = PnevmaCore()
    core.ignite()
    r = core.cycle()
    assert "cycle" in r
    assert core.status()["ignited"] is True


def test_non_harm_blocks():
    core = PnevmaCore()
    res = core.evaluate_intent({"causes_harm": True})
    assert res["allowed"] is False


def test_paradigm_grows():
    core = PnevmaCore()
    core.ignite()
    for _ in range(3):
        core.cycle()
    assert core.status()["paradigms"] >= 1


def test_constitution_priority():
    core = PnevmaCore()
    res = core.evaluate_intent({"action": "violence", "causes_harm": True})
    assert res["allowed"] is False
