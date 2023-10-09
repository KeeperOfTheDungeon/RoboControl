from RoboControl.Robot.AbstractRobot.AbstractListener import CurrentSensorListener, CurrentSensorChangeNotifier, \
    CurrentSensorSetupChangeNotifier
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_getActualCurrentDrain import \
    Cmd_getActualCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_getMaximalCurrentDrain import \
    Cmd_getMaximalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_getTotalCurrentDrain import Cmd_getTotalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_resetMaximalCurrentDrain import \
    Cmd_resetMaximalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_resetTotalCurrentDrain import \
    Cmd_resetTotalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_setCurrentSettings import Cmd_setCurrentSettings
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.current.CurrentValue import CurrentValue


class CurrentSensor(
    Sensor,
    CurrentSensorChangeNotifier,
    CurrentSensorSetupChangeNotifier
):
    _sensor_listener: list[CurrentSensorListener]
    _setup_listener: list[CurrentSensorSetupChangeNotifier]

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

    def get_actual(self) -> CurrentValue:
        return self._actual

    get_value = get_actual

    def get_actual_value(self) -> float:
        return self._actual.get_value()

    def set_actual(self, value: int) -> None:
        self._actual.set_value(value)
        for listener in self._sensor_listener:
            listener.current_value_changed()

    def get_max(self) -> CurrentValue:
        return self._max

    def get_max_value(self) -> float:
        return self._max.get_value()

    def set_max(self, value: int) -> None:
        self._max.set_value(value)
        for listener in self._sensor_listener:
            listener.current_value_changed()

    def get_total(self) -> CurrentValue:
        return self._total

    def get_total_value(self) -> float:
        return self._total.get_value()

    def set_total(self, value: float) -> None:
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

    def set_window_size(self, window_size: int) -> None:
        self._window_size = window_size
        for listener in self._setup_listener:
            listener.current_window_size_changed(self)

    def get_threshold(self) -> int:
        """ "get current threshold, threshold is the minimum level value for current sensing" """
        return self._threshold

    def set_threshold(self, threshold: int) -> None:
        self._threshold = threshold
        for listener in self._setup_listener:
            listener.current_threshold_changed(self)

    def get_data_values(self) -> list[ComponentValue]:
        return [
            self._actual,
            self._total,
            self._max,
        ]
