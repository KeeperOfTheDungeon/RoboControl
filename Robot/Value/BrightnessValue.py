
from RoboControl.Robot.Value.ComponentValue import ComponentValue


class BrightnessValue(ComponentValue):
	
		def __init__(self, meta_data):
			meta_data["type_name"] = "brightness"
			meta_data["description"] = "brightness"
			meta_data["max_range"] = 1.0
			meta_data["min_range"] = 0.0
			super().__init__(meta_data)

