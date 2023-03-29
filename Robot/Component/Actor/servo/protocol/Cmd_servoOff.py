from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SERVO = 0

class Cmd_servoOff(RemoteCommand):
	
	def __init__(self, id):
		super().__init__(id,"cmd_servoOff"," switch servo off")
		self._ttl_index = 0
		self._parameter_list.append(RemoteParameterUint8("index","servo index"))



	def set_index(self, index):
		self._parameter_list[INDEX_SERVO].set_value(index)



	def get_command(id, local_id):
		cmd = Cmd_servoOff(id)
		cmd.set_index(local_id)

		return (cmd)
