from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_stopStreamData(RemoteCommand):

    def __init__(self):
        super().__init__(DeviceProtocol.CMD_STOP_STREAM_DATA, "stopStreamData", "stop streaming data")
        self._type_index = 0
        self._parameter_list.append(RemoteParameterUint8("index", "stream index"))

    def set_type(self, new_type):
        self._parameter_list[self._type_index].set_value(new_type)

    @staticmethod
    def get_command(new_type):
        cmd = Cmd_stopStreamData()
        cmd.set_type(new_type)
        return cmd
