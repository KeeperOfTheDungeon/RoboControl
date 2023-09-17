from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_loadDataStreams(RemoteCommand):
    def __init__(self, id: int = DeviceProtocol.CMD_LOAD_STREAMS):
        super().__init__(id, "loadDataStreams", "load saved device data Streams from nonvolatile memory")

    @staticmethod
    def get_command():
        return Cmd_loadDataStreams()
