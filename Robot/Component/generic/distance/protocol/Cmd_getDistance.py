from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SENSOR = 0

class Cmd_getDistance(RemoteCommand):
	
	def __init__(self, id):
		super().__init__(id,"Cmd_getDistance","get measured distance from a distance sensor")
		self._ttl_index = 0
		self._parameter_list.append(RemoteParameterUint8("index","sensor index"))



	def set_index(self, index):
		self._parameter_list[INDEX_SENSOR].set_value(index)



	def get_command(id, local_id):
		cmd = Cmd_getDistance(id)
		cmd.set_index(local_id)

		return (cmd)
