from RoboControl.Robot.Value.ComponentValue import ComponentValue


class CurrentValue(ComponentValue):
	def __init__(self, meta_data):
		meta_data["type_name"] = "current"
		meta_data["description"] = "current sensor"
		meta_data["max_range"] = 5000
		meta_data["min_range"] = 0

		super().__init__(meta_data)
