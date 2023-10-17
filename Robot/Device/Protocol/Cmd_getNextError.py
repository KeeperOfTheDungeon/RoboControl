from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_getNextError(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_GET_NEXT_ERROR):
        super().__init__(id, "getNextError", "get next error from error queue")

    @staticmethod
    def get_command():
        return Cmd_getNextError()
