
from RoboControl.Com.Remote.Parameter.RemoteParameterInt import RemoteParameterInt


class RemoteParameterUint8(RemoteParameterInt):

	def __init__(self, name, description):
		super().__init__(name, description, 0,0xff, 1)



	def put_data(self, data_buffer):
		data_buffer.append(self._value)	


	def parse_from_buffer(self ,data_buffer ,index):

		self._value = data_buffer[index]
		return self._byte_size

	def get_as_buffer(self):
		buffer = bytearray(self._byte_size)
		buffer[0] = self._value
		
		return buffer