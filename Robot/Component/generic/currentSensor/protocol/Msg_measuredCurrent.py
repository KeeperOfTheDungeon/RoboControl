from typing import Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint16, RemoteParameterUint8
from RoboControl.Com.RemoteData import RemoteMessage

INDEX_SENSOR = 0
INDEX_DRAIN = 1


class Msg_measuredCurrent(RemoteMessage):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int = LegControllerProtocol.MSG_CURRENT_VALUE):
        super().__init__(id, "currentDrain", "measured current drain by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "current sensor index"))
        self._parameter_list.append(RemoteParameterUint16("drain", "measured current drain by this sensor"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            max_drain: int = None,
    ) -> "Msg_measuredCurrent":
        cmd = Msg_measuredCurrent(id)
        if None not in [index, max_drain]:
            cmd.set_data(index, max_drain)
        return cmd

    def get_index(self) -> int:
        """ "get sensor index for sensor corresponding to this message" """
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_current(self) -> int:
        return self._parameter_list[INDEX_DRAIN].get_value()

    def get_drain(self) -> int:
        return self._parameter_list[INDEX_DRAIN].get_value()

    def set_data(self, index: int, max_drain: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[INDEX_DRAIN].set_value(max_drain)
