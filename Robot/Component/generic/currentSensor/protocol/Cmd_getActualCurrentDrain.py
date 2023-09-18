from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand

INDEX_SENSOR = 0


class Cmd_getActualCurrentDrain(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = LegControllerProtocol.CMD_GET_ACTUAL_CURRENT_DRAIN):
        super().__init__(id, "Cmd_getActualCurrentDrain", " get the actual current drain measured by this sensor")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_getActualCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
