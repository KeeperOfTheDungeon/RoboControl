from RoboControl.Robot.Value.ComponentValue import ComponentValue


class DistanceValue(ComponentValue):

    def __init__(self, meta_data):
        meta_data["type_name"] = "distance"
        meta_data["description"] = "distance value"
        super().__init__(meta_data)
        self._beamWidth = meta_data["beam_width"]
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

    def get_milimeters(self):
        return self._value

    def get_beam_width(self):
        return self._beamWidth
