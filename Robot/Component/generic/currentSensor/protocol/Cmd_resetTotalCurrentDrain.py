from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand


INDEX_SENSOR = 0

class Cmd_resetTotalCurrentDrain(RemoteCommand):
	
	def __init__(self, id):
		super().__init__(id,"Cmd_resetMaximalCurrentDrain"," reset the total current drain measured by this sensor")
		self._ttl_index = 0
		self._parameter_list.append(RemoteParameterUint8("index","sensor index"))



	def set_index(self, index):
		self._parameter_list[INDEX_SENSOR].set_value(index)



	def get_command(id, local_id):
		cmd = Cmd_resetTotalCurrentDrain(id)
		cmd.set_index(local_id)

		return (cmd)
