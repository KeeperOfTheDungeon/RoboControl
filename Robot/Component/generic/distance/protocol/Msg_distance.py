from typing import Union

from RoboControl.Com.RemoteParameter import RemoteParameterUint24
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage

SENSOR_INDEX = 0
SENSOR_VALUE = 1


class Msg_distance(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint24]]

    def __init__(self, id: int):
        super().__init__(id, "distance", "actual distance measured by an distance sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterUint24("distance", "distance value in mm"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, distance: int = None
    ) -> "Msg_distance":
        cmd = Msg_distance(id)
        if None not in [index, distance]:
            cmd.set_data(index, distance)
        return cmd

    def get_index(self) -> int:
        return self._parameter_list[SENSOR_INDEX].get_value()

    def get_distance(self) -> int:
        return self._parameter_list[SENSOR_VALUE].get_value()

    def set_data(self, index: int, value: int) -> None:
        self._parameter_list[SENSOR_INDEX].set_value(index)
        self._parameter_list[SENSOR_VALUE].set_value(value)
