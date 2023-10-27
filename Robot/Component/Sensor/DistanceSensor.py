from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Sensor.DistanceSensorProtocol import Cmd_getDistance, Msg_distance, Stream_distances
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Value.ComponentValue import DistanceValue


class DistanceSensor(Sensor):

    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._distance_value = DistanceValue(meta_data)

    def get_distance_value(self):
        return self._distance_value

    def get_distance(self):
        self._distance_value.get_milimeters()

    def set_distance(self, value):
        self._distance_value.set_value(value)

    def remote_get_distance(self):
        cmd = Cmd_getDistance.get_command(self._cmd_get_value, self._local_id)
        self.send_data(cmd)



class DistanceSensorSet(ComponentSet):
    def __init__(self, sensors, protocol):
        super().__init__(sensors)
        self._msg_distance = protocol['msg_distance']
        self._stream_distance = protocol['stream_distance']

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        if self._msg_distance != 0:
            cmd = Msg_distance.get_command(self._msg_distance)
            processor = RemoteProcessor(cmd, self)
            msg_list.append(processor)
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        if self._stream_distance != 0:
            initial_values = [0 for i in self]
            cmd = Stream_distances.get_command(self._stream_distance, values=initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        return stream_list

    def get_component_on_local_id(self, id: int) -> DistanceSensor:
        # noinspection PyTypeChecker
        return super().get_component_on_local_id(id)

    def process_sensor_distances(self, remote_data: Stream_distances) -> None:
        for index in range(remote_data.get_parameter_count()):
            sensor = self.get_component_on_local_id(index)
            if sensor is not None:
                sensor.set_distance(remote_data.get_distance(index))

    def process_sensor_distance(self, remote_data: Msg_distance) -> None:
        index = remote_data.get_index()
        sensor = self.get_component_on_local_id(index)
        if sensor is not None:
            sensor.set_distance(remote_data.get_distance())

    def decode_stream(self, remote_data):
        if isinstance(remote_data, Stream_distances):
            self.process_sensor_distances(remote_data)
        else:
            super().decode_stream(remote_data)
        return False

    def decode_message(self, remote_data) :
        if isinstance(remote_data, Msg_distance):
            self.process_sensor_distance(remote_data)
        else:
            super().decode_message(remote_data)
        return False
