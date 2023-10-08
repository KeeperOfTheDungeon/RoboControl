from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_saveDataStreams(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_SAVE_STREAMS):
        super().__init__(id, "saveDataStreams", "save device actuals data Streams to non volatile memory")

    @staticmethod
    def get_command(id: int = DeviceProtocol.CMD_SAVE_STREAMS):
        return Cmd_saveDataStreams(id)
