from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Sensor.CurrentSensorProtocol import Cmd_getActualCurrentDrain, Cmd_getMaximalCurrentDrain, Cmd_getTotalCurrentDrain, Cmd_resetMaximalCurrentDrain, Cmd_resetTotalCurrentDrain, Cmd_setCurrentSettings, Msg_currentSettings, Msg_maxCurrentDrain, Msg_measuredCurrent, Msg_totalCurrentDrain, Stream_actualConsumption, Stream_maxConsumption, Stream_totalConsumption
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Value.ComponentValue import CurrentValue


class CurrentSensor(Sensor):
    _sensor_listener = list()
    _setup_listener =  list()

    def __init__(self, meta_data):
        super().__init__(meta_data)

        protocol = meta_data["protocol"]
        self._cmd_get_max_current = protocol["cmd_getMaxCurrent"]
        self._cmd_get_total_current = protocol["cmd_getTotalCurrent"]
        self._cmd_reset_max_current = protocol["cmd_resetMaxCurrent"]
        self._cmd_reset_total_current = protocol["cmd_resetTotalCurrent"]

        self._window_size = 0
        self._threshold = 0
        self._actual = CurrentValue({**meta_data, "name": meta_data["name"] + " actual current"})
        self._total = CurrentValue({**meta_data, "name": meta_data["name"] + " total current"})
        self._max = CurrentValue({**meta_data, "name": meta_data["name"] + " max current"})

    def get_actual(self):
        return self._actual

    get_value = get_actual

    def get_actual_value(self):
        return self._actual.get_value()

    def set_actual(self, value: int):
        self._actual.set_value(value)
        for listener in self._sensor_listener:
            listener.current_value_changed()

    def get_max(self) -> CurrentValue:
        return self._max

    def get_max_value(self):
        return self._max.get_value()

    def set_max(self, value: int):
        self._max.set_value(value)
        for listener in self._sensor_listener:
            listener.current_value_changed()

    def get_total(self) -> CurrentValue:
        return self._total

    def get_total_value(self) -> float:
        return self._total.get_value()

    def set_total(self, value: float):
        self._total.set_value(value)
        for listener in self._sensor_listener:
            listener.current_value_changed()

    def remote_get_current(self):
        cmd = Cmd_getActualCurrentDrain.get_command(self._cmd_get_value, self._local_id)
        self.send_data(cmd)

    def remote_get_max_current(self):
        cmd = Cmd_getMaximalCurrentDrain.get_command(self._cmd_get_max_current, self._local_id)
        self.send_data(cmd)

    def remote_get_total_current(self):
        cmd = Cmd_getTotalCurrentDrain.get_command(self._cmd_get_total_current, self._local_id)
        self.send_data(cmd)

    def remote_reset_max_current(self):
        cmd = Cmd_resetMaximalCurrentDrain.get_command(self._cmd_reset_max_current, self._local_id)
        self.send_data(cmd)

    def remote_reset_total_current(self):
        cmd = Cmd_resetTotalCurrentDrain.get_command(self._cmd_reset_total_current, self._local_id)
        self.send_data(cmd)

    def remote_set_settings(self, window_size: int, threshold: int) -> bool:
        if self.component_protocol is None:
            return False
        cmd = Cmd_setCurrentSettings.get_command(self._cmd_set_settings, self._local_id, window_size, threshold)
        return self.send_data(cmd)

    def get_window_size(self) -> int:
        """ "get size of measurement window , the real size is 10 * windowSize" """
        return self._window_size

    def set_window_size(self, window_size):
        self._window_size = window_size
        for listener in self._setup_listener:
            listener.current_window_size_changed(self)

    def get_threshold(self) -> int:
        """ "get current threshold, threshold is the minimum level value for current sensing" """
        return self._threshold

    def set_threshold(self, threshold):
        self._threshold = threshold
        for listener in self._setup_listener:
            listener.current_threshold_changed(self)

    def get_data_values(self):
        return [
            self._actual,
            self._total,
            self._max,
        ]


