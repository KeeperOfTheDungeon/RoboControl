from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_clearComStatistics(RemoteCommand):
	
	def __init__(self, id: int = DeviceProtocol.CMD_CLEAR_COM_STATISTICS):
		super().__init__(id, "clearComStatistics", "clear device comunication statistic")

	@staticmethod
	def get_command():
		return Cmd_clearComStatistics()
