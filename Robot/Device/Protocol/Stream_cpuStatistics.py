from typing import List

from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteStream import RemoteStream

INDEX_MIN_CPU_LOAD = 0
INDEX_ACTUAL_CPU_LOAD = 1
INDEX_MAX_CPU_LOAD = 2
INDEX_CPU_STATUS = 3


class Stream_cpuStatistics(RemoteStream):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int):
        super().__init__(id, "cpuStatus", "status of the cpu containing values for min max and last cycle duration")

        self._parameter_list.append(RemoteParameterUint8("min", "min load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("max", "max load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("actual", "actual load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("status", "actual status of the device cpu"))

        self.set_id(id)

    def get_last_load(self):
        return self._parameter_list[INDEX_ACTUAL_CPU_LOAD].get_value()

    def get_min_load(self):
        return self._parameter_list[INDEX_MIN_CPU_LOAD].get_value()

    def get_max_load(self):
        return self._parameter_list[INDEX_MAX_CPU_LOAD].get_value()

    def set_data(self, min_load: int, max_load: int, current_load: int, status: int) -> None:
        self._parameter_list[INDEX_MIN_CPU_LOAD].set_value(min_load)
        self._parameter_list[INDEX_MAX_CPU_LOAD].set_value(max_load)
        self._parameter_list[INDEX_ACTUAL_CPU_LOAD].set_value(current_load)
        self._parameter_list[INDEX_CPU_STATUS].set_value(status)

    @staticmethod
    def get_command(
            id: int,
            min_load: int = None, max_load: int = None, current_load: int = None, status: int = None
    ):
        cmd = Stream_cpuStatistics(id)
        if min_load and max_load and current_load and status:
            cmd.set_data(min_load, max_load, current_load, status)
        return
