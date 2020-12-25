from __future__ import annotations

from dataclasses import dataclass
from enum import Enum, unique
from typing import Dict, Iterable

from . import alignment, entity


@unique
class FactionId(Enum):
    NONE = -1
    FAIRY = 0
    ELF = 1
    ANGEL = 2
    GOBLIN = 3
    UNDEAD = 4
    DEMON = 5
    TITAN = 6
    DRUID = 7
    FACELESS = 8
    DWARF = 9
    DROW = 10
    MERCENARY = 11
    DRAGON = 12
    ARCHON = 13
    DJINN = 14
    MAKERS = 15


@unique
class FactionType(Enum):
    NONE = 0
    BASE = 1
    PRESTIGE = 2
    ELITE = 3


@dataclass(frozen=True)
class Faction(entity.Entity):
    id_: FactionId
    type_: FactionType
    alignment: alignment.Alignment

    @property
    def name(self) -> str:
        return self.id_.name.title()

    @property
    def is_base(self) -> bool:
        return self.type_ == FactionType.BASE

    @property
    def is_prestige(self) -> bool:
        return self.type_ == FactionType.PRESTIGE

    @property
    def is_elite(self) -> bool:
        return self.type_ == FactionType.ELITE


def _register(faction: Faction) -> Faction:
    if faction.id_ in _FACTIONS:
        raise ValueError(f'Duplicate faction registration: {faction.name}')

    _FACTIONS[faction.id_] = faction
    return faction


def all() -> Iterable[Faction]:
    return _FACTIONS.values()


def get(id_: FactionId) -> Faction:
    return _FACTIONS[id_]


_FACTIONS: Dict[FactionId, Faction] = {}

NONE = _register(Faction(FactionId.NONE, FactionType.NONE, alignment.NONE))

# Base Factions
FAIRY = _register(Faction(FactionId.FAIRY, FactionType.BASE, alignment.GOOD))
ELF = _register(Faction(FactionId.ELF, FactionType.BASE, alignment.GOOD))
ANGEL = _register(Faction(FactionId.ANGEL, FactionType.BASE, alignment.GOOD))
GOBLIN = _register(Faction(FactionId.GOBLIN, FactionType.BASE, alignment.EVIL))
UNDEAD = _register(Faction(FactionId.UNDEAD, FactionType.BASE, alignment.EVIL))
DEMON = _register(Faction(FactionId.DEMON, FactionType.BASE, alignment.EVIL))
TITAN = _register(Faction(FactionId.TITAN, FactionType.BASE, alignment.NEUTRAL))
DRUID = _register(Faction(FactionId.DRUID, FactionType.BASE, alignment.NEUTRAL))
FACELESS = _register(Faction(FactionId.FACELESS, FactionType.BASE, alignment.NEUTRAL))
MERCENARY = _register(Faction(FactionId.MERCENARY, FactionType.BASE, alignment.NONE))

# Prestige Factions
DWARF = _register(Faction(FactionId.DWARF, FactionType.PRESTIGE, alignment.GOOD))
DROW = _register(Faction(FactionId.DROW, FactionType.PRESTIGE, alignment.EVIL))
DRAGON = _register(Faction(FactionId.DRAGON, FactionType.PRESTIGE, alignment.NEUTRAL))

# Elite Factions
ARCHON = _register(Faction(FactionId.ARCHON, FactionType.ELITE, alignment.ORDER))
DJINN = _register(Faction(FactionId.DJINN, FactionType.ELITE, alignment.CHAOS))
MAKERS = _register(Faction(FactionId.MAKERS, FactionType.ELITE, alignment.BALANCE))
