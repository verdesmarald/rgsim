from __future__ import annotations

from enum import unique, Enum
from dataclasses import dataclass, field, replace
from decimal import Decimal
from typing import Callable, Dict, Iterable, Optional, TYPE_CHECKING

from . import alignment, building, entity, modifier
from .. import filters

if TYPE_CHECKING:
    from .. import simulator


@unique
class UpgradeId(Enum):
    GRINDING_DEDICATION = 32
    PROOF_OF_EVIL_DEED = 178
    PROOF_OF_GOOD_DEED = 224
    PROOF_OF_NEUTRALITY = 388
    PROOF_OF_BALANCE = 747
    PROOF_OF_CHAOS = 748
    PROOF_OF_ORDER = 749
    STURDY_TREASURE = 101501
    DURABLE_TREASURE = 101502
    REINFORCED_TREASURE = 101503
    RESILIENT_TREASURE = 101504
    UNBREAKABLE_TREASURE = 101505
    ETERNAL_TREASURE = 101506
    FILLED_TREASURE = 101601
    RICH_TREASURE = 101602
    WEALTHY_TREASURE = 101603
    OPULENT_TREASURE = 101604
    OVERFLOWING_TREASURE = 101605
    PRECIOUS_TREASURE = 101701
    ORNATE_TREASURE = 101702
    ADORNED_TREASURE = 101703
    EMBELLISHED_TREASURE = 101704
    RESPLENDENT_TREASURE = 101705
    ABSENT_RULER = 147901
    MISSING_RULER = 147902
    NONEXISTENT_RULER = 147903
    CROP_ROTATION = 501001
    IRRIGATION = 501002
    PROFESSIONAL_FARMERS = 501003
    PERFECT_SEEDS = 501004
    VERTICAL_FARMS = 501005
    FARMING_TOOLS = 501006
    ANIMAL_HERDING = 501007
    HEAVY_PLOW = 501008
    GOLDEN_SPOON = 501009
    INCREASED_FERTILE_AREA = 501010
    MAGICALLY_MODIFIED_ORGANISMS = 501011
    SUPERIOR_FERTILIZER = 501012
    SENTIENT_VEGETABLES = 501013
    CORN_MULTIPLICATION = 501014
    FRUIT_ARMY = 501015
    MIXED_MANURE = 501016
    SIDE_ORCHARDS = 501017
    CATTLE_DOMAIN = 501018
    POULTRY_FEED = 501019


@dataclass(frozen=True)
class Upgrade(entity.Entity):
    id_: UpgradeId
    cost: Decimal
    effects: Iterable[modifier.Modifier] = field(default_factory=tuple)
    available: Callable[[simulator.GameState], bool] = lambda _: True
    unlocked: Callable[[simulator.GameState], bool] = lambda _: True
    _name_override: Optional[str] = None

    @property
    def name(self) -> str:
        if self._name_override is not None:
            return self._name_override

        return self.id_.name.replace('_', ' ').title()

    def __post_init__(self) -> None:
        super().__post_init__()
        object.__setattr__(self, 'effects', (replace(m, owner=self) for m in self.effects))


def _register(u: Upgrade) -> Upgrade:
    if u.id_ in _ALL_UPGRADES:
        err_str = f'Duplicate upgrade id {u.id_} for upgrades {u.name}, {get(u.id_).name}'
        raise ValueError(err_str)

    _ALL_UPGRADES[u.id_] = u
    return u


def get(id_: UpgradeId) -> Upgrade:
    return _ALL_UPGRADES[id_]


def all() -> Iterable[Upgrade]:
    return list(_ALL_UPGRADES.values())


_ALL_UPGRADES: Dict[UpgradeId, Upgrade] = {}

GRINDING_DEDICATION: Upgrade = _register(Upgrade(
    UpgradeId.GRINDING_DEDICATION, Decimal(1e21),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(2),
            filters.alignment(alignment.NEUTRAL)
        ),
    )
))

