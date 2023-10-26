from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Component.Sensor.luxSensor.RemoteParameterLuxValue import RemoteParameterLuxValue




class Cmd_getLux(RemoteCommand):

    INDEX_SENSOR = 0

    _parameter_list: list[RemoteParameterUint8]

    def __init__(self, id: int):
        super().__init__(id, "Cmd_getLux", "get measured lux value from a light sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index: int) -> None:
        self._parameter_list[Cmd_getLux.INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id: int, local_id: int):
        cmd = Cmd_getLux(id)
        cmd.set_index(local_id)
        return cmd
    

class Msg_lux(RemoteMessage):

    INDEX_SENSOR = 0
    INDEX_LUX = 1

    _parameter_list = list()

    def __init__(self, id: int):
        super().__init__(id, "luxValue", "actual lux value measured by a light sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterLuxValue("distance", "light value in lux"))

    @staticmethod
    def get_command(id, index, distance):
        cmd = Msg_lux(id)
        if None not in [index, distance]:
            cmd.set_data(index, distance)
        return cmd

    def get_index(self) -> int:
        return self._parameter_list[Msg_lux.INDEX_SENSOR].get_value()

    def get_lux_value(self) -> float:
        return self._parameter_list[Msg_lux.INDEX_LUX].get_value()

    def set_data(self, index: int, value: float) -> None:
        self._parameter_list[Msg_lux.INDEX_SENSOR].set_value(index)
        self._parameter_list[Msg_lux.INDEX_LUX].set_value(value)


class Stream_lux(RemoteStream):
    _parameter_list: list[RemoteParameterLuxValue]

    def __init__(self, id: int):
        super().__init__(id, "luxValues", "actual measured light in lux")

    @staticmethod
    def get_command(id: int, values):
        cmd = Stream_lux(id)
        if values:
            cmd.set_data(values)
        return cmd

    def set_data(self, values) -> None:
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def get_lux_value(self, index):
        if index >= self.get_payload_size():
            return 0
        return self._parameter_list[index].get_value()

    def make_parameter(self, index: int):
        return RemoteParameterLuxValue(f"lux {index}", f"measured lux value from sensor {index}")

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)
