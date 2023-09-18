from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoFlags import RemoteParameterServoFlags
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition

INDEX_SERVO = 0
INDEX_MIN_RANGE = 1
INDEX_MAX_RANGE = 2
INDEX_OFFSET = 3
INDEX_SCALE = 4
INDEX_FLAGS = 5


class Cmd_setServoSettings(RemoteCommand):
    """
    "command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor"
    """
    _parameter_list: List[
        RemoteParameterUint8 | RemoteParameterServoPosition | RemoteParameterUint16 | RemoteParameterServoFlags]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_ON):
        super().__init__(id, "cmd_setServoSettings", "set settings for a servo")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("min range", "servo min range"))
        self._parameter_list.append(RemoteParameterServoPosition("max range", "servo max range"))
        self._parameter_list.append(RemoteParameterUint16("offset", "servo offset"))
        self._parameter_list.append(RemoteParameterUint16("scale", "servo scale"))
        self._parameter_list.append(RemoteParameterServoFlags())

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        """ "get sensor index for sensor corresponding to this message" """
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_min_range(self) -> float:
        return self._parameter_list[INDEX_MIN_RANGE].get_position()

    def get_max_range(self) -> float:
        return self._parameter_list[INDEX_MAX_RANGE].get_position()

    def get_offset(self) -> int:
        return self._parameter_list[INDEX_OFFSET].get_value()

    def is_reverse(self) -> bool:
        return self._parameter_list[INDEX_FLAGS].is_reverse()

    def set_data(
            self, min_range: float, max_range: float, offset: int, scale: float, reverse: bool
    ) -> None:
        self._parameter_list[INDEX_MIN_RANGE].set_position(min_range)
        self._parameter_list[INDEX_MAX_RANGE].set_position(max_range)
        self._parameter_list[INDEX_OFFSET].set_value(offset)
        self._parameter_list[INDEX_SCALE].set_value(scale)
        self._parameter_list[INDEX_FLAGS].set_reverse(reverse)

    @staticmethod
    def get_command(id: int, local_id, *args) -> "Cmd_setServoSettings":
        cmd = Cmd_setServoSettings(id)
        cmd.set_index(local_id)
        if args:
            cmd.set_data(*args)
        return cmd
