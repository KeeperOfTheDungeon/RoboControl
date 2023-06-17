from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand

INDEX_TTL = 0


class Cmd_ping(RemoteCommand):
    def __init__(self, id: int):
        super().__init__(id, "ping", " send ping")
        self._parameter_list.append(RemoteParameterUint8("ttl", "time to live"))

    def set_ttl(self, ttl):
        self._parameter_list[INDEX_TTL].set_value(ttl)

    @staticmethod
    def get_command(id: int):
        cmd = Cmd_ping(id)
        cmd.set_ttl(10)
        return cmd
