from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Component.Sensor.luxSensor.LuxSensorProtocol import Cmd_getLux
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
