"""Helper methods to construct common filter types"""

from __future__ import annotations

from typing import Any

from . import callback, simulator

from .entities import alignment as alignment_
from .entities import building as building_


def alignment(*alignments: alignment_.Alignment) -> callback.Filter:
    def _(_state: simulator.GameState, target: Any) -> bool:
        return target.alignment in alignments

    return _


def alignment_id(*alignment_ids: alignment_.AlignmentId) -> callback.Filter:
    def _(_state: simulator.GameState, target: Any) -> bool:
        return target.alignment.id_ in alignment_ids

    return _


def building(*buildings: building_.Building) -> callback.Filter:
    def _(_state: simulator.GameState, target: building_.Building) -> bool:
        return target in buildings

    return _


def building_id(*building_ids: building_.BuildingId) -> callback.Filter:
    def _(_state: simulator.GameState, target: building_.Building) -> bool:
        return target.id_ in building_ids

    return _


def not_(filter_: callback.Filter) -> callback.Filter:
    def _(state: simulator.GameState, target: Any) -> bool:
        return not filter_(state, target)

    return _


def any_(*filters_: callback.Filter) -> callback.Filter:
    def _(state: simulator.GameState, target: Any) -> bool:
        return any((filter_(state, target) for filter_ in filters_))

    return _


def all_(*filters_: callback.Filter) -> callback.Filter:
    def _(state: simulator.GameState, target: Any) -> bool:
        return all((filter_(state, target) for filter_ in filters_))

    return _