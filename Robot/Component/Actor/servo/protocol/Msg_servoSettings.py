from typing import List, Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.RemoteParameter import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoFlags import RemoteParameterServoFlags
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoStatus import RemoteParameterServoStatus


INDEX_SENSOR = 0
INDEX_MIN_RANGE = 1
INDEX_MAX_RANGE = 2
INDEX_OFFSET = 3
INDEX_SCALE = 4
INDEX_FLAGS = 5


class Msg_servoSettings(RemoteMessage):
    _parameter_list: List[
        Union[
            RemoteParameterUint8, RemoteParameterUint16,
            RemoteParameterServoPosition, RemoteParameterServoFlags,
        ]
    ]  # RemoteParameterServoStatus

    def __init__(self, id: int = LegControllerProtocol.MSG_SERVO_SETTINGS):
        super().__init__(id, "servoSettings", "actual servo settings")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("min range", "servo min range"))
        self._parameter_list.append(RemoteParameterServoPosition("max range", "servo max range"))
        self._parameter_list.append(RemoteParameterUint16("offset", "servo offset"))
        self._parameter_list.append(RemoteParameterUint16("scale", "servo scale"))
        self._parameter_list.append(RemoteParameterServoFlags())
        # self._parameter_list.append(RemoteParameterServoStatus("scale", "servo scale"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, min_range: float = None, max_range: float = None,
            offset: int = None, scale: int = None, reverse: bool = None
    ):
        cmd = Msg_servoSettings(id)
        if None not in [index, min_range, max_range, offset, scale, reverse]:
            cmd.set_data(index, min_range, max_range, offset, scale, reverse)
        return cmd

    def set_data(self,
                 index: int, min_range: float, max_range: float, offset: int, scale: int, reverse: bool
                 ):
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[INDEX_MIN_RANGE].set_position(min_range)
        self._parameter_list[INDEX_MAX_RANGE].set_position(max_range)
        self._parameter_list[INDEX_OFFSET].set_value(offset)
        self._parameter_list[INDEX_SCALE].set_value(scale)
        self._parameter_list[INDEX_FLAGS].set_reverse(reverse)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_min_range(self) -> float:
        return self._parameter_list[INDEX_MIN_RANGE].get_position()

    def get_max_range(self) -> float:
        return self._parameter_list[INDEX_MAX_RANGE].get_position()

    def get_offset(self) -> int:
        return self._parameter_list[INDEX_OFFSET].get_value()

    def get_scale(self) -> int:
        return self._parameter_list[INDEX_SCALE].get_value()

    def is_reverse(self) -> bool:
        return self._parameter_list[INDEX_FLAGS].is_reverse()

    def is_on(self) -> bool:
        return self._parameter_list[INDEX_FLAGS].is_on()

    def is_force_feedback_on(self) -> bool:
        return self._parameter_list[INDEX_FLAGS].is_force_feedback_on()

    def is_position_feedback_on(self) -> bool:
        return self._parameter_list[INDEX_FLAGS].is_position_feedback_on()
