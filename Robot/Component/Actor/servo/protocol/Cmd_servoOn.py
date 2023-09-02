from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SERVO = 0


class Cmd_servoOn(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_ON):
        super().__init__(id, "cmd_servoOn", "switch servo on")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, local_id) -> "Cmd_servoOn":
        cmd = Cmd_servoOn(id)
        cmd.set_index(local_id)  # maybe move the 1 << local_id here?
        return cmd
