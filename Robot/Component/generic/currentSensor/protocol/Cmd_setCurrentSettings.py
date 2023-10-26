from RoboControl.Com.RemoteParameter import RemoteParameterUint16
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand


INDEX_SENSOR 		= 0
INDEX_WINDOW_SIZE	= 1
INDEX_THRESHOLD 	= 2

class Cmd_setCurrentSettings(RemoteCommand):
	
	def __init__(self, id):
		super().__init__(id,"Cmd_setCurrentSettings","set settings for a Current Sensor")
		self._parameter_list.append(RemoteParameterUint8("index","sensor index"))
		self._parameter_list.append(RemoteParameterUint8("window size","current sensor data window size"))
		self._parameter_list.append(RemoteParameterUint16("threshold","current sensor threshold"))



	def set_index(self, index):
		self._parameter_list[INDEX_SENSOR].set_value(index)


	def set_window_size(self, window_size):
		self._parameter_list[INDEX_WINDOW_SIZE].set_value(window_size)


	def set_threshold(self, threshold):
		self._parameter_list[INDEX_THRESHOLD].set_value(threshold)



	def get_command(id, local_id, window_size, threshold):
		cmd = Cmd_setCurrentSettings(id)
		cmd.set_window_size(window_size)
		cmd.set_threshold(threshold)
		cmd.set_index(local_id)

		return (cmd)
