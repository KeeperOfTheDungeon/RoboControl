from typing import List

from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

INDEX_TTL = 0


class Msg_pingResponse(RemoteMessage):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = DeviceProtocol.MSG_PING_RESPONSE):
        super().__init__(id, "pingResponse", "response to a ping command")
        self._parameter_list.append(RemoteParameterUint8("ttl", "time to live"))

    @staticmethod
    def get_command(id: int, ttl: int = None) -> "Msg_pingResponse":
        res = Msg_pingResponse(id)
        if ttl is not None:
            res.set_data(ttl)
        return res

    def get_ttl(self):
        return self._parameter_list[INDEX_TTL].get_value()

    def set_data(self, node_type: int) -> None:
        self._parameter_list[INDEX_TTL].set_value(node_type)
