from typing import Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.RemoteData import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition

INDEX_SERVO = 0
INDEX_POSITION = 1


class Msg_servoPosition(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterServoPosition]]

    def __init__(self, id: int = LegControllerProtocol.MSG_SERVO_POSITION):
        super().__init__(id, "servoPosition", "actual servo position")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, position: int = None,
    ) -> "Msg_servoPosition":
        cmd = Msg_servoPosition(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_position(self) -> float:
        return self._parameter_list[INDEX_POSITION].get_value()

    def set_data(self, index: int, position: float) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[INDEX_POSITION].set_value(position)
