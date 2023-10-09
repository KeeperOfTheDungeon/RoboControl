from typing import Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage

INDEX_SENSOR = 0
INDEX_SPEED = 1


class Msg_servoSpeed(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int = LegControllerProtocol.MSG_SERVO_SPEED):
        super().__init__(id, "msg_servoSpeed", "actual servo speed")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterUint16("speed", "servo speed"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, speed: int = None,
    ) -> "Msg_servoSpeed":
        cmd = Msg_servoSpeed(id)
        if None not in [index, speed]:
            cmd.set_data(index, speed)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_speed(self):
        return self._parameter_list[INDEX_SPEED].get_value()

    def set_data(self, index: int, speed: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[INDEX_SPEED].set_value(speed)
