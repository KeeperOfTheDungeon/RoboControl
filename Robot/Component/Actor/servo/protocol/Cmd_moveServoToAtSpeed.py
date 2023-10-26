from typing import List, Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoVelocity import RemoteParameterServoVelocity


INDEX_SERVO = 0
INDEX_POSITION = 1
INDEX_VELOCITY = 2


class Cmd_moveServoToAtSpeed(RemoteCommand):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterServoPosition, RemoteParameterServoVelocity]]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_MOVE_TO_AT_SPEED):
        super().__init__(id, "cmd_moveServoToAtSpeed", "move servo to given position at given speed")

        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))
        self._parameter_list.append(RemoteParameterServoVelocity("velocity", "servo velocity"))

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_position(self, position: float) -> None:
        self._parameter_list[INDEX_POSITION].set_position(position)

    def get_position(self) -> float:
        return self._parameter_list[INDEX_POSITION].get_position()

    def set_velocity(self, velocity: float) -> None:
        self._parameter_list[INDEX_VELOCITY].set_velocity(velocity)

    def get_velocity(self) -> float:
        return self._parameter_list[INDEX_VELOCITY].get_velocity()

    @staticmethod
    def get_command(id: int, index, position: float, velocity: float) -> "Cmd_moveServoToAtSpeed":
        cmd = Cmd_moveServoToAtSpeed(id)
        # TODO java source allows skipping index, position and velocity
        cmd.set_index(index)
        cmd.set_position(position)
        cmd.set_velocity(velocity)
        return cmd
