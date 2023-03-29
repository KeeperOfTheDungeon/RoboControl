from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

class Cmd_getNextError(RemoteCommand):
	
	def __init__(self):
		super().__init__("getNextError", "get next error from error queue")


	def get_command():
		cmd = Cmd_getNextError()
		cmd.set_id(DeviceProtocol.CMD_GET_NEXT_ERROR)

		return (cmd)
