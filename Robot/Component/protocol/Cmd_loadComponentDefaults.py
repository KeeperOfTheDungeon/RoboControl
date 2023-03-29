from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8


class Cmd_loadComponentDefaults(RemoteCommand):
	
	_index = 0

	def __init__(self, id):
		super().__init__(id, "loadComponentDefaults","load components defaults from non volatile memory")
		self._parameter_list.append(RemoteParameterUint8("index","component index"))

		pass

	def set_index(self, index):
		self._parameter_list[self._index].set_value(index)

	def get_index(self):
		return self._parameter_list[self._index].get_value()


	def get_command(id, local_id):
		cmd = Cmd_loadComponentDefaults(id)
		cmd.set_index(local_id)

		return (cmd)

