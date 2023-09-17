from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_continueAllDataStreams(RemoteCommand):

    def __init__(self):
        super().__init__(DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS, "continueAllStreams", "continue all active streams on device")

    def get_command():
        cmd = Cmd_continueAllDataStreams()
        return (cmd)
