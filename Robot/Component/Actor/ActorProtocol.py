from RoboControl.Com.RemoteData import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Component.ComponentProtocol import ComponentProtocol


class ActorProtocol(ComponentProtocol):
    def __init__(self, protocol):
        super().__init__(protocol)
        self._cmd_set_value_id = protocol["cmd_set_value_id"]
        self._cmd_get_value_id = protocol["cmd_get_value_id"]
        self._msg_value_id = protocol["msg_value_id"]
        self._stream_values_id = protocol["stream_values_id"]


class Cmd_getActorValue(RemoteCommand):
    _parameter_list = list()
    _index = 0

    def __init__(self, id: int):
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
