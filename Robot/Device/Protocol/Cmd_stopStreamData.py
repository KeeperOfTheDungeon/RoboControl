from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

class Cmd_stopStreamData(RemoteCommand):
	
	def __init__(self):
		super().__init__(DeviceProtocol.CMD_STOP_STREAM_DATA, "stopStreamData","stop streaming data")
		self._type_index = 0
		self._parameter_list.append(RemoteParameterUint8("index", "stream index"))



	def set_type(self, type):
		self._parameter_list[self._type_index].set_value(type)

	def get_command(type):
		cmd = Cmd_stopStreamData()
		cmd.set_type(type)

		return (cmd)