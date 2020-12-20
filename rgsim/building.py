"""Building definitions and functionality"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal
from typing import Dict, Iterable

from faction import Alignment

@dataclass
class Building():
    uid: int
    name: str
    tier: Decimal
    alignment: Alignment
    base_production: Decimal
    base_price: Decimal


def _register(b: Building) -> Building:
    _ALL_BUILDINGS[b.uid] = b
    return b


def get_by_id(uid: int) -> Building:
    return _ALL_BUILDINGS[uid]


def all() -> Iterable[Building]:
    return list(_ALL_BUILDINGS.values())


_ALL_BUILDINGS: Dict[int, Building] = {}

FARM = _register(Building(9, 'Farm', Decimal(1), Alignment.NEUTRAL, Decimal(2), Decimal(10)))
INN = _register(Building(13, 'Inn', Decimal(2), Alignment.NEUTRAL, Decimal(6), Decimal(125)))
BLACKSMITH = _register(Building(3, 'Blacksmith', Decimal(3), Alignment.NEUTRAL, Decimal(20), Decimal(600)))
DEEP_MINE = _register(Building(7, 'Deep Mine', Decimal(4), Alignment.NEUTRAL, Decimal(65), Decimal(1800)))
STONE_PILLARS = _register(Building(22, 'Stone Pillars', Decimal(5), Alignment.NEUTRAL, Decimal(200), Decimal(5600)))
ALCHEMIST_LAB = _register(Building(1, 'Alchemist Lab', Decimal(6), Alignment.NEUTRAL, Decimal(650), Decimal(38000)))
MONASTERY = _register(Building(17, 'Monastery', Decimal(7), Alignment.NEUTRAL, Decimal(2000), Decimal(442000)))
LABYRINTH = _register(Building(16, 'Labyrinth', Decimal(8), Alignment.NEUTRAL, Decimal(8500), Decimal(7.3e6)))
IRON_STRONGHOLD = _register(Building(14, 'Iron Stronghold', Decimal(9), Alignment.NEUTRAL, Decimal(100000), Decimal(145e6)))
ANCIENT_PYRAMID = _register(Building(2, 'Ancient Pyramid', Decimal(10), Alignment.NEUTRAL, Decimal(1.2e6), Decimal(3.2e9)))
WARRIOR_BARRACKS = _register(Building(23, 'Warrior Barracks', Decimal(4), Alignment.GOOD, Decimal(65), Decimal(1800)))
KNIGHTS_JOUST = _register(Building(15, 'Knight\'s Joust', Decimal(5), Alignment.GOOD, Decimal(200), Decimal(5600)))
WIZARD_TOWER = _register(Building(25, 'Wizard Tower', Decimal(6), Alignment.GOOD, Decimal(650), Decimal(38000)))
CATHEDRAL = _register(Building(4, 'Cathedral', Decimal(7), Alignment.GOOD, Decimal(2000), Decimal(442000)))
CITADEL = _register(Building(5, 'Citadel', Decimal(8), Alignment.GOOD, Decimal(8500), Decimal(7.3e6)))
ROYAL_CASTLE = _register(Building(20, 'Royal Castle', Decimal(9), Alignment.GOOD, Decimal(100000), Decimal(145e6)))
HEAVENS_GATE = _register(Building(11, 'Heaven\'s Gate', Decimal(10), Alignment.GOOD, Decimal(1.2e6), Decimal(3.2e9)))
SLAVE_PEN = _register(Building(21, 'Slave Pen', Decimal(4), Alignment.EVIL, Decimal(65), Decimal(1800)))
ORCISH_ARENA = _register(Building(19, 'Orcish Arena', Decimal(5), Alignment.EVIL, Decimal(200), Decimal(5600)))
WITCH_CONCLAVE = _register(Building(24, 'Witch Conclave', Decimal(6), Alignment.EVIL, Decimal(650), Decimal(38000)))
DARK_TEMPLE = _register(Building(6, 'Dark Temple', Decimal(7), Alignment.EVIL, Decimal(2000), Decimal(442000)))
NECROPOLIS = _register(Building(18, 'Necropolis', Decimal(8), Alignment.EVIL, Decimal(8500), Decimal(7.3e6)))
EVIL_FORTRESS = _register(Building(8, 'Evil Fortress', Decimal(9), Alignment.EVIL, Decimal(100000), Decimal(145e6)))
HELL_PORTAL = _register(Building(12, 'Hell Portal', Decimal(10), Alignment.EVIL, Decimal(1.2e6), Decimal(3.2e9)))
HALL_OF_LEGENDS = _register(Building(10, 'Hall of Legends', Decimal(11), Alignment.NEUTRAL, Decimal(250000), Decimal(2e11)))
