import sys

from RoboControl.Robot.Value.ComponentValue import ComponentValue


class CurrentValue(ComponentValue):
    def __init__(self, meta_data):
        meta_data["type_name"] = "current"
        meta_data["description"] = "current sensor"
        meta_data["max_range"] = sys.float_info.max
        meta_data["min_range"] = -5000

        super().__init__(meta_data)
