from typing import List

from Devices.LegSensors import LegSensorsProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8

LED_INDEX = 0
BRIGHTNESS_INDEX = 1


class Cmd_setLedBrightness(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = LegSensorsProtocol.CMD_LED_SET_BRIGHTNESS):
        super().__init__(id, "setLedBrightness", "set brightness of a LED")
        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))
        self._parameter_list.append(RemoteParameterUint8("brightness", "LED brightness"))

    def set_index(self, index: int) -> None:
        self._parameter_list[LED_INDEX].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[LED_INDEX].get_value()

    def set_brightness(self, brightness: float) -> None:
        brightness = int(brightness * 255)
        self._parameter_list[BRIGHTNESS_INDEX].set_value(brightness)

    def get_brightness(self) -> float:
        value = self._parameter_list[BRIGHTNESS_INDEX].get_value()
        return value / 255

    @staticmethod
    def get_command(id: int, index: int = None, brightness: float = None) -> "Cmd_setLedBrightness":
        cmd = Cmd_setLedBrightness(id)
        if index:
            cmd.set_index(index)
        if brightness:
            cmd.set_brightness(brightness)
        return cmd
