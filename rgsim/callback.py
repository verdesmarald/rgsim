from __future__ import annotations

from decimal import Decimal
from typing import Any, Protocol, TYPE_CHECKING

if TYPE_CHECKING:
    from . import simulator

class Amount(Protocol):
    """Calculate an amount based on game state and target entity"""
    def __call__(self, state: simulator.GameState, target: Any, /) -> Decimal: ...


class Filter(Protocol):
    """Check if effect is applicable to target based on game state"""
    def __call__(self, state: simulator.GameState, target: Any, /) -> bool: ...