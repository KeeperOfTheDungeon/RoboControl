from typing import Union

from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SERVO = 0
INDEX_SPEED = 1


class Cmd_setServoForceThreshold(RemoteCommand):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int):
        super().__init__(id, "setServoForceThreshold", "set servos force threshold")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterUint16("speed", "new servo force threshold"))

    def set_data(self, index: int, position: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[INDEX_SPEED].set_value(position)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_speed(self) -> int:
        return self._parameter_list[INDEX_SPEED].get_value()

    @staticmethod
    def get_command(
            id: int,
            index: int = None, position: int = None
    ) -> "Cmd_setServoForceThreshold":
        cmd = Cmd_setServoForceThreshold(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd
