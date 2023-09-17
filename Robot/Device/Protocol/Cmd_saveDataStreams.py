from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_saveDataStreams(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_SAVE_STREAMS):
        super().__init__(id, "clearAllStreams", "clear all data streams on device")

    @staticmethod
    def get_command():
        return Cmd_saveDataStreams()
