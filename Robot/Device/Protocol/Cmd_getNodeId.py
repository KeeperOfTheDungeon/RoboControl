from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

INDEX_TTL = 0


class Cmd_getNodeId(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "getNodeId", "get destinations node id")

    @staticmethod
    def get_command(id: int):
        cmd = Cmd_getNodeId(id)
        cmd.set_id(DeviceProtocol.CMD_GET_NODE_ID)
        return cmd
