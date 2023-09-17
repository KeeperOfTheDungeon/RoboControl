from typing import List

from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand

INDEX_TYPE = 0


class Cmd_setDeviceState(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]
    # FIXME false java file?

    def __init__(self, id: int):
        super().__init__(id, "setDeviceState", "set device state")
        self._parameter_list.append(RemoteParameterUint8("type", "type of data (device dependent)"))

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_setDeviceState":
        cmd = Cmd_setDeviceState(id)
        if index:
            cmd.set_data(index)
        return cmd

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_TYPE].set_value(index)

    def get_type(self) -> int:
        return self._parameter_list[INDEX_TYPE].get_value()
