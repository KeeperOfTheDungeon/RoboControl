from RoboControl.Robot.Value.ComponentValue import ComponentValue


class ServoVelocityValue(ComponentValue):


	def __init__(self, meta_data):
		meta_data["type_name"] = "servo velocity"
		meta_data["description"] = "servo velocity value"

		meta_data["max_range"] = 100
		meta_data["min_range"] = -100

