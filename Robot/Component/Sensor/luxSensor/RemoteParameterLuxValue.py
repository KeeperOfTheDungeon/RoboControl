from RoboControl.Com.RemoteParameter import RemoteParameter

BYTE_SIZE = 3


class RemoteParameterLuxValue(RemoteParameter):
    def __init__(self, name, description):
        super().__init__(name, description, BYTE_SIZE)
        self._value = 0.0

    def put_data(self, data_buffer: list) -> None:
        # high = self._value >> 16
        # data_buffer.put(high)
        # low = self._value & 0xffff
        # data_buffer.put_char(low)
        data_buffer.append(self._value + 0x800000)

    def parse_from_buffer(self, data_buffer: bytearray, index: int) -> int:
        # if self._value > 0xffffff:
        #     self._value = 0xffffff
        value = data_buffer[index] << 16
        value |= data_buffer[index + 1] << 8
        value |= data_buffer[index + 2]

        self._value = value * 0.25
        return self._byte_size

    def get_as_string(self, description: bool) -> str:
        if description:
            return self._name + "=" + str(self._value) + "lux"
        return str(self._value)
