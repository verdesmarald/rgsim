"""Building definitions and functionality"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from enum import Enum, unique
from typing import Dict, Iterable, Optional

from . import alignment, entity


@unique
class BuildingId(Enum):
    """Id for building (matches ids from RG)"""
    FARM = 9
    INN = 13
    BLACKSMITH = 3
    DEEP_MINE = 7
    STONE_PILLARS = 22
    ALCHEMIST_LAB = 1
    MONASTERY = 17
    LABYRINTH = 16
    IRON_STRONGHOLD = 14
    ANCIENT_PYRAMID = 2
    WARRIOR_BARRACKS = 23
    KNIGHTS_JOUST = 15
    WIZARD_TOWER = 25
    CATHEDRAL = 4
    CITADEL = 5
    ROYAL_CASTLE = 20
    HEAVENS_GATE = 11
    SLAVE_PEN = 21
    ORCISH_ARENA = 19
    WITCH_CONCLAVE = 24
    DARK_TEMPLE = 6
    NECROPOLIS = 18
    EVIL_FORTRESS = 8
    HELL_PORTAL = 12
    HALL_OF_LEGENDS = 10


@dataclass(frozen=True)
class Building(entity.Entity):
    id_: BuildingId
    tier: Decimal
    alignment: alignment.Alignment
    base_production: Decimal
    base_price: Decimal

    _name_override: Optional[str] = None

    @property
    def name(self) -> str:
        if self._name_override is not None:
            return self._name_override

        return self.id_.name.replace('_', ' ').title()


def _register(building: Building) -> Building:
    if building.id_ in _BUILDINGS:
        raise ValueError(f'Duplicate building registration: {building.name}')

    _BUILDINGS[building.id_] = building
    return building


def get(id_: BuildingId) -> Building:
    return _BUILDINGS[id_]


def all() -> Iterable[Building]:
    return _BUILDINGS.values()


_BUILDINGS: Dict[BuildingId, Building] = {}

FARM = _register(Building(
    BuildingId.FARM, Decimal(1), alignment.NONE, Decimal(2), Decimal(10)
))
INN = _register(Building(
    BuildingId.INN, Decimal(2), alignment.NONE, Decimal(6), Decimal(125)
))
BLACKSMITH = _register(Building(
    BuildingId.BLACKSMITH, Decimal(3), alignment.NONE, Decimal(20), Decimal(600)
))
DEEP_MINE = _register(Building(
    BuildingId.DEEP_MINE, Decimal(4), alignment.NEUTRAL, Decimal(65), Decimal(1800)
))
STONE_PILLARS = _register(Building(
    BuildingId.STONE_PILLARS, Decimal(5), alignment.NEUTRAL, Decimal(200), Decimal(5600)
))
ALCHEMIST_LAB = _register(Building(
    BuildingId.ALCHEMIST_LAB, Decimal(6), alignment.NEUTRAL, Decimal(650), Decimal(38000)
))
MONASTERY = _register(Building(
    BuildingId.MONASTERY, Decimal(7), alignment.NEUTRAL, Decimal(2000), Decimal(442000)
))
LABYRINTH = _register(Building(
    BuildingId.LABYRINTH, Decimal(8), alignment.NEUTRAL, Decimal(8500), Decimal(7.3e6)
))
IRON_STRONGHOLD = _register(Building(
    BuildingId.IRON_STRONGHOLD, Decimal(9), alignment.NEUTRAL, Decimal(1e5), Decimal(145e6)
))
ANCIENT_PYRAMID = _register(Building(
    BuildingId.ANCIENT_PYRAMID, Decimal(10), alignment.NEUTRAL, Decimal(1.2e6), Decimal(3.2e9)
))
WARRIOR_BARRACKS = _register(Building(
    BuildingId.WARRIOR_BARRACKS, Decimal(4), alignment.GOOD, Decimal(65), Decimal(1800)
))
KNIGHTS_JOUST = _register(Building(
    BuildingId.KNIGHTS_JOUST, Decimal(5), alignment.GOOD, Decimal(200), Decimal(5600),
    _name_override='Knight\'s Joust'
))
WIZARD_TOWER = _register(Building(
    BuildingId.WIZARD_TOWER, Decimal(6), alignment.GOOD, Decimal(650), Decimal(38000)
))
CATHEDRAL = _register(Building(
    BuildingId.CATHEDRAL, Decimal(7), alignment.GOOD, Decimal(2000), Decimal(442000)
))
CITADEL = _register(Building(
    BuildingId.CITADEL, Decimal(8), alignment.GOOD, Decimal(8500), Decimal(7.3e6)
))
ROYAL_CASTLE = _register(Building(
    BuildingId.ROYAL_CASTLE, Decimal(9), alignment.GOOD, Decimal(100000), Decimal(145e6)
))
HEAVENS_GATE = _register(Building(
    BuildingId.HEAVENS_GATE, Decimal(10), alignment.GOOD, Decimal(1.2e6), Decimal(3.2e9),
    _name_override='Heaven\'s Gate'
))
SLAVE_PEN = _register(Building(
    BuildingId.SLAVE_PEN, Decimal(4), alignment.EVIL, Decimal(65), Decimal(1800)
))
ORCISH_ARENA = _register(Building(
    BuildingId.ORCISH_ARENA, Decimal(5), alignment.EVIL, Decimal(200), Decimal(5600)
))
WITCH_CONCLAVE = _register(Building(
    BuildingId.WITCH_CONCLAVE, Decimal(6), alignment.EVIL, Decimal(650), Decimal(38000)
))
DARK_TEMPLE = _register(Building(
    BuildingId.DARK_TEMPLE, Decimal(7), alignment.EVIL, Decimal(2000), Decimal(442000)
))
NECROPOLIS = _register(Building(
    BuildingId.NECROPOLIS, Decimal(8), alignment.EVIL, Decimal(8500), Decimal(7.3e6)
))
EVIL_FORTRESS = _register(Building(
    BuildingId.EVIL_FORTRESS, Decimal(9), alignment.EVIL, Decimal(100000), Decimal(145e6)
))
HELL_PORTAL = _register(Building(
    BuildingId.HELL_PORTAL, Decimal(10), alignment.EVIL, Decimal(1.2e6), Decimal(3.2e9)
))
HALL_OF_LEGENDS = _register(Building(
    BuildingId.HALL_OF_LEGENDS, Decimal(11), alignment.NONE, Decimal(250000), Decimal(2e11),
    _name_override='Hall of Legends'
))
