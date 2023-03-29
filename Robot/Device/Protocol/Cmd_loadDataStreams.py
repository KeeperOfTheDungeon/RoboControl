from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

class Cmd_loadDataStreams(RemoteCommand):
	
	def __init__(self):
		super().__init__(DeviceProtocol.CMD_LOAD_STREAMS,"loadDataStreams","load saved device data Streams from nonvolatile memory")


	def get_command():
		cmd = Cmd_loadDataStreams()

		return (cmd)
