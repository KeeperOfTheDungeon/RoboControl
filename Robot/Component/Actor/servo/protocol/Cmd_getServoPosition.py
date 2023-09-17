from typing import List, Optional

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SERVO = 0


class Cmd_getServoPosition(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_MOVE_TO):
        super().__init__(id, "getServoPosition", "getPosition of a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: Optional[int] = None) -> "Cmd_getServoPosition":
        cmd = Cmd_getServoPosition(id)
        if index is not None:
            cmd.set_index(index)
        return cmd
