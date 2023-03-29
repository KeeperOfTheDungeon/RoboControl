from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8


class Cmd_clearComStatistics(RemoteCommand):
	
	def __init__(self, id):
		super().__init__("id, clearComStatistics", "clear device comunication statistic")


	def get_command():
		cmd = Cmd_clearComStatistics()
		return (cmd)
