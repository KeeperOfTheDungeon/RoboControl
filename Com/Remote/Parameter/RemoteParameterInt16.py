from RoboControl.Com.Remote.Parameter.RemoteParameterInt import RemoteParameterInt


class RemoteParameterInt16(RemoteParameterInt):

	def __init__(self, name, description):
		super().__init__(name, description,  -0x8000, 0x7fff, 2)


	def put_data(self, data_buffer):
		data_buffer.append(self._value + 0x8000 )	


	def parse_from_buffer(self ,data_buffer ,index):

		self._value = data_buffer[index] << 8
		self._value |= data_buffer[index+1]
		
		self._value -= 0x8000
		return self._byte_size
