from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.generic.currentSensor.CurrentSensor import CurrentSensor
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_currentSettings import Msg_currentSettings
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_maxCurrentDrain import Msg_maxCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_measuredCurrent import Msg_measuredCurrent
from RoboControl.Robot.Component.generic.currentSensor.protocol.Msg_totalCurrentDrain import Msg_totalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Stream_actualConsumption import Stream_actualConsumption
from RoboControl.Robot.Component.generic.currentSensor.protocol.Stream_maxConsumption import Stream_maxConsumption
from RoboControl.Robot.Component.generic.currentSensor.protocol.Stream_totalConsumption import Stream_totalConsumption
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor


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

    def decode_message(self, remote_data: RemoteMessage) -> bool:
        # if isinstance(remote_data, Msg_temperature):
        #     self.process_sensor_temperature(remote_data)
        return super().decode_message(remote_data)

    def decode_stream(self, remote_data: RemoteStream) -> bool:
        if isinstance(remote_data, Stream_actualConsumption):
            self.process_actual_consumption(remote_data)
        elif isinstance(remote_data, Stream_maxConsumption):
            self.process_max_consumption(remote_data)
        elif isinstance(remote_data, Stream_totalConsumption):
            self.process_total_consumption(remote_data)
        else:
            super().decode_stream(remote_data)
        return False
