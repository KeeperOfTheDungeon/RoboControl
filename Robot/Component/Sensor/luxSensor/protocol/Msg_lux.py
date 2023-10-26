from typing import List, Union

from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Sensor.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue

INDEX_SENSOR = 0
INDEX_LUX = 1


class Msg_lux(RemoteMessage):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterLuxValue]]

    def __init__(self, id: int):
        super().__init__(id, "luxValue", "actual lux value measured by a light sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterLuxValue("distance", "light value in lux"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, distance: int = None,
    ) -> "Msg_lux":
        cmd = Msg_lux(id)
        if None not in [index, distance]:
            cmd.set_data(index, distance)
        return cmd

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_lux_value(self) -> float:
        return self._parameter_list[INDEX_LUX].get_value()

    def set_data(self, index: int, value: float) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[INDEX_LUX].set_value(value)
