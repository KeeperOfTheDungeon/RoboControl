import sys

from RoboControl.Robot.Value.ComponentValue import ComponentValue


class FloatValue(ComponentValue):
    def __init__(self, meta_data):
        meta_data["type_name"] = "float"
        meta_data["description"] = "float value"

        meta_data["max_range"] = sys.float_info.max
        meta_data["min_range"] = sys.float_info.min
        super().__init__(meta_data)

    def add(self, value: float) -> float:
        return self.set_value(self.get_value() + value)

    def set_value(self, value: float) -> float:
        """ "set new value of this instance. If value out of range correct value to range." """
        if value > self.get_max_range():
            value = self.get_max_range()
        elif value < self.get_min_range():
            value = self.get_min_range()

        if value == self.get_value():
            return value
        self._value = value
        self.notify_value_changed()
        return self._value
