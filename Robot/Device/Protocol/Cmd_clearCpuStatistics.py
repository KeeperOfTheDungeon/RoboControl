from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_clearCpuStatistics(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_CLEAR_CPU_STATISTICS):
        super().__init__(id, "clearCpuStatistics", "clear device cpu statistic")

    @staticmethod
    def get_command() -> "Cmd_clearCpuStatistics":
        return Cmd_clearCpuStatistics()
