from __future__ import annotations

from typing import TYPE_CHECKING

import wx # type: ignore

from . import shared

if TYPE_CHECKING:
    from ..entities import building


class ResourcesPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        self.gold = wx.Button(self, label=str(f'Gold: {shared.game_state.gold} (+{shared.game_state.calculate_building_production()}/s)'))
        self.sizer.Add(self.gold)

        self.gems = wx.Button(self, label=str(f'Gems: {shared.game_state.gems}'))
        self.sizer.Add(self.gems)

        self.mana = wx.Button(self, label=str(f'Mana: {shared.game_state.mana}'))
        self.sizer.Add(self.mana)

        self.SetSizerAndFit(self.border)
