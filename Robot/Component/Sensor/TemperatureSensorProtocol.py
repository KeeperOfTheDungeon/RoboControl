from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream
from RoboControl.Com.RemoteParameter import RemoteParameterUint8, RemoteParameterUint24

INDEX_SENSOR = 0

class Cmd_getTemperature(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "Cmd_getTemperature", "Get measured temperature from a temperature sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id: int, local_id):
        cmd = Cmd_getTemperature(id)
        cmd.set_index(local_id)
        return cmd


class Msg_temperature(RemoteMessage):

    SENSOR_VALUE = 1

    def __init__(self, id: int):
        super().__init__(id, "actual temperature measured by an temperature sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterUint24("temperature", "temperature in °C"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, temperature: float = None
    ):
        cmd = Msg_temperature(id)
        if None not in [index, temperature]:
            cmd.set_data(index, temperature)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_distance(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def set_data(self, index: int, value: float):
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[self.SENSOR_VALUE].set_value(value)

class Stream_temperatures(RemoteStream):

    def __init__(self, id):
        super().__init__(id,  "actual temperature measured by temperature sensors")

    @staticmethod
    def get_command(id: int, values):
        cmd = Stream_temperatures(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def get_temperature(self, index):
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_value()

    def set_data(self, values: list[int]):
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def make_parameter(self, index: int):
        return RemoteParameterUint24(f"temperature {index}", f"temperature for sensor {index}")

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)