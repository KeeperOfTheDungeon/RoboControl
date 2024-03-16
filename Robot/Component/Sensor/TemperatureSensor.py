from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Value.ComponentValue import TemperatureValue


class TemperatureSensor(Sensor):

    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._temperature_value = TemperatureValue(meta_data)

    def get_temperature_value(self):
        return self._temperature_value

    def get_temperature(self):
        return self._temperature_value.get_temperature()

    def set_distance(self, value):
        self._temperature_value.set_value(value)
        return


class TemperatureSensorSet(ComponentSet):
    def __init__(self, components, protocol):
        super().__init__(components)
