from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

 
class Cmd_getComponentValue(RemoteCommand):
	
	_index = 0

	def __init__(self, id):
		super().__init__(id, "getComponentValue","get component value")
		self._parameter_list.append(RemoteParameterUint8("index","component index"))
		pass

	def set_index(self, index):
		self._parameter_list[self._index].set_value(index)

	def get_index(self):
		return self._parameter_list[self._index].get_value()


	def get_command(id, index):
		cmd = Cmd_getComponentValue(id)
		cmd.set_index(index)

		return (cmd)
