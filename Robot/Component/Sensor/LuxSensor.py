from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Component.Sensor.LuxSensorProtocol import Cmd_getLux, Msg_lux, Stream_lux
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.lux.LuxValue import LuxValue


class LuxSensor(Sensor):
    _sensor_listener = list()

    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._lux_value = LuxValue(meta_data)  # ,10000)

    def get_lux_value(self) -> LuxValue:
        return self._lux_value

    def get_lux(self) -> float:
        return self.get_lux_value().get_value()

    def set_lux(self, lux: float) -> None:
        self._lux_value.set_value(lux)
        for listener in self._sensor_listener:
            listener.lux_value_changed(self)

    def remote_get_value(self):
        cmd = Cmd_getLux.get_command(self._cmd_get_value, self._local_id)
        self.send_data(cmd)

    def get_data_values(self) -> list[ComponentValue]:
        return [self.get_lux_value()]



class LuxSensorSet(ComponentSet):
    def __init__(self, components, protocol):
        super().__init__(components)
        self._msg_lux = protocol['msg_lux']
        self._stream_lux = protocol['stream_lux']

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        if self._msg_lux != 0:
            msg_list.append(RemoteProcessor(Msg_lux.get_command(self._msg_lux,0,0), self))
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        if self._stream_lux != 0:
            initial_values = [0 for i in self]
            cmd = Stream_lux.get_command(self._stream_lux, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        return stream_list

    def process_msg_lux(self, remote_data: Msg_lux) -> None:
        index = remote_data.get_index()
        value = remote_data.get_lux_value()

        if index < len(self):
            self[index].set_lux(value)

    def process_stream_lux(self, stream_lux: Stream_lux) -> None:
        for sensor in self:
            index = sensor.get_local_id()
            value = stream_lux.get_lux_value(index)
            sensor.set_lux(value)

    def get_component_on_local_id(self, id: int) -> LuxSensor:
        # noinspection PyTypeChecker
        return super().get_component_on_local_id(id)

    def process_lux(self, remote_data):
        index = remote_data.get_index()
        sensor = self.get_component_on_local_id(index)
        if sensor is not None:
            sensor.set_lux(remote_data.get_lux_value())

    def process_lux_values(self, remote_data: Stream_lux):
        for index in range(remote_data.get_parameter_count()):
            sensor = self.get_component_on_local_id(index)
            if sensor is not None:
                value = remote_data.get_lux_value(index)
                sensor.set_lux(value)

    def decode_message(self, remote_data):
        if isinstance(remote_data, Msg_lux):
            self.process_lux(remote_data)
        else:
            super().decode_message(remote_data)
        return False  # why always False

    def decode_stream(self, remote_data):
        if isinstance(remote_data, Stream_lux):
            self.process_lux_values(remote_data)
        else:
            super().decode_stream(remote_data)
        return False  # why always False
