from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStream import RemoteStream


class Stream_actualConsumption(RemoteStream):
    _parameter_list: list[RemoteParameterUint16]

    def __init__(self, id: int = LegControllerProtocol.STREAM_CURRENT_CONSUMPTION):
        super().__init__(
            id,
            "actualConsumption",
            "measured current values from device size, size/count is device dependent"
        )

    @staticmethod
    def get_command(id: int, values: list[int]) -> "Stream_actualConsumption":
        cmd = Stream_actualConsumption(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def set_data(self, values: list[int]) -> None:
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def get_actual_consumption(self, index):
        value = 0
        if index < len(self._parameter_list):
            value = self._parameter_list[index].get_value()
        return value

    def get_value(self, index: int) -> int:
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_value()

    def get_values_count(self) -> int:
        return len(self._parameter_list)

    def make_parameter(self, index: int) -> RemoteParameterUint16:
        return RemoteParameterUint16(f"current {index}", f"measured current for sensor {index}")

    def parse_data_packet_data(self, data_packet: "RemoteDataPacket") -> None:
        return self.parse_data_packet_data_dynamic(data_packet)
