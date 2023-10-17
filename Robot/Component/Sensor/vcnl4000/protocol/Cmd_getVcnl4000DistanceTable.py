from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand

INDEX_SENSOR = 0


class Cmd_getVcnl4000DistanceTable(RemoteCommand):
    _parameter_list: list[RemoteParameterUint8]

    def __init__(self, id: int):
        super().__init__(id, "getVcnl4000DistanceTable", "get distance table for VCNL4000 sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_getVcnl4000DistanceTable":
        cmd = Cmd_getVcnl4000DistanceTable(id)
        if index is not None:
            cmd.set_data(index)
        return cmd

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
