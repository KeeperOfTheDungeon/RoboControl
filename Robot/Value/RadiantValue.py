from RoboControl.Robot.Math.Radiant import Radiant
from RoboControl.Robot.Value.ComponentValue import ComponentValue


class RadiantValue(ComponentValue):
    def get_value_as_degree(self):
        return Radiant.convert_radiant_to_degree(self._value)
