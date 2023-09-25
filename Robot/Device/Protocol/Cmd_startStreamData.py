# disabled for micropython  # from typing import List

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_startStreamData(RemoteCommand):
    _parameter_list: "List[RemoteParameterUint8]"

    def __init__(self, id: int = DeviceProtocol.CMD_START_STREAM_DATA):
        super().__init__(id, "startStreamData", "start streaming data")
        self._type_index = 0
        self._period_index = 1
        self._parameter_list.append(RemoteParameterUint8("type", "type of data (device dependent)"))
        self._parameter_list.append(RemoteParameterUint8("period", "period of in 10 ms steps"))

    def set_type(self, new_type):
        self._parameter_list[self._type_index].set_value(new_type)

    def set_period(self, new_period):
        self._parameter_list[self._period_index].set_value(new_period)

    def get_type(self) -> int:
        return self._parameter_list[self._type_index].get_value()

    def get_period(self) -> int:
        return self._parameter_list[self._period_index].get_value()

    @staticmethod
    def get_command(id: int, new_type: int = None, period: int = None) -> "Cmd_startStreamData":
        cmd = Cmd_startStreamData(id)
        if new_type:
            cmd.set_type(new_type)
        if period:
            cmd.set_period(period)
        return cmd
