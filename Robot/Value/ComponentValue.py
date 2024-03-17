import sys

from RoboControl.Robot.Math.Radiant import Radiant


class ComponentValue:
    def __init__(self, meta_data: dict):
        self._name: str = meta_data.get("name", "generic")
        self._type_name: str = meta_data.get("type_name", "generic")
        self._description: str = meta_data.get("description", "generic")

        self._max_range: float = meta_data["max_range"]  # sys.sys.float_info.max
        self._min_range: float = meta_data["min_range"]  # sys.sys.float_info.min
        self._value: float = 0

        self._overflow: bool = False
        self._underflow: bool = False
        self._valid: bool = False

        self._notifyAllways: bool = True
        self._value_changed_listener_list = list()  # this.listeners

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def has_name(self, name) -> bool:
        return self._name == name

    def get_type_name(self) -> str:
        return self._type_name

    def get_type_description(self) -> str:
        return self._description

    def set_range(self, min_range: float, max_range: float) -> None:
        """ "set minimum und maximum range of this float value" """
        self._max_range = max_range
        self._min_range = min_range

    def get_min_range(self) -> float:
        return self._min_range
    
    def set_min_range(self, min_range: float) -> None:
        self._min_range = min_range

    def get_max_range(self) -> float:
        return self._max_range
    
    def set_max_range(self, max_range: float) -> None:
        self._max_range = max_range

    def set_overflow_value(self) -> None:
        self._value = self._max_range
        self._overflow = True
        self._underflow = False
        self._valid = True

    def set_underflow_value(self) -> None:
        self._value = self._min_range
        self._overflow = False
        self._underflow = True
        self._valid = True

    def set_value(self, value):
        value_changed = False

        if self._notifyAllways:
            value_changed = True
        elif value != self._value:
            value_changed = True

        if value > self._max_range:
            self.set_overflow_value()
        elif value < self._min_range:
            self.set_underflow_value()
        else:
            self._overflow = False
            self._underflow = False
            self._value = value
            self._valid = True

        if value_changed:
            self.notify_value_changed()
        return self._value

    def get_value(self) -> float:
        return self._value

    def is_valid(self) -> bool:
        return self._valid

    def add_listener(self, listener):
        self._value_changed_listener_list.append(listener)

    def remove_listener(self, listener):
        self._value_changed_listener_list.remove(listener)

    def notify_value_changed(self):
        for listener in self._value_changed_listener_list:
            listener.component_value_changed(self)

    def actualize(self):
        return False

    def __str__(self):
        return self._name

    @staticmethod
    def to_formated_fraction_string(value: float, fraction: int) -> str:
        # TODO why not just fstring?
        value_as_string = str(value)
        separator_index = value_as_string.index('.')
        fraction_size = len(value_as_string) - separator_index
        if fraction_size > fraction:
            fraction_size = fraction + 1
        return value_as_string[0:separator_index + fraction_size]


class BrightnessValue(ComponentValue):

    def __init__(self, meta_data):
        meta_data["type_name"] = "brightness"
        meta_data["description"] = "brightness"
        meta_data["max_range"] = 1.0
        meta_data["min_range"] = 0.0
        super().__init__(meta_data)


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


class RadiantValue(ComponentValue):
    def get_value_as_degree(self):
        return Radiant.convert_radiant_to_degree(self._value)


class LightValue(ComponentValue):

    def __init__(self, meta_data):
        meta_data["type_name"] = "light"
        meta_data["description"] = "light"
        super().__init__(meta_data)


class LuxValue(ComponentValue):

    def __init__(self, meta_data):
        meta_data["type_name"] = "lux"
        meta_data["description"] = "lux"
        super().__init__(meta_data)


class TemperatureValue(ComponentValue):

    def __init__(self, meta_data):
        meta_data["type_name"] = "temperature"
        meta_data["description"] = "temperature"
        meta_data["max_range"] = 100.0
        meta_data["min_range"] = -100.0
        super().__init__(meta_data)

    def get_temperature(self):
        return self._value

    def set_temperature(self, temperature):
        self._value = temperature
        return


class DistanceValue(ComponentValue):
    def __init__(self, meta_data):
        meta_data["type_name"] = "distance"
        meta_data["description"] = "distance value"
        super().__init__(meta_data)

        if "beam_width" in meta_data:
            self._beamWidth = meta_data["beam_width"]
        if "granularity" in meta_data:
            self._granularity = meta_data["granularity"]

    def get_granularity(self):
        return self._granularity

    def set_granularity(self, granularity):
        self._granularity = granularity

    def set_overflow_value(self):
        self._value = 0
        self._overflow = False
        self._underflow = False
        self._valid = False

    def set_underflow_value(self):
        self._value = 0
        self._overflow = False
        self._underflow = False
        self._valid = False

    def set_distance_range(self, distance_range):
        self._max_range = distance_range

    def get_distance_range(self):
        return self._max_range

    def get_millimeters(self):
        return self._value

    def get_beam_width(self):
        return self._beamWidth


class CurrentValue(ComponentValue):
    def __init__(self, meta_data):
        meta_data["type_name"] = "current"
        meta_data["description"] = "current sensor"
        meta_data["max_range"] = sys.float_info.max
        meta_data["min_range"] = -5000

        super().__init__(meta_data)
