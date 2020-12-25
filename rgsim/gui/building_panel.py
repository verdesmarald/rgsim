from __future__ import annotations

from typing import TYPE_CHECKING

import wx # type: ignore

from . import shared

if TYPE_CHECKING:
    from ..entities import building


class BuildingPanel(wx.Panel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.border = wx.BoxSizer()
        self.border.Add(self.sizer, 1, wx.ALL | wx.EXPAND, 5)

        for building_state in shared.game_state.buildings.values():
            self.button = wx.Button(self, label=str(f'{building_state.building.name}: {building_state.owned}'))
            self.sizer.Add(self.button)

        self.SetSizerAndFit(self.border)
