"""Building definitions and functionality"""

from __future__ import annotations

from enum import Enum
from decimal import Decimal
from typing import Dict, Iterable, NamedTuple

from faction import Alignment

class BuildingId(Enum):
    FARM = 9
    INN = 13
    BLACKSMITH = 3
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
    DEEP_MINE = 7
    STONE_PILLARS = 22
    ALCHEMIST_LAB = 1
    MONASTERY = 17
    LABYRINTH = 16
    IRON_STRONGHOLD = 14
    ANCIENT_PYRAMID = 2
    HALL_OF_LEGENDS = 10


class Building(NamedTuple):
    uid: BuildingId
    name: str
    tier: Decimal
    alignment: Alignment
    base_production: Decimal
    base_price: Decimal

    @staticmethod
    def get_by_id(uid: BuildingId) -> Building:
        return _ALL_BUILDINGS[uid]

    @staticmethod
    def all() -> Iterable[Building]:
        return list(_ALL_BUILDINGS.values())


_ALL_BUILDINGS: Dict[BuildingId, Building] = { b.uid: b for b in [
    Building(
        BuildingId.FARM, 'Farm', Decimal(1),
        Alignment.NEUTRAL, Decimal(2), Decimal(10)
    ),
    Building(
        BuildingId.INN, 'Inn', Decimal(2),
        Alignment.NEUTRAL, Decimal(6), Decimal(125)
    ),
    Building(
        BuildingId.BLACKSMITH, 'Blacksmith', Decimal(3),
        Alignment.NEUTRAL, Decimal(20), Decimal(600)
    ),
    Building(
        BuildingId.DEEP_MINE, 'Deep Mine', Decimal(4),
        Alignment.NEUTRAL, Decimal(65), Decimal(1800)
    ),
    Building(
        BuildingId.STONE_PILLARS, 'Stone Pillars', Decimal(5),
        Alignment.NEUTRAL, Decimal(200), Decimal(5600)
    ),
    Building(
        BuildingId.ALCHEMIST_LAB, 'Alchemist Lab', Decimal(6),
        Alignment.NEUTRAL, Decimal(650), Decimal(38000)
    ),
    Building(
        BuildingId.MONASTERY, 'Monastery', Decimal(7),
        Alignment.NEUTRAL, Decimal(2000), Decimal(442000)
    ),
    Building(
        BuildingId.LABYRINTH, 'Labyrinth', Decimal(8),
        Alignment.NEUTRAL, Decimal(8500), Decimal(7.3e6)
    ),
    Building(
        BuildingId.IRON_STRONGHOLD, 'Iron Stronghold', Decimal(9),
        Alignment.NEUTRAL, Decimal(100000), Decimal(145e6)
    ),
    Building(
        BuildingId.ANCIENT_PYRAMID, 'Ancient Pyramid', Decimal(10),
        Alignment.NEUTRAL, Decimal(1.2e6), Decimal(3.2e9)
    ),
    Building(
        BuildingId.WARRIOR_BARRACKS, 'Warrior Barracks', Decimal(4),
        Alignment.GOOD, Decimal(65), Decimal(1800)
    ),
    Building(
        BuildingId.KNIGHTS_JOUST, 'Knight\'s Joust', Decimal(5),
        Alignment.GOOD, Decimal(200), Decimal(5600)
    ),
    Building(
        BuildingId.WIZARD_TOWER, 'Wizard Tower', Decimal(6),
        Alignment.GOOD, Decimal(650), Decimal(38000)
    ),
    Building(
        BuildingId.CATHEDRAL, 'Cathedral', Decimal(7),
        Alignment.GOOD, Decimal(2000), Decimal(442000)
    ),
    Building(
        BuildingId.CITADEL, 'Citadel', Decimal(8),
        Alignment.GOOD, Decimal(8500), Decimal(7.3e6)
    ),
    Building(
        BuildingId.ROYAL_CASTLE, 'Royal Castle', Decimal(9),
        Alignment.GOOD, Decimal(100000), Decimal(145e6)
    ),
    Building(
        BuildingId.HEAVENS_GATE, 'Heaven\'s Gate', Decimal(10),
        Alignment.GOOD, Decimal(1.2e6), Decimal(3.2e9)
    ),
    Building(
        BuildingId.SLAVE_PEN, 'Slave Pen', Decimal(4),
        Alignment.EVIL, Decimal(65), Decimal(1800)
    ),
    Building(
        BuildingId.ORCISH_ARENA, 'Orcish Arena', Decimal(5),
        Alignment.EVIL, Decimal(200), Decimal(5600)
    ),
    Building(
        BuildingId.WITCH_CONCLAVE, 'Witch Conclave', Decimal(6),
        Alignment.EVIL, Decimal(650), Decimal(38000)
    ),
    Building(
        BuildingId.DARK_TEMPLE, 'Dark Temple', Decimal(7),
        Alignment.EVIL, Decimal(2000), Decimal(442000)
    ),
    Building(
        BuildingId.NECROPOLIS, 'Necropolis', Decimal(8),
        Alignment.EVIL, Decimal(8500), Decimal(7.3e6)
    ),
    Building(
        BuildingId.EVIL_FORTRESS, 'Evil Fortress', Decimal(9),
        Alignment.EVIL, Decimal(100000), Decimal(145e6)
    ),
    Building(
        BuildingId.HELL_PORTAL, 'Hell Portal', Decimal(10),
        Alignment.EVIL, Decimal(1.2e6), Decimal(3.2e9)
    ),
    Building(
        BuildingId.HALL_OF_LEGENDS, 'Hall of Legends', Decimal(11),
        Alignment.NEUTRAL, Decimal(250000), Decimal(2e11)
    )
]}