class CurrentSensorSet(ComponentSet):
    def __init__(self, components, protocol):
        super().__init__([
            CurrentSensor(component) for component in components
        ])
        self._msg_actual_current = protocol['msg_actualCurrent']
        self._msg_max_current = protocol['msg_maxCurrent']
        self._msg_total_current = protocol['msg_totalCurrent']

        self._stream_actual_current = protocol['stream_actualCurrent']
        self._stream_max_current = protocol['stream_maxCurrent']
        self._stream_total_current = protocol['stream_totalCurrent']

        self._cmd_get_actual_current = protocol['cmd_getActualCurrentDrain']
        self._cmd_get_max_current = protocol['cmd_getMaxCurrent']
        self._cmd_get_total_current = protocol['cmd_getTotalCurrent']

        self._cmd_reset_max_current = protocol['cmd_resetMaxCurrent']
        self._cmd_reset_total_current = protocol['cmd_resetTotalCurrent']

    def get_command_processors(self):
        stream_list = super().get_command_processors()
        initial_values = [0 for _ in self]
        if self._cmd_get_actual_current != 0:
            cmd = Stream_actualConsumption.get_command(self._stream_actual_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        if self._cmd_get_max_current != 0:
            cmd = Stream_maxConsumption.get_command(self._stream_max_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        if self._cmd_get_total_current != 0:
            cmd = Stream_totalConsumption.get_command(self._stream_total_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        if self._cmd_reset_max_current != 0:
            cmd = Stream_totalConsumption.get_command(self._stream_total_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        if self._cmd_reset_total_current != 0:
            cmd = Stream_totalConsumption.get_command(self._stream_total_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        return stream_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        initial_values = [0 for _ in self]
        if self._stream_actual_current != 0:
            cmd = Stream_actualConsumption.get_command(self._stream_actual_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        if self._stream_actual_current != 0:
            cmd = Stream_maxConsumption.get_command(self._stream_max_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        if self._stream_actual_current != 0:
            cmd = Stream_totalConsumption.get_command(self._stream_total_current, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)
        return stream_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        if self._msg_actual_current != 0:
            cmd = Msg_measuredCurrent.get_command(self._msg_actual_current)
            processor = RemoteProcessor(cmd, self)
            msg_list.append(processor)
        if self._msg_max_current != 0:
            cmd = Msg_maxCurrentDrain.get_command(self._msg_max_current)
            processor = RemoteProcessor(cmd, self)
            msg_list.append(processor)
        if self._msg_total_current != 0:
            cmd = Msg_totalCurrentDrain.get_command(self._msg_total_current)
            processor = RemoteProcessor(cmd, self)
            msg_list.append(processor)
        if self._msg_total_current != 0:
            cmd = Msg_currentSettings.get_command(self._msg_total_current)
            processor = RemoteProcessor(cmd, self)
            msg_list.append(processor)
        return msg_list

    def process_current_settings(self, current_data: Msg_currentSettings) -> None:
        current: CurrentSensor = self.get_component_on_local_id(current_data.get_index())
        if current is not None:
            current.set_threshold(current_data.get_threshold())
            current.set_window_size(current_data.get_window_size())

    def process_current_value(self, current_data: Msg_measuredCurrent) -> None:
        current: CurrentSensor = self.get_component_on_local_id(current_data.get_index())
        if current is not None:
            current.set_actual(current_data.get_drain())

    def process_actual_consumption(self, current_data: Stream_actualConsumption) -> None:
        for index in range(current_data.get_parameter_count()):
            current: CurrentSensor = self.get_component_on_local_id(index)
            if current is not None:
                current.set_actual(current_data.get_value(index))

    def process_max_consumption(self, current_data: Stream_maxConsumption) -> None:
        for index in range(current_data.get_parameter_count()):
            current: CurrentSensor = self.get_component_on_local_id(index)
            if current is not None:
                current.set_max(current_data.get_value(index))

    def process_total_consumption(self, current_data: Stream_totalConsumption) -> None:
        for index in range(current_data.get_parameter_count()):
            current: CurrentSensor = self.get_component_on_local_id(index)
            if current is not None:
                current.set_total(current_data.get_value(index))

    def process_current_max_value(self, current_data: Msg_maxCurrentDrain) -> None:
        current: CurrentSensor = self.get_component_on_local_id(current_data.get_index())
        if current is not None:
            current.set_total(current_data.get_max_current())

    # noinspection PyTypeChecker
    def get_component_on_local_id(self, index: int) -> CurrentSensor:
        return super().get_component_on_local_id(index)

    def decode_message(self, remote_data):
        # if isinstance(remote_data, Msg_temperature):
        #     self.process_sensor_temperature(remote_data)
        return super().decode_message(remote_data)

    def decode_stream(self, remote_data):
        if isinstance(remote_data, Stream_actualConsumption):
            self.process_actual_consumption(remote_data)
        elif isinstance(remote_data, Stream_maxConsumption):
            self.process_max_consumption(remote_data)
        elif isinstance(remote_data, Stream_totalConsumption):
            self.process_total_consumption(remote_data)
        else:
            super().decode_stream(remote_data)
        return False
