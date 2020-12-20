from __future__ import annotations

from decimal import Decimal
from dataclasses import dataclass, field
from typing import Any, Dict

from building import Building, BuildingId
import modifier
from upgrade import Upgrade, UpgradeId


_DEFAULT_MODIFIERS = [
    modifier.additive(modifier.Target.CLICK_REWARD, modifier.fixed(1), uid='default.click'),
    modifier.additive(modifier.Target.MAX_MANA, modifier.fixed(1000), uid='default.mana'),
    modifier.additive(modifier.Target.MANA_REGEN, modifier.fixed(1), uid='default.manaRegen'),
    modifier.multiplicative(
        modifier.Target.BUILDING_PRODUCTION,
        lambda state, _target: state.trophies,
        modifier.building_filter(BuildingId.HALL_OF_LEGENDS),
        uid="default.holMultiplier"
    )
]


@dataclass
class UpgradeState:
    upgrade: Upgrade
    purchased: bool = False


@dataclass
class BuildingState:
    building: Building
    owned: Decimal = Decimal(0)


@dataclass
class GameState:
    mana: Decimal = Decimal(0)
    gold: Decimal = Decimal(0)
    gems: Decimal = Decimal(0)
    trophies: Decimal = Decimal(0)
    treasury: Decimal = Decimal(0)
    excavations: Decimal = Decimal(0)

    buildings: Dict[BuildingId, BuildingState] = field(default_factory=lambda: {
        b.uid: BuildingState(b) for b in Building.all()
    })
    upgrades: Dict[UpgradeId, UpgradeState] = field(default_factory=lambda: {
        u.uid: UpgradeState(u) for u in Upgrade.all()
    })
    modifiers: Dict[modifier.Strategy, Dict[modifier.Target, Dict[str, modifier.Modifier]]] = field(
        default_factory=lambda: {
            m.strategy : {m.target : {m.uid: m}} for m in _DEFAULT_MODIFIERS
        }
    )

    def purchase_building(self, building_id: BuildingId, quantity: Decimal) -> GameState:
        self.buildings[building_id].owned += quantity

        return self

    def purchase_upgrade(self, upgrade_id: UpgradeId, spend_gold: bool = False) -> GameState:
        if not self.upgrades[upgrade_id].purchased:
            self.upgrades[upgrade_id].purchased = True

            upgrade = Upgrade.get_by_id(upgrade_id)
            for modifier in upgrade.effects:
                self.register_modifier(modifier)

            if spend_gold:
                self.gold -= upgrade.cost

        return self

    def unpurchase_upgrade(self, upgrade_id: UpgradeId, credit_gold: bool = False) -> GameState:
        if self.upgrades[upgrade_id].purchased:
            self.upgrades[upgrade_id].purchased = False

            upgrade = Upgrade.get_by_id(upgrade_id)
            for modifier in upgrade.effects:
                self.deregister_modifier(modifier)

            if credit_gold:
                self.gold += upgrade.cost

        return self

    def register_modifier(self, modifier: modifier.Modifier) -> GameState:
        self.modifiers \
            .setdefault(modifier.strategy, {}) \
            .setdefault(modifier.target, {}) \
            [modifier.uid] = modifier

        return self

    def deregister_modifier(self, modifier: modifier.Modifier) -> GameState:
        self.modifiers \
            .setdefault(modifier.strategy, {}) \
            .setdefault(modifier.target, {}) \
            .pop(modifier.uid, None)

        return self

    def calculate_building_production(self) -> Decimal:
        production = Decimal(0)

        for building_state in self.buildings.values():
            if building_state.owned == 0:
                continue

            production += building_state.owned * self.apply_modifiers(
                building_state.building,
                modifier.Target.BUILDING_PRODUCTION,
                building_state.building.base_production
            )

        return production

    def apply_modifiers(
        self, target: Any, modifer_type: modifier.Target, base_value: Decimal = Decimal(0)
    ):
        additive_mods = self.modifiers \
            .get(modifier.Strategy.ADDITIVE, {}) \
            .get(modifer_type, {}) \
            .values()
        multiplicative_mods = self.modifiers \
            .get(modifier.Strategy.MULTIPLICATIVE, {}) \
            .get(modifer_type, {}) \
            .values()

        result = base_value

        for mod in additive_mods:
            if mod.applies_to(self, target):
                result += mod.amount(self, target)

        for mod in multiplicative_mods:
            if mod.applies_to(self, target):
                result *= mod.amount(self, target)

        return result


if __name__ == '__main__':
    state = GameState().purchase_building(BuildingId.FARM, Decimal(12))
    print(state.calculate_building_production())
    state.purchase_upgrade(UpgradeId.CROP_ROTATION)
    print(state.calculate_building_production())
    state.purchase_upgrade(UpgradeId.IRRIGATION)
    print(state.calculate_building_production())
    state.unpurchase_upgrade(UpgradeId.CROP_ROTATION)
    print(state.calculate_building_production())
    state \
        .purchase_building(BuildingId.FARM, Decimal(10)) \
        .purchase_building(BuildingId.INN, Decimal(10))
    print(state.calculate_building_production())