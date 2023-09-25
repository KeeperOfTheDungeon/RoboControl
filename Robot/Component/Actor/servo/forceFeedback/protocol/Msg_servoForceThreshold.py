from typing import Union, List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition

INDEX_SERVO = 0
INDEX_SPEED = 1


class Msg_servoForceThreshold(RemoteMessage):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterServoPosition]]

    def __init__(self, id: int = LegControllerProtocol.MSG_SERVO_POSITION):
        super().__init__(id, "servoForceThreshold", "actual servo force threshold")
        self._servo_index = 0
        self._servo_position = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("speed", "servo force threshold"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            position: int = None,
    ) -> "Msg_servoForceThreshold":
        cmd = Msg_servoForceThreshold(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd

    def get_index(self) -> int:
        """ "get sensor index for sensor corresponding to this message" """
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_force_threshold(self) -> int:
        """
        :return: "gradient"
        """
        return self._parameter_list[INDEX_SPEED].get_value()

    def set_data(self, index: int, position: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[INDEX_SPEED].set_value(position)
