

from RoboControl.Com.RemoteData import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8

INDEX_TYPE = 0


class Cmd_getComponentSettings(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id):
        super().__init__(id, "getComponentSettings", "get components active settings")
        self._parameter_list.append(RemoteParameterUint8("index", "component index"))

    def set_index(self, index):
        self._parameter_list[INDEX_TYPE].set_value(index)

    def get_index(self):
        return self._parameter_list[INDEX_TYPE].get_value()

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_getComponentSettings(id)
        cmd.set_index(local_id)
        return cmd
    


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
	

    
class Cmd_saveComponentDefaults(RemoteCommand):
	
	_index = 0

	def __init__(self, id):
		super().__init__(id, "saveComponentDefaults","save components defaults to non volatile memory")
		self._parameter_list.append(RemoteParameterUint8("index","component index"))

		pass

	def set_index(self, index):
		self._parameter_list[self._index].set_value(index)

	def get_index(self):
		return self._parameter_list[self._index].get_value()


	def get_command(id, local_id):
		cmd = Cmd_saveComponentDefaults(id)
		cmd.set_index(local_id)

		return (cmd)