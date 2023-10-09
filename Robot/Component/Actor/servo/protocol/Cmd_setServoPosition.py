from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition

INDEX_SERVO = 0
INDEX_POSITION = 1


class Cmd_setServoPosition(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8 | RemoteParameterServoPosition]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_ON):
        super().__init__(
            id, "cmd_setServoPosition",
            "set servo position, if received, servo try to reach this position at full speed"
        )
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_position(self, position: float) -> None:
        self._parameter_list[INDEX_POSITION].set_position(position)

    def get_position(self) -> float:
        return self._parameter_list[INDEX_POSITION].get_position()

    @staticmethod
    def get_command(id: int, local_id, position: float) -> "Cmd_setServoPosition":
        cmd = Cmd_setServoPosition(id)
        cmd.set_index(local_id)
        cmd.set_position(position)
        return cmd
