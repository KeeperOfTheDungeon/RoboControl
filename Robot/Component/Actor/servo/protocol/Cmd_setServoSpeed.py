from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition

INDEX_SERVO = 0
INDEX_SPEED = 1


class Cmd_setServoSpeed(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8 | RemoteParameterServoPosition]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_ON):
        super().__init__(
            id, "cmd_setServoSpeed",
            "set servos actual speed"
        )
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("speed", "servo speed"))

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_speed(self, speed: float) -> None:
        self._parameter_list[INDEX_SPEED].set_value(speed)

    def get_speed(self) -> float:
        return self._parameter_list[INDEX_SPEED].get_value()

    @staticmethod
    def get_command(id: int, local_id, speed: float = None) -> "Cmd_setServoSpeed":
        cmd = Cmd_setServoSpeed(id)
        cmd.set_index(local_id)
        if speed:
            cmd.set_speed(speed)
        return cmd
