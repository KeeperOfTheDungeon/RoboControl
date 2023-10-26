import struct

from RoboControl.Com.RemoteParameter import RemoteParameter
from RoboControl.Robot.Math.Radiant import Radiant


class RemoteParameterServoVelocity(RemoteParameter):
    def __init__(self, name, description):
        super().__init__(name, description, 2)
        self._velocity: float = 0

    def set_velocity(self, velocity: float) -> None:
        self._velocity = velocity

    def get_velocity(self) -> float:
        return self._velocity

    def get_buffer_size(self) -> int:
        return self._byte_size

    def put_data(self, data: bytearray) -> None:
        v = self._velocity * 314.16
        data.join(struct.pack("f", v))

    def parse_from_buffer(self, data_buffer: bytearray, index: int) -> int:
        position = data_buffer[index:index + self._byte_size]
        position /= 314.16
        self._velocity = position
        return self._byte_size

    def get_as_string(self, description: bool) -> str:
        res = ""
        if description:
            res += f"{self._name}="
            res += f"{Radiant.convert_radiant_to_degree(self._velocity)}°"
        else:
            res += f"{self._velocity}"
        return res
