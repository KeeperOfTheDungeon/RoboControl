from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.RemoteData import RemoteCommand

INDEX_SENSOR = 0


class Cmd_getMaximalCurrentDrain(RemoteCommand):
    _parameter_list: list[RemoteParameterUint8]

    def __init__(self, id: int = LegControllerProtocol.CMD_GET_MAXIMAL_CURRENT_DRAIN):
        super().__init__(id, "Cmd_getMaximalCurrentDrain", " get the higest current drain ever measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id: int, local_id: int) -> "Cmd_getMaximalCurrentDrain":
        cmd = Cmd_getMaximalCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
