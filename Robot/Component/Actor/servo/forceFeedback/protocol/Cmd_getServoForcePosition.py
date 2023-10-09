from typing import List

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SERVO = 0


class Cmd_getServoForcePosition(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int):
        super().__init__(id, "getServoForcePosition", "get force position of a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_getServoForcePosition":
        cmd = Cmd_getServoForcePosition(id)
        if index is not None:
            cmd.set_data(index)
        return cmd
