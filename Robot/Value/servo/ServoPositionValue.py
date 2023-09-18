from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.RadiantValue import RadiantValue


class ServoPositionValue(RadiantValue):

	def __init__(self, meta_data):
		meta_data["type_name"] = "servo position"
		meta_data["description"] = "servo position"
		super().__init__(meta_data)

	def is_at_min(self) -> bool:
		raise ValueError("WIP")

	def is_at_max(self) -> bool:
		raise ValueError("WIP")

	def is_active(self) -> bool:
		raise ValueError("WIP")

	def set_stalling(self, *args) -> None:
		raise ValueError("WIP")

	def set_on(self, *args) -> None:
		raise ValueError("WIP")

	def set_at_min(self, *args) -> None:
		raise ValueError("WIP")

	def set_at_max(self, *args) -> None:
		raise ValueError("WIP")

	def set_inverse(self, *args) -> None:
		raise ValueError("WIP")
