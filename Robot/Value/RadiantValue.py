
from RoboControl.Robot.Math.Radiant import Radiant
from RoboControl.Robot.Value.ComponentValue import ComponentValue


class RadiantValue(ComponentValue):
	def __init__(self,meta_data):
		super().__init__(meta_data)



	def get_value_as_degree(self):
		radiant = Radiant.convert_radiant_to_degree(self._value)
		return radiant
