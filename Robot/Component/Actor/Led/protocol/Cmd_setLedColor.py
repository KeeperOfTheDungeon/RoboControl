# disabled for micropython  # from typing import List, Union

from Devices.LegSensors import LegSensorsProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_LED = 0
INDEX_COLOR = 1


class Cmd_setLedColor(RemoteCommand):
    _parameter_list: "List[Union[RemoteParameterHsvColor, RemoteParameterUint8]]"

    def __init__(self, id: int = LegSensorsProtocol.CMD_LED_SET_COLOR):
        super().__init__(id, "setLedColor", "set color of an RGB LED")
        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))
        self._parameter_list.append(RemoteParameterHsvColor("color", "LED color"))

    def set_index(self, index: int) -> None:
        self._parameter_list[INDEX_LED].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_LED].get_value()

    def set_data(self, index: int, color: HsvColor) -> None:
        self._parameter_list[INDEX_LED].set_value(index)
        self._parameter_list[INDEX_COLOR].set_value(color)

    def get_color(self) -> HsvColor:
        return self._parameter_list[INDEX_COLOR].get_color()

    @staticmethod
    def get_command(id, index: int = None, color: HsvColor = None):
        cmd = Cmd_setLedColor(id)
        if None not in [index, color]:
            cmd.set_data(index, color)
        return cmd
