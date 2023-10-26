from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_clearAllDataStreams(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS):
        super().__init__(id, "clearAllStreams", "clear all data streams on device")

    @staticmethod
    def get_command():
        return Cmd_clearAllDataStreams()
