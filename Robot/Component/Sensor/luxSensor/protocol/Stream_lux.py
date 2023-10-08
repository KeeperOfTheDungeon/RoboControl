from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Sensor.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue


class Stream_lux(RemoteStream):
    _parameter_list: list[RemoteParameterLuxValue]

    def __init__(self, id: int):
        super().__init__(id, "luxValues", "actual measured light in lux")

    @staticmethod
    def get_command(id: int, values: list[float] = None):
        cmd = Stream_lux(id)
        if values:
            cmd.set_data(values)
        return cmd

    def set_data(self, values: list[float]) -> None:
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def get_lux_value(self, index: int) -> float:
        if index >= self.get_payload_size():
            return 0
        return self._parameter_list[index].get_value()

    def make_parameter(self, index: int) -> RemoteParameterLuxValue:
        return RemoteParameterLuxValue(f"lux {index}", f"measured lux value from sensor {index}")

    def parse_data_packet_data(self, data_packet: "RemoteDataPacket") -> None:
        return self.parse_data_packet_data_dynamic(data_packet)
