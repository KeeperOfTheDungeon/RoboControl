from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_pauseAllDataStreams(RemoteCommand):
    def __init__(self, id: int = DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS):
        super().__init__(id, "pauseAllStreams", "pause all active streams on device")

    @staticmethod
    def get_command():
        return Cmd_pauseAllDataStreams()
