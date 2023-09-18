from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_getErrorCount(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_GET_ERROR_COUNT):
        super().__init__(id, "getErrorCounts", "get count of errors on device")

    @staticmethod
    def get_command():
        cmd = Cmd_getErrorCount()
        cmd.set_id(DeviceProtocol.CMD_GET_ERROR_COUNT)
        return cmd
