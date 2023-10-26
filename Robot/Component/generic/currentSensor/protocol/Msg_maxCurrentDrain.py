from typing import Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint16
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage

SENSOR_INDEX = 0
SENSOR_CURRENT = 1


class Msg_maxCurrentDrain(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int = LegControllerProtocol.MSG_CURRENT_MAX_VALUE):
        super().__init__(id, "Msg_maxCurrentDrain", "maximal current drain measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "current sensor index"))
        self._parameter_list.append(RemoteParameterUint16("drain", "maximal current drain measured by this sensor"))

    @staticmethod
    def get_command(id: int) -> "Msg_maxCurrentDrain":
        cmd = Msg_maxCurrentDrain(id)
        return cmd

    def get_index(self) -> int:
        return self._parameter_list[SENSOR_INDEX].get_value()

    def get_max_current(self) -> int:
        return self._parameter_list[SENSOR_CURRENT].get_value()
