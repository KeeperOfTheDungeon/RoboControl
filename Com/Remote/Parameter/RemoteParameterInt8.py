
from RoboControl.Com.Remote.Parameter.RemoteParameterInt import RemoteParameterInt


class RemoteParameterInt8(RemoteParameterInt):

	def __init__(self, name, description):
		super().__init__(name, description,  -128, 127, 1)


	def put_data(self, data_buffer):
		data_buffer.append(self._value +128 )	


	def parse_from_buffer(self ,data_buffer ,index):

		self._value = data_buffer[index] -128
		return self._byte_size

	def get_as_buffer(self):
		buffer = bytearray(self._byte_size)
		buffer[0] = self._value
		
		return buffer