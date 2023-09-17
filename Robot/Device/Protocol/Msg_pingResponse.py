from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

INDEX_TTL = 0


class Msg_pingResponse(RemoteMessage):

    def __init__(self):
        super().__init__(DeviceProtocol.MSG_PING_RESPONSE, "msgpingResponse", "response to a ping command")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("ttl", "time to live"))

    def get_command(id):
        cmd = Msg_pingResponse()
        return (cmd)

    def get_ttl(self):
        return self._parameter_list[INDEX_TTL].get_value()
