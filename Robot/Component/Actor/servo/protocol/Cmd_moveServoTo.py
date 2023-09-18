from typing import List, Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition

INDEX_SERVO = 0
INDEX_POSITION = 1


class Cmd_moveServoTo(RemoteCommand):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterServoPosition]]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_MOVE_TO):
        super().__init__(id, "cmd_moveServoTo", "move servo to given position")

        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_position(self, position) -> None:
        self._parameter_list[INDEX_POSITION].set_position(position)

    def get_position(self) -> float:
        return self._parameter_list[INDEX_POSITION].get_position()

    @staticmethod
    def get_command(id: int, index, position: float) -> "Cmd_moveServoTo":
        cmd = Cmd_moveServoTo(id)
        # TODO java source allows skipping index and position
        cmd.set_index(index)
        cmd.set_position(position)
        return cmd
