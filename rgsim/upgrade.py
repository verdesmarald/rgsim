from __future__ import annotations

from enum import Enum, auto
from dataclasses import dataclass, field
from decimal import Decimal
from typing import Any, Callable, Dict, Iterable, List, TYPE_CHECKING

from building import BuildingId
from faction import Alignment

import modifier

if TYPE_CHECKING:
    from sim import GameState

class UpgradeId(Enum):
    GRINDING_DEDICATION = auto()
    # region Deeds
    PROOF_OF_GOOD_DEED = auto()
    PROOF_OF_EVIL_DEED = auto()
    PROOF_OF_NEUTRALITY = auto()
    #endregion
    #region Clicking
    STURDY_TREASURE = auto()
    DURABLE_TREASURE = auto()
    REINFORCED_TREASURE = auto()
    RESILIENT_TREASURE = auto()
    UNBREAKABLE_TREASURE = auto()
    ETERNAL_TREASURE = auto()
    FILLED_TREASURE = auto()
    RICH_TREASURE = auto()
    WEALTHY_TREASURE = auto()
    OPULENT_TREASURE = auto()
    OVERFLOWING_TREASURE = auto()
    PRECIOUS_TREASURE = auto()
    ORNATE_TREASURE = auto()
    ADORNED_TREASURE = auto()
    EMBELLISHED_TREASURE = auto()
    RESPLENDENT_TREASURE = auto()
    #endregion
    #region Farms
    CROP_ROTATION = auto()
    IRRIGATION = auto()
    PROFESSIONAL_FARMERS = auto()
    PERFECT_SEEDS = auto()
    VERTICAL_FARMS = auto()
    FARMING_TOOLS = auto()
    ANIMAL_HERDING = auto()
    HEAVY_PLOW = auto()
    GOLDEN_SPOON = auto()
    INCREASED_FERTILE_AREA = auto()
    MAGICALLY_MODIFIED_ORGANISMS = auto()
    SUPERIOR_FERTILIZER = auto()
    SENTIENT_VEGETABLES = auto()
    CORN_MULTIPLICATION = auto()
    FRUIT_ARMY = auto()
    MIXED_MANURE = auto()
    SIDE_ORCHARDS = auto()
    CATTLE_DOMAIN = auto()
    POULTRY_FEED = auto()
    #endregion


@dataclass
class Upgrade:
    uid: UpgradeId
    name: str
    cost: Decimal
    effects: List[modifier.Modifier] = field(default_factory=list)
    available: Callable[[GameState], bool] = lambda _: True
    unlocked: Callable[[GameState], bool] = lambda _: True

    @staticmethod
    def get_by_id(uid: UpgradeId) -> Upgrade:
        return _ALL_UPGRADES[uid]

    @staticmethod
    def all() -> Iterable[Upgrade]:
        return list(_ALL_UPGRADES.values())

    def add_modifier(self, modifier: modifier.Modifier) -> Upgrade:
        modifier.uid = f'{self.uid.value}.{len(self.effects)}'
        self.effects.append(modifier)
        return self


_ALL_UPGRADES: Dict[UpgradeId, Upgrade] = { u.uid: u for u in [
    Upgrade(UpgradeId.GRINDING_DEDICATION, 'Grinding Dedication', Decimal(1e21))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(2),
                modifier.alignment_filter(Alignment.NEUTRAL)
            )
        )
    ,
    #region Deeds
    Upgrade(UpgradeId.PROOF_OF_GOOD_DEED, 'Proof of Good Deed', Decimal(25000)),
    Upgrade(UpgradeId.PROOF_OF_EVIL_DEED, 'Proof of Evil Deed', Decimal(25000)),
    Upgrade(UpgradeId.PROOF_OF_NEUTRALITY, 'Proof of Neutrality', Decimal(1e16)),
    #endregion
    #region Clicking
    Upgrade(UpgradeId.STURDY_TREASURE, 'Sturdy Treasure', Decimal(500))
        .add_modifier(modifier.additive(modifier.Target.CLICK_REWARD, modifier.fixed(4)))
        .add_modifier(
            modifier.additive(modifier.Target.OFFLINE_CLICKS_PER_SECOND, modifier.fixed(1))
        )
    ,
    Upgrade(UpgradeId.DURABLE_TREASURE, 'Durable Treasure', Decimal(5000))
        .add_modifier(modifier.additive(modifier.Target.CLICK_REWARD, modifier.fixed(45)))
        .add_modifier(
            modifier.additive(modifier.Target.OFFLINE_CLICKS_PER_SECOND, modifier.fixed(1))
        )
    ,
    Upgrade(UpgradeId.REINFORCED_TREASURE, 'Reinforced Treasure', Decimal(5e6))
        .add_modifier(modifier.additive(modifier.Target.CLICK_REWARD, modifier.fixed(4950)))
        .add_modifier(
            modifier.additive(modifier.Target.OFFLINE_CLICKS_PER_SECOND, modifier.fixed(1))
        )
    ,
    Upgrade(UpgradeId.RESILIENT_TREASURE, 'Resilient Treasure', Decimal(5e9))
        .add_modifier(modifier.additive(modifier.Target.CLICK_REWARD, modifier.fixed(500000)))
        .add_modifier(
            modifier.additive(modifier.Target.OFFLINE_CLICKS_PER_SECOND, modifier.fixed(1))
        )
    ,
    Upgrade(UpgradeId.UNBREAKABLE_TREASURE, 'Unbreakable Treasure', Decimal(5e13))
        .add_modifier(modifier.additive(modifier.Target.CLICK_REWARD, modifier.fixed(5e7)))
        .add_modifier(
            modifier.additive(modifier.Target.OFFLINE_CLICKS_PER_SECOND, modifier.fixed(1))
        )
    ,
    Upgrade(UpgradeId.ETERNAL_TREASURE, 'Eternal Treasure', Decimal(5e16))
        .add_modifier(modifier.additive(modifier.Target.CLICK_REWARD, modifier.fixed(5e10)))
        .add_modifier(
            modifier.additive(modifier.Target.OFFLINE_CLICKS_PER_SECOND, modifier.fixed(1))
        )
    ,
    Upgrade(UpgradeId.FILLED_TREASURE, 'Filled Treasure', Decimal(10000))
        .add_modifier(modifier.multiplicative(modifier.Target.CLICK_REWARD, modifier.fixed(1.25)))
        .add_modifier(
            modifier.multiplicative(modifier.Target.BUILDING_PRODUCTION, modifier.fixed(1.25))
        )
    ,
    Upgrade(UpgradeId.RICH_TREASURE, 'Rich Treasure', Decimal(5e7))
        .add_modifier(modifier.multiplicative(modifier.Target.CLICK_REWARD, modifier.fixed(1.25)))
        .add_modifier(
            modifier.multiplicative(modifier.Target.BUILDING_PRODUCTION, modifier.fixed(1.25))
        )
    ,
    Upgrade(UpgradeId.WEALTHY_TREASURE, 'Wealthy Treasure', Decimal(1e11))
        .add_modifier(modifier.multiplicative(modifier.Target.CLICK_REWARD, modifier.fixed(1.25)))
        .add_modifier(
            modifier.multiplicative(modifier.Target.BUILDING_PRODUCTION, modifier.fixed(1.25))
        )
    ,
    Upgrade(UpgradeId.OPULENT_TREASURE, 'Opulent Treasure', Decimal(5e12))
        .add_modifier(modifier.multiplicative(modifier.Target.CLICK_REWARD, modifier.fixed(1.25)))
        .add_modifier(
            modifier.multiplicative(modifier.Target.BUILDING_PRODUCTION, modifier.fixed(1.25))
        )
    ,
    Upgrade(UpgradeId.OVERFLOWING_TREASURE, 'Overflowing Treasure', Decimal(5e15))
        .add_modifier(modifier.multiplicative(modifier.Target.CLICK_REWARD, modifier.fixed(1.25)))
        .add_modifier(
            modifier.multiplicative(modifier.Target.BUILDING_PRODUCTION, modifier.fixed(1.25))
        )
    ,
    Upgrade(UpgradeId.PRECIOUS_TREASURE, 'Precious Treasure', Decimal(50000))
        .add_modifier(
            modifier.additive(
                modifier.Target.CLICK_REWARD,
                lambda state, _target: 0.01 * state.total_production()
            )
        )
    ,
    Upgrade(UpgradeId.ORNATE_TREASURE, 'Ornate Treasure', Decimal(5e7))
        .add_modifier(
            modifier.additive(
                modifier.Target.CLICK_REWARD,
                lambda state, _target: 0.01 * state.total_production()
            )
        )
    ,
    Upgrade(UpgradeId.ADORNED_TREASURE, 'Adorned Treasure', Decimal(5e10))
        .add_modifier(
            modifier.additive(
                modifier.Target.CLICK_REWARD,
                lambda state, _target: 0.01 * state.total_production()
            )
        )
    ,
    Upgrade(UpgradeId.EMBELLISHED_TREASURE, 'Embellished Treasure', Decimal(5e13))
        .add_modifier(
            modifier.additive(
                modifier.Target.CLICK_REWARD,
                lambda state, _target: 0.01 * state.total_production()
            )
        )
    ,
    Upgrade(UpgradeId.RESPLENDENT_TREASURE, 'Resplendent Treasure', Decimal(5e15))
        .add_modifier(
            modifier.additive(
                modifier.Target.CLICK_REWARD,
                lambda state, _target: 0.01 * state.total_production()
            )
        )
    ,
    #endregion
    #region Farms
    Upgrade(UpgradeId.CROP_ROTATION, "Crop Rotation", Decimal(200))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(2),
                modifier.building_filter(BuildingId.FARM)
            )
        )
        .add_modifier(modifier.additive(modifier.Target.ASSISTANTS, modifier.fixed(1)))
    ,
    Upgrade(UpgradeId.IRRIGATION, "Irrigation", Decimal(6580))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(3),
                modifier.building_filter(BuildingId.FARM)
            )
        )
        .add_modifier(modifier.additive(modifier.Target.ASSISTANTS, modifier.fixed(1)))
    ,
    Upgrade(UpgradeId.PROFESSIONAL_FARMERS, "Professional Farmers", Decimal(1.07e7))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(4),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.PERFECT_SEEDS, "Perfect Seeds", Decimal(5.09e11))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(5),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.VERTICAL_FARMS, "Vertical Farms", Decimal(6.895e14))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(6),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.FARMING_TOOLS, "Farming Tools", Decimal(9.716e20))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(5),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.ANIMAL_HERDING, "Animal Herding", Decimal(1.331e27))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(4),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.HEAVY_PLOW, "Heavy Plow", Decimal(1.787e33))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(3),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.GOLDEN_SPOON, "Golden Spoon", Decimal(2.36e39))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(2),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.INCREASED_FERTILE_AREA, "Increased Fertile Area", Decimal(3.08e45))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(3),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.MAGICALLY_MODIFIED_ORGANISMS, "Magically Modified Organisms", Decimal(3.978e51))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(4),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.SUPERIOR_FERTILIZER, "Superior Fertilizer", Decimal(5.096e57))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(5),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.SENTIENT_VEGETABLES, "Sentient Vegetables", Decimal(6.483e63))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(6),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.CORN_MULTIPLICATION, "Corn Multiplication", Decimal(8.199e69))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(5),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.FRUIT_ARMY, "Fruit Army", Decimal(1.118e79))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(4),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.MIXED_MANURE, "Mixed Manure", Decimal(1.782e94))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(5),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.SIDE_ORCHARDS, "Side Orchards", Decimal(2.829e109))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(6),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.CATTLE_DOMAIN, "Cattle Domain", Decimal(4.477e124))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(5),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    ,
    Upgrade(UpgradeId.POULTRY_FEED, "Poultry Feed", Decimal(1.05e155))
        .add_modifier(
            modifier.multiplicative(
                modifier.Target.BUILDING_PRODUCTION,
                modifier.fixed(4),
                modifier.building_filter(BuildingId.FARM)
            )
        )
    #endregion
]}
