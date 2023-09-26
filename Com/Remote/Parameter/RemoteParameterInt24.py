from RoboControl.Com.Remote.Parameter.RemoteParameterInt import RemoteParameterInt


class RemoteParameterInt24(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, -0x800000, 0x7fffff, 3)

    def put_data(self, data_buffer):
        data_buffer.append(self._value + 0x800000)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index + 1] << 16
        self._value |= data_buffer[index + 2] << 8
        self._value |= data_buffer[index + 3]

        self._value -= 0x800000
        return self._byte_size
