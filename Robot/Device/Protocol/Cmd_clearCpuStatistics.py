from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

class Cmd_clearCpuStatistics(RemoteCommand):
	
	def __init__(self, id):
		super().__init__("id, clearCpuStatistics", "clear device cpu statistic")


	def get_command():
		cmd = Cmd_clearCpuStatistics()
		return (cmd)
