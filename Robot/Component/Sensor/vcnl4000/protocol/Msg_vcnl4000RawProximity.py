from typing import Union

from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage

INDEX_SENSOR = 0
INDEX_PROXIMITY_VALUE = 1


class Msg_vcnl4000RawProximity(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int):
        super().__init__(id, "proximity", "VCNL 4000 raw proximity value")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        self._parameter_list.append(RemoteParameterUint16("proximity", "proximity value"))

    @staticmethod
    def get_command(id: int, index: int = None, value: int = None) -> "Msg_vcnl4000RawProximity":
        cmd = Msg_vcnl4000RawProximity(id)
        if None not in [index, value]:
            cmd.set_data(index, value)
        return cmd

    def set_data(self, index: int, value: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[INDEX_PROXIMITY_VALUE].set_value(value)

    def get_proximity_value(self) -> int:
        return self._parameter_list[INDEX_PROXIMITY_VALUE].get_value()

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
