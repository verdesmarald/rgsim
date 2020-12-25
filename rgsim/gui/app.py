"""Entry point for GUI app"""
from __future__ import annotations

import wx # type: ignore

from .. import simulator
from ..entities import building, upgrade

from . import building_panel, resources_panel, shared


class RGSimulatorApp(wx.App):
    def OnInit(self) -> bool:
        main_frame = MainWindow(None)
        main_frame.Show()
        return True


class MainWindow(wx.Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.root_panel = wx.Panel(self)
        self.sizer = wx.BoxSizer()

        self.resources_panel = resources_panel.ResourcesPanel(self.root_panel)
        self.sizer.Add(self.resources_panel)

        self.building_panel = building_panel.BuildingPanel(self.root_panel)
        self.sizer.Add(self.building_panel)

        self.root_panel.SetSizerAndFit(self.sizer)

        self.SetSize((1200, 900))
        self.SetTitle("RG Simulator")
        self.Centre()
        self.Show()


def main():
    shared.game_state.purchase_building(building.FARM.id_, 10)
    shared.game_state.purchase_upgrade(upgrade.IRRIGATION)
    RGSimulatorApp().MainLoop()


if __name__ == '__main__':
    main()
