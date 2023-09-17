from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_pauseAllDataStreams(RemoteCommand):

    def __init__(self):
        super().__init__(DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS, "pauseAllStreams",
                         "pause all active streams on device")

    def get_command():
        cmd = Cmd_pauseAllDataStreams()

        return (cmd)
