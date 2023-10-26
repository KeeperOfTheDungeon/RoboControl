from typing import Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint32
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage

SENSOR_INDEX = 0
SENSOR_CURRENT = 1


class Msg_totalCurrentDrain(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint32]]

    def __init__(self, id: int = LegControllerProtocol.MSG_CURRENT_TOTAL_CONSUMPTION):
        super().__init__(id, "Msg_totalCurrentDrain", "total current amount measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "current sensor index"))
        self._parameter_list.append(RemoteParameterUint32("drain", "total current amount measured by this sensor"))

    @staticmethod
    def get_command(id: int) -> "Msg_totalCurrentDrain":
        cmd = Msg_totalCurrentDrain(id)
        return cmd

    def get_index(self) -> int:
        return self._parameter_list[SENSOR_INDEX].get_value()

    def get_total(self) -> int:
        return self._parameter_list[SENSOR_CURRENT].get_value()
