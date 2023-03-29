from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.RadiantValue import RadiantValue


class ServoPositionValue(RadiantValue):

	def __init__(self, meta_data):
		meta_data["type_name"] = "servo position"
		meta_data["description"] = "servo position"
		super().__init__(meta_data)




"""

	protected boolean isAtMax;
	protected boolean isAtMin;
	protected boolean isActive;
	

"""