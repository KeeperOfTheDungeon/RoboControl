from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream
from RoboControl.Com.RemoteParameter import RemoteParameterUint24, RemoteParameterUint8

INDEX_SENSOR = 0


class Cmd_getDistance(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "Cmd_getDistance")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id: int, local_id):
        cmd = Cmd_getDistance(id)
        cmd.set_index(local_id)
        return cmd
    

class Msg_distance(RemoteMessage):
   
    SENSOR_VALUE = 1

    def __init__(self, id: int):
        super().__init__(id,  "actual distance measured by an distance sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterUint24("distance", "distance value in mm"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, distance: int = None
    ):
        cmd = Msg_distance(id)
        if None not in [index, distance]:
            cmd.set_data(index, distance)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_distance(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def set_data(self, index: int, value: int):
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[Msg_distance.SENSOR_VALUE].set_value(value)


class Stream_distances(RemoteStream):
    _parameter_list: list[RemoteParameterUint24]

    def __init__(self, id):
        super().__init__(id,  "actual distances measured by distance sensors")

    @staticmethod
    def get_command(id: int, values):
        cmd = Stream_distances(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def get_distance(self, index):
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_value()

    def set_data(self, values: list[int]):
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def make_parameter(self, index: int):
        return RemoteParameterUint24(f"distance {index}", f"distance for sensor {index}")

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)
