from typing import Union, List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoStatus import RemoteParameterServoStatus
# from RoboControl.Robot.Component.generic.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue

INDEX_SENSOR = 0
INDEX_SPEED = 1


class Msg_servoStatus(RemoteMessage):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterServoStatus]]

    def __init__(self, id: int = LegControllerProtocol.MSG_SERVO_STATUS):
        super().__init__(id, "msg_servoStatus", "actual servo status")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoStatus("status", "servo status"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            is_on: bool = None, is_active: bool = None, is_reverse: bool = None,
            is_at_min: bool = None, is_at_max: bool = None, is_stalling: bool = None,
    ) -> "Msg_servoStatus":
        cmd = Msg_servoStatus(id)
        if None not in [
            index, is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling
        ]:
            cmd.set_data(index, is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_speed(self):
        return self._parameter_list[INDEX_SPEED].get_value()

    def set_data(
            self, index: int,
            is_on: bool, is_active: bool, is_reverse: bool, is_at_min: bool, is_at_max: bool, is_stalling: bool
    ) -> None:
        self._parameter_list[INDEX_SPEED].set_on(is_on)
        self._parameter_list[INDEX_SPEED].set_active(is_active)
        self._parameter_list[INDEX_SPEED].set_reverse(is_reverse)
        self._parameter_list[INDEX_SPEED].set_at_min(is_at_min)
        self._parameter_list[INDEX_SPEED].set_at_max(is_at_max)
        self._parameter_list[INDEX_SPEED].set_stalling(is_stalling)
