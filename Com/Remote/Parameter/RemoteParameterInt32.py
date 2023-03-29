from RoboControl.Com.Remote.Parameter.RemoteParameterInt import RemoteParameterInt


class RemoteParameterInt32(RemoteParameterInt):

	def __init__(self, name, description):
		super().__init__(name, description,  -0x80000000, 0x7fffffff, 4)


	def put_data(self, data_buffer):
		data_buffer.append(self._value + 0x80000000 )	


	def parse_from_buffer(self ,data_buffer ,index):
		
		self._value = data_buffer[index] 	<< 24
		self._value |= data_buffer[index+1] << 16
		self._value |= data_buffer[index+2] << 8
		self._value |= data_buffer[index+3]

		self._value -= 0x80000000
		return self._byte_size
