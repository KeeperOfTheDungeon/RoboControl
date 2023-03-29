from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

class Cmd_saveDataStreams(RemoteCommand):
	
	def __init__(self):
		super().__init__(DeviceProtocol.CMD_SAVE_STREAMS,"clearAllStreams","clear all data streams on device")


	def get_command():
		cmd = Cmd_saveDataStreams()

		return (cmd)