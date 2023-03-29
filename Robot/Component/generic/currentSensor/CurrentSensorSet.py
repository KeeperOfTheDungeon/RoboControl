
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.generic.currentSensor.CurrentSensor import CurrentSensor
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_currentSettings import Msg_currentSettings
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_maxCurrentDrain import Msg_maxCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_measuredCurrent import Msg_measuredCurrent
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_totalCurrentDrain import Msg_totalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Stream_actualConsumption import Stream_actualConsumption
from RoboControl.Robot.Component.generic.currentSensor.protocol.Stream_maxConsumption import Stream_maxConsumption
from RoboControl.Robot.Component.generic.currentSensor.protocol.Stream_totalConsumption import Stream_totalConsumption
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor


class CurrentSensorSet(ComponentSet):
	def __init__(self, components, protocol):

	
	#	self._cmd_get_actual_current = protocol['cmd_getActualCurrent']
	
	#	self._cmd_get_max_current = protocol['cmd_getMaxCurrent']
	#	self._cmd_reset_max_current = protocol['cmd_resetMaxCurrent']

	#	self._cmd_get_total_current = protocol['cmd_getTotalCurrent']
	#	self._cmd_reset_total_current = protocol['cmd_resetTotalCurrent']


		self._msg_actual_current = protocol['msg_actualCurrent']
		self._msg_max_current = protocol['msg_maxCurrent']
		self._msg_total_current = protocol['msg_totalCurrent']

		self._stream_actual_current = protocol['stream_actualCurrent']
		self._stream_max_current = protocol['stream_maxCurrent']
		self._stream_total_current = protocol['stream_totalCurrent']


		sensors = list()
 
		for component in components:
			sensor = CurrentSensor(component)
			sensors.append(sensor)

		super().__init__(sensors)

	def get_command_processors(self):
		command_list = super().get_command_processors()
		return command_list

	def get_message_processors(self):
		msg_list = super().get_message_processors()

		if (self._msg_actual_current != 0):
			msg_list.append(RemoteProcessor(Msg_measuredCurrent.get_command(self._msg_actual_current), self.process_msg_current))

		if (self._msg_max_current != 0):
			msg_list.append(RemoteProcessor(Msg_maxCurrentDrain.get_command(self._msg_max_current), self.process_msg_max_current))

		if (self._msg_total_current != 0):
			msg_list.append(RemoteProcessor(Msg_totalCurrentDrain.get_command(self._msg_total_current), self.process_msg_total_current))

		if (self._msg_total_current != 0):
			msg_list.append(RemoteProcessor(Msg_currentSettings.get_command(self._msg_total_current), self.process_settings))


		return msg_list


	def get_stream_processors(self):
		stream_list = super().get_stream_processors()
		
		if (self._stream_actual_current != 0):
			stream_list.append(RemoteProcessor(Stream_actualConsumption.get_command(self._stream_actual_current, len(self)), self.process_stream_actual))

		if (self._stream_max_current != 0):
			stream_list.append(RemoteProcessor(Stream_maxConsumption.get_command(self._stream_max_current, len(self)), self.process_stream_max))


		if (self._stream_total_current != 0):
			stream_list.append(RemoteProcessor(Stream_totalConsumption.get_command(self._stream_total_current, len(self)), self.process_stream_total))



		return stream_list



	def process_stream_actual(self, stream_positions):
		
		for sensor in self:
			index = sensor.get_local_id()
			value = stream_positions.get_actual_consumption(index)

			sensor.set_actual(value)



	def process_stream_max(self, stream_positions):
		
		for sensor in self:
			index = sensor.get_local_id()
			value = stream_positions.get_max_consumption(index)

			sensor.set_max(value)


	def process_stream_total(self, stream_positions):
		
		for sensor in self:
			index = sensor.get_local_id()
			value = stream_positions.get_total_consumption(index)

			sensor.set_total(value)



	def process_msg_current(self, remote_data):
		index = remote_data.get_index()
		value = remote_data.get_current()
		
		if index < len(self):
			self[index].set_actual(value) 



	def process_msg_max_current(self, remote_data):
		index = remote_data.get_index()
		value = remote_data.get_max_current()
		
		if index < len(self):
			self[index].set_max(value) 
		

	def process_msg_total_current(self, remote_data):
		index = remote_data.get_index()
		value = remote_data.get_max_current()
		
		if index < len(self):
			self[index].get_total(value) 

	def process_settings(self, remote_data):
		pass