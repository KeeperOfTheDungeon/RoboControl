from typing import List

from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

NODE_TYPE = 0


class Msg_nodeType(RemoteMessage):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = DeviceProtocol.MSG_PING_RESPONSE):
        super().__init__(id, "nodeType", "type of a node")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("type", "type of a node"))

    @staticmethod
    def get_command(id: int, node_type: int = None) -> "Msg_nodeType":
        res = Msg_nodeType(id)
        if node_type is not None:
            res.set_data(node_type)
        return res

    def get_node_type(self):
        return self._parameter_list[NODE_TYPE].get_value()

    def set_data(self, node_type: int) -> None:
        self._parameter_list[NODE_TYPE].set_value(node_type)
