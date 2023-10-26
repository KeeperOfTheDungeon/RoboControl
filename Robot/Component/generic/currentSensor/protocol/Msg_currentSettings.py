from typing import Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint8, RemoteParameterUint16
from RoboControl.Com.RemoteData import RemoteMessage

INDEX_SENSOR = 0
INDEX_WINDOW_SIZE = 1
INDEX_THRESHOLD = 2


class Msg_currentSettings(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int = LegControllerProtocol.MSG_CURRENT_SETTINGS):
        super().__init__(id, "Msg_maxCurrentDrain", "maximal current drain measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterUint8("window size", "current sensor data window size"))
        self._parameter_list.append(RemoteParameterUint16("threshold", "current sensor threshold"))

    @staticmethod
    def get_command(id: int) -> "Msg_currentSettings":
        cmd = Msg_currentSettings(id)
        return cmd

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_window_size(self) -> int:
        return self._parameter_list[INDEX_WINDOW_SIZE].get_value()

    def get_threshold(self) -> int:
        return self._parameter_list[INDEX_THRESHOLD].get_value()
