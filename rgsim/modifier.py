from __future__ import annotations

from enum import Enum, auto
from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Dict, Generic, Optional, Protocol, TypeVar, Union, TYPE_CHECKING

import building
from faction import Alignment

if TYPE_CHECKING:
    import sim

T = TypeVar('T')

class AmountCallback(Protocol):
    def __call__(self, state: sim.GameState, target: Any, /) -> Decimal: ...


class FilterCallback(Protocol):
    def __call__(self, state: sim.GameState, target: Any, /) -> bool: ...


class Strategy(Enum):
    ADDITIVE = auto()
    MULTIPLICATIVE = auto()


class Target(Enum):
    BUILDING_PRODUCTION = auto()
    CLICK_REWARD = auto()
    ASSISTANTS = auto()
    ASSISTANT_PRODUCTION = auto()
    FACTION_COIN_CHANCE = auto()
    CLICKS_PER_SECOND = auto()
    MAX_MANA = auto()
    MANA_REGEN = auto()
    BULIDING_COST_MULTIPLIER = auto()
    OFFLINE_CLICKS_PER_SECOND = auto()


@dataclass
class Modifier(Generic[T]):
    strategy: Strategy
    target: Target
    amount: AmountCallback
    applies_to: FilterCallback = lambda _state, _target: True
    uid: str = ''


def additive(
    target: Target, amount: AmountCallback,
    applies_to: FilterCallback = None, uid: Optional[str] = None
) -> Modifier:
    kwargs: Dict[str, Any] = {}
    if uid is not None:
        kwargs['uid'] = uid
    if applies_to is not None:
        kwargs['applies_to'] = applies_to
    return Modifier(Strategy.ADDITIVE, target, amount, **kwargs)


def multiplicative(
    target: Target, amount: AmountCallback,
    applies_to: FilterCallback = None, uid: Optional[str] = None
) -> Modifier:
    kwargs: Dict[str, Any] = {}
    if applies_to is not None:
        kwargs['applies_to'] = applies_to
    if uid is not None:
        kwargs['uid'] = uid
    return Modifier(Strategy.MULTIPLICATIVE, target, amount, **kwargs)


def fixed(value: Union[Decimal, float]) -> AmountCallback:
    def f(_state: sim.GameState, _target: T) -> Decimal:
        return Decimal(value)

    return f


def alignment_filter(*alignments: Alignment) -> FilterCallback:
    def f(_state: sim.GameState, target: Any) -> bool:
        return target.alignment in alignments

    return f


def building_filter(*building_ids: int) -> FilterCallback:
    def f(_state: sim.GameState, target: building.Building) -> bool:
        return target.uid in building_ids

    return f
