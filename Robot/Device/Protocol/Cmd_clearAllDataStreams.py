from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

class Cmd_clearAllDataStreams(RemoteCommand):
	
	def __init__(self):
		super().__init__(DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS, "clearAllStreams","clear all data streams on device")


	def get_command():
		cmd = Cmd_clearAllDataStreams()
		return (cmd)