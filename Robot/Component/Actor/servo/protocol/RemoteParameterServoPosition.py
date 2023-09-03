from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter


class RemoteParameterServoPosition(RemoteParameter):

    def __init__(self, name, description):
        super().__init__(name, description, 2)
        self._value = 0

    def set_position(self, position):
        self._value = position

    def get_position(self):
        return self._value

    def parse_from_buffer(self, data_buffer, index):
        position = 0

        position = data_buffer[index] << 8
        position |= data_buffer[index + 1]

        if position > 0x7fff:
            position = position - 0x10000

        position = float(position)
        self._value = position / 10000

        return self._byte_size

    def get_as_buffer(self):
        position = int(self._value * 10000)
        buffer = bytearray(self._byte_size)
        buffer[0] = (position & 0xff00) >> 8
        buffer[1] = position & 0xff

        return buffer
