from __future__ import annotations

from enum import Enum, auto, unique
from dataclasses import dataclass
from decimal import Decimal
from typing import Any, Dict, Optional, Union, TYPE_CHECKING

from . import entity

if TYPE_CHECKING:
    from .. import callback, simulator


@unique
class Strategy(Enum):
    ADDITIVE = auto()
    MULTIPLICATIVE = auto()


@unique
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


@dataclass(frozen=True)
class Modifier(entity.Entity):
    strategy: Strategy
    target: Target
    amount: callback.Amount
    applies_to: callback.Filter = lambda _state, _target: True
    owner: Optional[entity.Entity] = None

    @property
    def name(self) -> str:
        raise NotImplementedError


def additive(
        target: Target, amount: callback.Amount,
        applies_to: callback.Filter = None, id_: Optional[str] = None) -> Modifier:
    kwargs: Dict[str, Any] = {}
    if id_ is not None:
        kwargs['id_'] = id_
    if applies_to is not None:
        kwargs['applies_to'] = applies_to
    return Modifier(Strategy.ADDITIVE, target, amount, **kwargs)


def multiplicative(
        target: Target, amount: callback.Amount,
        applies_to: callback.Filter = None, id_: Optional[str] = None) -> Modifier:
    kwargs: Dict[str, Any] = {}
    if applies_to is not None:
        kwargs['applies_to'] = applies_to
    if id_ is not None:
        kwargs['id_'] = id_
    return Modifier(Strategy.MULTIPLICATIVE, target, amount, **kwargs)


def fixed(value: Union[Decimal, float]) -> callback.Amount:
    """Define an amount callback that always returns a fixed value"""
    def _(_state: simulator.GameState, _target: Any) -> Decimal:
        return Decimal(value)

    return _
