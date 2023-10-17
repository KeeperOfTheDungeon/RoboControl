from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand

INDEX_SENSOR = 0


class Cmd_getVcnl4000RawProximity(RemoteCommand):
    _parameter_list: list[RemoteParameterUint8]

    def __init__(self, id: int):
        # name = "setMpu9150Settings" # description = "set settings for a mpu9150Sensor"
        super().__init__(id, "getProximity", "get VCNL 4000 raw proximity value")
        # RemoteParameterUint8("index","mpu9150 sensor index")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_getVcnl4000RawProximity":
        cmd = Cmd_getVcnl4000RawProximity(id)
        if index is not None:
            cmd.set_data(index)
        return cmd

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
