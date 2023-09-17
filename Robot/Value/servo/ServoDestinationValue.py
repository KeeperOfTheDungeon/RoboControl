from RoboControl.Robot.Math.Radiant import Radiant
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.RadiantValue import RadiantValue
from RoboControl.Robot.Value.servo.ServoVelocityValue import ServoVelocityValue


class ServoDestinationValue(RadiantValue):
    def __init__(self, meta_data):
        meta_data["type_name"] = "servo destination"
        meta_data["description"] = "servo destination value"

        meta_data["max_range"] = 100
        meta_data["min_range"] = -100
        super().__init__(meta_data)
        self._velocity = ServoVelocityValue(meta_data)

    def set_destination(self, destination):
        self.set_value(destination)

    def get_destination(self):
        return self.get_value()

    def set_velocity(self, velocity):
        self._velocity.set_value(velocity)

    def get_velocity(self):
        return self._velocity.get_value()

    def get_position_as_degree(self) -> float:
        return Radiant.convert_radiant_to_degree(self.get_value())
