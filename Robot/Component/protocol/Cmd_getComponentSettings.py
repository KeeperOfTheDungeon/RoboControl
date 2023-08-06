from typing import List

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8


class Cmd_getComponentSettings(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]
    _index = 0

    def __init__(self, id):
        super().__init__(id, "getComponentSettings", "get components active settings")
        self._parameter_list.append(RemoteParameterUint8("index", "component index"))

    def set_index(self, index):
        self._parameter_list[self._index].set_value(index)

    def get_index(self):
        return self._parameter_list[self._index].get_value()

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_getComponentSettings(id)
        cmd.set_index(local_id)
        return cmd
