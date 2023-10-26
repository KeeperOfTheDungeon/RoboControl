from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand

INDEX_SENSOR = 0


class Cmd_getTotalCurrentDrain(RemoteCommand):
    _parameter_list: list[RemoteParameterUint8]

    def __init__(self, id: int = LegControllerProtocol.CMD_GET_TOTAL_CURRENT_DRAIN):
        super().__init__(id, "Cmd_getTotalCurrentDrain", " get the total current drain ever measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id: int, local_id: int) -> "Cmd_getTotalCurrentDrain":
        cmd = Cmd_getTotalCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
