from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter
from RoboControl.Robot.Math.Radiant import Radiant

BYTE_SIZE = 2


class RemoteParameterServoPosition(RemoteParameter):

    def __init__(self, name, description):
        super().__init__(name, description, BYTE_SIZE)
        self._value = 0  # position

    def set_position(self, position: float) -> None:
        self._value = position

    def get_position(self):
        return self._value

    def parse_from_buffer(self, data_buffer, index):
        # WIP why?
        position = data_buffer[index] << 8
        position |= data_buffer[index + 1]

        if position > 0x7fff:
            position = position - 0x10000

        # below is same as the java version
        position = float(position)
        self._value = position / 10000

        return self._byte_size

    def get_as_buffer(self):
        position = int(self._value * 10000)
        buffer = bytearray(self._byte_size)
        buffer[0] = (position & 0xff00) >> 8
        buffer[1] = position & 0xff

        return buffer

    def get_as_string(self, description: bool) -> str:
        if description:
            return self.get_name() + "=" + f"{Radiant.convert_radiant_to_degree(self._value):.2f}°"
        return str(self._value)

    def put_data(self, data_buffer):
        data_buffer.append(self._value * 10000)
        return data_buffer
