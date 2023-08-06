from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SERVO = 0


class Cmd_servoOff(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_OFF):
        super().__init__(id, "cmd_servoOff", " switch servo off")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_servoOff(id)
        cmd.set_index(local_id)
        return cmd
