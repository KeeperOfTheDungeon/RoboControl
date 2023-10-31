
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Value.ComponentValue import LightValue


class CurrentSensor(Sensor):
    _sensor_listener = list()

    def __init__(self, meta_data):
        super().__init__(meta_data)

    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._lux_value = LightValue(meta_data)  # ,10000)
