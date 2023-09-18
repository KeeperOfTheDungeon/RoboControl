from typing import List

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8


class Cmd_getActorValue(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]
    _index = 0

    def __init__(self, id: int = 0x0):
        # WIP what is the default id for ACTOR_VALUE?
        super().__init__(id, "getActorValue", "get actors value")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[self._index].set_value(index)

    def get_index(self):
        return self._parameter_list[self._index].get_value()

    @staticmethod
    def get_command(id, index):
        cmd = Cmd_getActorValue()
        cmd.set_id(id)
        cmd.set_index(index)
        return cmd
