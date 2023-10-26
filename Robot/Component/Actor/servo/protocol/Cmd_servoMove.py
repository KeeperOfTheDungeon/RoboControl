from typing import List, Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoVelocity import RemoteParameterServoVelocity

INDEX_SERVO = 0
INDEX_VELOCITY = 1


class Cmd_servoMove(RemoteCommand):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterServoVelocity]]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_MOVE):
        super().__init__(id, "cmd_servoMove", "move servo at given velocity")

        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoVelocity("velocity", "velocity of this movement"))

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_velocity(self, velocity: float) -> None:
        self._parameter_list[INDEX_VELOCITY].set_velocity(velocity)

    def get_velocity(self) -> float:
        return self._parameter_list[INDEX_VELOCITY].get_velocity()

    @staticmethod
    def get_command(id: int, index, velocity: float) -> "Cmd_servoMove":
        cmd = Cmd_servoMove(id)
        # TODO java source allows skipping index and position
        cmd.set_index(index)
        cmd.set_velocity(velocity)
        return cmd
