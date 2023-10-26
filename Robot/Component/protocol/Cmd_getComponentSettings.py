from typing import List

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8

INDEX_TYPE = 0


class Cmd_getComponentSettings(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id):
        super().__init__(id, "getComponentSettings", "get components active settings")
        self._parameter_list.append(RemoteParameterUint8("index", "component index"))

    def set_index(self, index):
        self._parameter_list[INDEX_TYPE].set_value(index)

    def get_index(self):
        return self._parameter_list[INDEX_TYPE].get_value()

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_getComponentSettings(id)
        cmd.set_index(local_id)
        return cmd
