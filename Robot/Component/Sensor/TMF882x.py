from PicoControl.com.tmf8821.tmf8821_app import TMF8821MeasureResults
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Component.Sensor.DistanceSensor import DistanceSensorSet, DistanceSensor
from RoboControl.Robot.Component.Sensor.TMF882xProtocol import Msg_distance
from RoboControl.Robot.Component.Sensor.DistanceSensorProtocol import Cmd_getDistance

from RoboControl.Robot.Component.Sensor.TemperatureSensor import TemperatureSensor, TemperatureSensorSet
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor


class TMF882x(RobotComponent):

    # TODO Sensors and spad_map_setting should be equal
    def __init__(self, meta_data, distance_sensors_count: int = 9):
        super().__init__(meta_data)

        self._temp_sensor = TMF882xTemperatureSensor(meta_data)
        self._distance_sensors: list[TMF882xDistanceSensor] = list()

        for i in range(0, distance_sensors_count):
            self._distance_sensors.append(TMF882xDistanceSensor(meta_data))

    def get_temp_sensor(self):
        return self._temp_sensor

    def get_distance_sensors(self):
        return self._distance_sensors

    def set_transmitter(self, transmitter):
        super().set_transmitter(transmitter)
        self._temp_sensor.set_transmitter(transmitter)
        for sensor in self._distance_sensors:
            sensor.set_transmitter(transmitter)


class TMF882xSet(ComponentSet):

    def __init__(self, components, protocol):
        self.distance_sensors = list()
        self.temperature_sensors = list()
        self.tmf882x_sensors = list()

        for component in components:
            sensor = TMF882x(component)
            self.tmf882x_sensors.append(sensor)
            self.distance_sensors.append(sensor.get_distance_sensors())
            self.temperature_sensors.append(sensor.get_temp_sensor())

        super().__init__(self.tmf882x_sensors)

        self._cmd_getTemperature = protocol["cmd_getTemperature"] = protocol["cmd_getValue"]
        self._temperature_sensor_set = TMF882xTemperatureSensorSet(self.temperature_sensors, protocol)

        self._cmd_getDistance = protocol["cmd_getDistance"] = protocol["cmd_getValue"]
        self._distance_sensor_set = TMF882xDistanceSensorSet(self.distance_sensors, protocol)

    def get_distance_sensors(self):
        return self._distance_sensor_set

    def get_temperature_sensors(self):
        return self._temperature_sensor_set

    def get_command_processors(self):
        command_list = super().get_command_processors()
        command_list.append(RemoteProcessor(Cmd_getDistance(self._cmd_getDistance), self))
        command_list.extend(self._distance_sensor_set.get_command_processors())
        command_list.extend(self._temperature_sensor_set.get_command_processors())
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        msg_list.extend(self._temperature_sensor_set.get_message_processors())
        msg_list.extend(self._distance_sensor_set.get_message_processors())
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        stream_list.extend(self._distance_sensor_set.get_stream_processors())
        stream_list.extend(self._temperature_sensor_set.get_stream_processors())
        return stream_list

    def get_component_on_local_id(self, index: int) -> TMF882x:
        return super().get_component_on_local_id(index)

    def decode_command(self, remote_command):
        if isinstance(remote_command, Cmd_getDistance):
            cmd: Cmd_getDistance = remote_command
            print("TMF8821: ", cmd.get_parameter_list()[0])
            return True


class TMF882xDistanceSensor(DistanceSensor):
    TMF882x_MAX_RANGE = 5000.0
    TMF882x_MIN_RANGE = 10.0

    _setup_listener = list()

    def __init__(self, meta_data):
        meta_data["min_range"] = TMF882xDistanceSensor.TMF882x_MIN_RANGE
        meta_data["max_range"] = TMF882xDistanceSensor.TMF882x_MAX_RANGE
        meta_data["confidence"] = 0
        meta_data["protocol"]["cmd_getValue"] = meta_data["protocol"]["cmd_getTemperature"]
        self._msg_distance = meta_data["protocol"]["msg_distance"]
        super().__init__(meta_data)

    def set_distance(self, value):
        if isinstance(value, TMF8821MeasureResults):
            super().set_distance(value.distanceInMm)
            self.set_confidence(value.confidence)
        else:
            super().set_distance(value)

    def set_confidence(self, value):
        self._distance_value.set_confidence(value)

    def get_confidence(self):
        return self._distance_value.get_confidence()

    def Msg_distance(self):
        cmd = Msg_distance.get_command(self._msg_distance, self._local_id, self.get_distance(), self.get_confidence())
        self.send_data(cmd)


class TMF882xTemperatureSensor(TemperatureSensor):

    def __init__(self, meta_data):
        meta_data["protocol"]["cmd_getValue"] = meta_data["protocol"]["cmd_getTemperature"]
        super().__init__(meta_data)


class TMF882xTemperatureSensorSet(TemperatureSensorSet):
    pass


class TMF882xDistanceSensorSet(DistanceSensorSet):
    pass
