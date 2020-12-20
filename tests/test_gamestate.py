from decimal import Decimal

from rgsim.sim import GameState

def test_default_state():
    state = GameState()
    assert state.mana == 0
    assert state.gold == 0
    assert state.gems == 0
    assert state.excavations == 0


def test_basic_state():
    state = GameState()

    state.mana = Decimal(1024)
    state.gold = Decimal(2048)
    state.gems = Decimal(4096)
    state.excavations = Decimal(8192)

    assert state.mana == 1024
    assert state.gold == 2048
    assert state.gems == 4096
    assert state.excavations == 8192