#region Deeds
PROOF_OF_EVIL_DEED: Upgrade = _register(Upgrade(UpgradeId.PROOF_OF_EVIL_DEED, Decimal(25000)))
PROOF_OF_GOOD_DEED: Upgrade = _register(Upgrade(UpgradeId.PROOF_OF_GOOD_DEED, Decimal(25000)))
PROOF_OF_NEUTRALITY: Upgrade = _register(Upgrade(UpgradeId.PROOF_OF_NEUTRALITY, Decimal(1e16)))
PROOF_OF_BALANCE: Upgrade = _register(Upgrade(UpgradeId.PROOF_OF_BALANCE, Decimal(1e15)))
PROOF_OF_CHAOS: Upgrade = _register(Upgrade(UpgradeId.PROOF_OF_CHAOS, Decimal(1e15)))
PROOF_OF_ORDER: Upgrade = _register(Upgrade(UpgradeId.PROOF_OF_ORDER, Decimal(1e15)))
#endregion

#region Clicking
STURDY_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.STURDY_TREASURE, Decimal(500),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(4)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.OFFLINE_CLICKS_PER_SECOND,
            modifier.fixed(1)
        ),
    )
))
DURABLE_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.DURABLE_TREASURE, Decimal(5000),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(45)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.OFFLINE_CLICKS_PER_SECOND,
            modifier.fixed(1)
        ),
    )
))
REINFORCED_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.REINFORCED_TREASURE, Decimal(5e6),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(4950)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.OFFLINE_CLICKS_PER_SECOND,
            modifier.fixed(1)
        ),
    )
))
RESILIENT_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.RESILIENT_TREASURE, Decimal(5e9),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(500000)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.OFFLINE_CLICKS_PER_SECOND,
            modifier.fixed(1)
        ),
    )
))
UNBREAKABLE_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.UNBREAKABLE_TREASURE, Decimal(5e13),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(5e7)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.OFFLINE_CLICKS_PER_SECOND,
            modifier.fixed(1)
        ),
    )
))
ETERNAL_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.ETERNAL_TREASURE, Decimal(5e16),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(5e10)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.OFFLINE_CLICKS_PER_SECOND,
            modifier.fixed(1)
        ),
    )
))
FILLED_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.FILLED_TREASURE, Decimal(10000),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(1.25)
        ),
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(1.25)
        ),
    )
))
RICH_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.RICH_TREASURE, Decimal(5e7),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(1.25)
        ),
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(1.25)
        ),
    )
))
WEALTHY_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.WEALTHY_TREASURE, Decimal(1e11),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(1.25)
        ),
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(1.25)
        ),
    )
))
OPULENT_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.OPULENT_TREASURE, Decimal(5e12),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(1.25)
        ),
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(1.25)
        ),
    )
))
OVERFLOWING_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.OVERFLOWING_TREASURE, Decimal(5e15),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.CLICK_REWARD,
            modifier.fixed(1.25)
        ),
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(1.25)
        ),
    )
))
PRECIOUS_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.PRECIOUS_TREASURE, Decimal(50000),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            lambda state, _target: 0.01 * state.total_production()
        ),
    )
))
ORNATE_TREASURE: Upgrade = _register(Upgrade(
    UpgradeId.ORNATE_TREASURE, Decimal(5e7),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            lambda state, _target: 0.01 * state.total_production()
        ),
    )
))
ADORNED_TREASURE: Upgrade = _register(Upgrade(UpgradeId.ADORNED_TREASURE, Decimal(5e10),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            lambda state, _target: 0.01 * state.total_production()
        ),
    )
))
EMBELLISHED_TREASURE: Upgrade = _register(Upgrade(UpgradeId.EMBELLISHED_TREASURE, Decimal(5e13),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            lambda state, _target: 0.01 * state.total_production()
        ),
    )
))
RESPLENDENT_TREASURE: Upgrade = _register(Upgrade(UpgradeId.RESPLENDENT_TREASURE, Decimal(5e15),
    effects=(
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.CLICK_REWARD,
            lambda state, _target: 0.01 * state.total_production()
        ),
    )
))
#endregion
#region Farms
CROP_ROTATION: Upgrade = _register(Upgrade(UpgradeId.CROP_ROTATION, Decimal(200),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(2),
            filters.building(building.FARM)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.ASSISTANTS,
            modifier.fixed(1)
        ),
    )
))
IRRIGATION: Upgrade = _register(Upgrade(UpgradeId.IRRIGATION, Decimal(6580),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(3),
            filters.building(building.FARM)
        ),
        modifier.Modifier(
            modifier.Strategy.ADDITIVE,
            modifier.Target.ASSISTANTS,
            modifier.fixed(1)
        ),
    )
))
PROFESSIONAL_FARMERS: Upgrade = _register(Upgrade(
    UpgradeId.PROFESSIONAL_FARMERS, Decimal(1.07e7),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(4),
            filters.building(building.FARM)
        ),
    )
))
PERFECT_SEEDS: Upgrade = _register(Upgrade(
    UpgradeId.PERFECT_SEEDS, Decimal(5.09e11),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(5),
            filters.building(building.FARM)
        ),
    )
))
VERTICAL_FARMS: Upgrade = _register(Upgrade(
    UpgradeId.VERTICAL_FARMS, Decimal(6.895e14),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(6),
            filters.building(building.FARM)
        ),
    )
))
FARMING_TOOLS: Upgrade = _register(Upgrade(
    UpgradeId.FARMING_TOOLS, Decimal(9.716e20),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(5),
            filters.building(building.FARM)
        ),
    )
))
ANIMAL_HERDING: Upgrade = _register(Upgrade(
    UpgradeId.ANIMAL_HERDING, Decimal(1.331e27),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(4),
            filters.building(building.FARM)
        ),
    )
))
HEAVY_PLOW: Upgrade = _register(Upgrade(
    UpgradeId.HEAVY_PLOW, Decimal(1.787e33),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(3),
            filters.building(building.FARM)
        ),
    )
))
GOLDEN_SPOON: Upgrade = _register(Upgrade(
    UpgradeId.GOLDEN_SPOON, Decimal(2.36e39),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(2),
            filters.building(building.FARM)
        ),
    )
))
INCREASED_FERTILE_AREA: Upgrade = _register(Upgrade(
    UpgradeId.INCREASED_FERTILE_AREA, Decimal(3.08e45),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(3),
            filters.building(building.FARM)
        ),
    )
))
MAGICALLY_MODIFIED_ORGANISMS: Upgrade = _register(Upgrade(
    UpgradeId.MAGICALLY_MODIFIED_ORGANISMS, Decimal(3.978e51),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(4),
            filters.building(building.FARM)
        ),
    )
))
SUPERIOR_FERTILIZER: Upgrade = _register(Upgrade(
    UpgradeId.SUPERIOR_FERTILIZER, Decimal(5.096e57),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(5),
            filters.building(building.FARM)
        ),
    )
))
SENTIENT_VEGETABLES: Upgrade = _register(Upgrade(
    UpgradeId.SENTIENT_VEGETABLES, Decimal(6.483e63),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(6),
            filters.building(building.FARM)
        ),
    )
))
CORN_MULTIPLICATION: Upgrade = _register(Upgrade(
    UpgradeId.CORN_MULTIPLICATION, Decimal(8.199e69),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(5),
            filters.building(building.FARM)
        ),
    )
))
FRUIT_ARMY: Upgrade = _register(Upgrade(
    UpgradeId.FRUIT_ARMY, Decimal(1.118e79),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(4),
            filters.building(building.FARM)
        ),
    )
))
MIXED_MANURE: Upgrade = _register(Upgrade(
    UpgradeId.MIXED_MANURE, Decimal(1.782e94),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(5),
            filters.building(building.FARM)
        ),
    )
))
SIDE_ORCHARDS: Upgrade = _register(Upgrade(
    UpgradeId.SIDE_ORCHARDS, Decimal(2.829e109),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(6),
            filters.building(building.FARM)
        ),
    )
))
CATTLE_DOMAIN: Upgrade = _register(Upgrade(
    UpgradeId.CATTLE_DOMAIN, Decimal(4.477e124),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(5),
            filters.building(building.FARM)
        ),
    )
))
POULTRY_FEED: Upgrade = _register(Upgrade(
    UpgradeId.POULTRY_FEED, Decimal(1.05e155),
    effects=(
        modifier.Modifier(
            modifier.Strategy.MULTIPLICATIVE,
            modifier.Target.BUILDING_PRODUCTION,
            modifier.fixed(4),
            filters.building(building.FARM)
        ),
    )
))
#endregion
