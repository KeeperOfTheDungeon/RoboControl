

from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage


SENSOR_INDEX 		= 0
WINDOW_SIZE_INDEX	= 1
THRESHOLD_INDEX 	= 2

class Msg_currentSettings(RemoteMessage):

	def __init__(self, id):
		super().__init__(id, "Msg_maxCurrentDrain", "maximal current drain measured by this sensor")

		self._parameter_list.append(RemoteParameterUint8("index","sensor index"))
		self._parameter_list.append(RemoteParameterUint8("window size","current sensor data window size"))
		self._parameter_list.append(RemoteParameterUint16("threshold","current sensor threshold"))

	def get_command(id):
		cmd = Msg_currentSettings(id)
		return (cmd)


	def get_index(self):
		return self._parameter_list[SENSOR_INDEX].get_value()


	def get_window_size(self):
		return self._parameter_list[WINDOW_SIZE_INDEX].get_value()
		

	def get_threshold(self):
		return self._parameter_list[THRESHOLD_INDEX].get_value()
		
