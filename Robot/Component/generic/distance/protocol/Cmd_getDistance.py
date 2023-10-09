from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SENSOR = 0


class Cmd_getDistance(RemoteCommand):
    _parameter_list: list[RemoteParameterUint8]

    def __init__(self, id: int):
        super().__init__(id, "Cmd_getDistance", "get measured distance from a distance sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id: int, local_id: int) -> "Cmd_getDistance":
        cmd = Cmd_getDistance(id)
        cmd.set_index(local_id)
        return cmd
