from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from typing import Dict, Iterable

from . import entity

class AlignmentId(Enum):
    NONE = 0
    GOOD = 1
    EVIL = 2
    NEUTRAL = 3
    ORDER = 4
    CHAOS = 5
    BALANCE = 6


class AlignmentType(Enum):
    NONE = 0
    PRIMARY = 1
    SECONDARY = 2


@dataclass(frozen=True)
class Alignment(entity.Entity):
    id_: AlignmentId
    type_: AlignmentType

    @property
    def name(self) -> str:
        return self.id_.name.title()

    @property
    def is_primary(self) -> bool:
        """True if this is a primary alignment"""
        return self.type_ == AlignmentType.PRIMARY

    @property
    def is_secondary(self) -> bool:
        """True if this is a secondary alignment"""
        return self.type_ == AlignmentType.SECONDARY


def _register(alignment: Alignment) -> Alignment:
    if alignment.id_ in _ALIGNMENTS:
        raise ValueError(f'Duplicate alignment registration: {alignment.name}')

    _ALIGNMENTS[alignment.id_] = alignment
    return alignment


def all() -> Iterable[Alignment]:
    return _ALIGNMENTS.values()


def get(id_: AlignmentId) -> Alignment:
    return _ALIGNMENTS[id_]


_ALIGNMENTS: Dict[AlignmentId, Alignment] = {}

NONE = _register(Alignment(AlignmentId.NONE, AlignmentType.NONE))
GOOD = _register(Alignment(AlignmentId.GOOD, AlignmentType.PRIMARY))
EVIL = _register(Alignment(AlignmentId.EVIL, AlignmentType.PRIMARY))
NEUTRAL = _register(Alignment(AlignmentId.NEUTRAL, AlignmentType.PRIMARY))
ORDER = _register(Alignment(AlignmentId.ORDER, AlignmentType.SECONDARY))
CHAOS = _register(Alignment(AlignmentId.CHAOS, AlignmentType.SECONDARY))
BALANCE = _register(Alignment(AlignmentId.BALANCE, AlignmentType.SECONDARY))
