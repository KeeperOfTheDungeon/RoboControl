from typing import Union

from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Robot.Component.Sensor.vcnl4000 import Vcnl4000DistanceSensor
from RoboControl.Robot.Component.Sensor.vcnl4000.DistanceTable import DistanceTable

INDEX_SENSOR = 0


class Cmd_setVcnl4000DistanceTable(RemoteCommand):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int):
        super().__init__(id, "setVcnl4000DistanceTable", "entrys for a VCNL4000 Sensor distance table")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            self._parameter_list.append(RemoteParameterUint8(f"distance{i}", "distance point"))
            self._parameter_list.append(RemoteParameterUint16(f"value{i}", "proximity value"))

    @staticmethod
    def get_command(id: int, index: int = None, distances: DistanceTable = None) -> "Cmd_setVcnl4000DistanceTable":
        cmd = Cmd_setVcnl4000DistanceTable(id)
        if None not in [index, distances]:
            cmd.set_data(index, distances)
        return cmd

    def set_data(self, index: int, distances: DistanceTable) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            offset = (i * 2)
            self._parameter_list[offset + 1].set_value(distances.get_Distance(index))
            self._parameter_list[offset + 2].set_value(distances.get_proximity_value(index))

    def get_distance_table(self) -> DistanceTable:
        distances = DistanceTable()
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            offset = (i * 2)
            distance = self._parameter_list[offset + 1].get_value()
            proximity = self._parameter_list[offset + 2].get_value()
            distances.set_proximity_point(i, distance, proximity)
        return distances

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
