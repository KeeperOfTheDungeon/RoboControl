from RoboControl.Com.Remote.Parameter.RemoteParameterInt import RemoteParameterInt


class RemoteParameterUint32(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, 0, 0xffffffff, 4)

    def put_data(self, data_buffer):
        data_buffer.append((self._value & 0xff000000) >> 24)
        data_buffer.append((self._value & 0xff0000) >> 16)
        data_buffer.append((self._value & 0xff00) >> 8)
        data_buffer.append(self._value & 0xff)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index] << 24
        self._value |= data_buffer[index + 1] << 16
        self._value |= data_buffer[index + 2] << 8
        self._value |= data_buffer[index + 3]
        return self._byte_size
