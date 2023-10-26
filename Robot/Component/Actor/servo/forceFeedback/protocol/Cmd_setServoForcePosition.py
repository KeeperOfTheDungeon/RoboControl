from typing import Union

from RoboControl.Com.RemoteParameter import RemoteParameterUint16
from RoboControl.Com.RemoteData import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8

INDEX_SERVO = 0
INDEX_SPEED = 1


class Cmd_setServoForcePosition(RemoteCommand):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int):
        super().__init__(id, "setServoForcePosition", "set servos force position")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterUint16("speed", "new servo force position"))

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
    ) -> "Cmd_setServoForcePosition":
        cmd = Cmd_setServoForcePosition(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd
