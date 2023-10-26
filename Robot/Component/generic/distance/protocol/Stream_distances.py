from RoboControl.Com.RemoteParameter import RemoteParameterUint24
from RoboControl.Com.RemoteData import RemoteStream


class Stream_distances(RemoteStream):
    _parameter_list: list[RemoteParameterUint24]

    def __init__(self, id):
        super().__init__(id, "distances", "actual distances measured by distance sensors")

    @staticmethod
    def get_command(id: int, values: list[int] = None) -> "Stream_distances":
        cmd = Stream_distances(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def get_distance(self, index: int) -> int:
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_value()

    def set_data(self, values: list[int]) -> None:
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def make_parameter(self, index: int) -> RemoteParameterUint24:
        return RemoteParameterUint24(f"distance {index}", f"distance for sensor {index}")

    def parse_data_packet_data(self, data_packet: "RemoteDataPacket") -> None:
        return self.parse_data_packet_data_dynamic(data_packet)
