from copy import deepcopy

from RoboControl.Robot.Component.Sensor.vcnl4000.DistanceTable import DistanceTable
from RoboControl.Robot.Component.Sensor.DistanceSensor import DistanceSensor

DISTANCE_DATA_DEEPTH = 8

VCNL4000_BEAM_WIDTH = 30.0

VCNL4000_MAX_RANGE = 200.0
VCNL4000_MIN_RANGE = 1.0
VCNL4000_MAX_GRANULARITY = 10.0


class Vcnl4000DistanceSensor(DistanceSensor):
    _setup_listener = list()

    def __init__(self, meta_data):
        meta_data["beam_width"] = VCNL4000_BEAM_WIDTH
        meta_data["min_range"] = VCNL4000_MIN_RANGE
        meta_data["max_range"] = VCNL4000_MAX_RANGE
        meta_data["granularity"] = VCNL4000_MAX_GRANULARITY
        meta_data["protocol"]['cmd_getValue'] = meta_data["protocol"]['cmd_getDistance']
        super().__init__(meta_data)

    #	self._proximityValue = 0
    #	self._distance_table = DistanceTable()

    #	def set_proximity_value(self, proximity_value):
    #		self._proximityValue = proximity_value

    #	def get_proximity_value(self):
    #		return self._proximityValue

    def set_distance_table(self, distance_table):
        self._distance_table = deepcopy.copy(distance_table)

        for listener in self._setup_listener:
            listener.distance_table_changed(self)

    def get_distance_table(self):
        return deepcopy.copy(self._distance_table)
