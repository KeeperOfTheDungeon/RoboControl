from typing import List

from Devices.LegSensors import LegSensorsProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8


class Cmd_getLedBrightness(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]
    _index = 0

    def __init__(self, id: int = LegSensorsProtocol.CMD_LED_GET_BRIGHTNESS):
        super().__init__(id, "getLedBrightness", "get brightness of a LED")
        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))

    def set_index(self, index):
        self._parameter_list[self._index].set_value(index)

    def get_index(self):
        return self._parameter_list[self._index].get_value()

    @staticmethod
    def get_command(id, index):
        cmd = Cmd_getLedBrightness()
        cmd.set_id(id)
        cmd.set_index(index)
        return cmd
