from RoboControl.Robot.Math.Radiant import Radiant
from RoboControl.Robot.Value.ComponentValue import ComponentValue, RadiantValue


class ServoDestinationValue(RadiantValue):
    def __init__(self, meta_data):
        meta_data["type_name"] = "servo destination"
        meta_data["description"] = "servo destination value"

        # WIP are these correct?
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


class ServoPositionValue(RadiantValue):  # ServoAngleValue
    _is_at_max: bool = False
    _is_at_min: bool = False

    _is_active: bool = False
    _is_on: bool = False

    _is_inverse: bool = False
    _is_stalling: bool = False

    def __init__(self, meta_data):
        meta_data["type_name"] = "servo position"
        meta_data["description"] = "servo position"
        super().__init__(meta_data)
        self._min_range = 0
        self._max_range = 0

    def is_active(self) -> bool:
        return self._is_active

    def set_active(self, status: bool) -> None:
        self._is_active = status

    def is_on(self) -> bool:
        return self._is_on

    def set_on(self, status: bool) -> None:
        self._is_on = status

    def is_inverse(self) -> bool:
        return self._is_inverse

    def set_inverse(self, status: bool) -> None:
        self._is_inverse = status

    def get_position_as_radiant(self) -> float:
        # return (self.get_value() * math.pi) / 180.0
        return self.get_value()

    get_rotation = get_position_as_radiant

    def get_position_as_degree(self) -> float:
        return Radiant.convert_radiant_to_degree(self.get_value())

    def is_stalling(self) -> bool:
        return self._is_stalling

    def set_stalling(self, is_stalling: bool) -> None:
        self._is_stalling = is_stalling

    def is_at_min(self) -> bool:
        return self._is_at_min

    def set_at_min(self, status: bool) -> None:
        self._is_at_min = status

    def is_at_max(self) -> bool:
        return self._is_at_max

    def set_at_max(self, status: bool) -> None:
        self._is_at_max = status

    def component_value_changed(self, source: ComponentValue) -> None:
        # if source == self._min_servo_range:
        # 	self._min_range = source.get_value()
        # elif source == self._max_servo_range:
        # 	self._max_range = source.get_value()
        self.set_value(source.get_value())

    def get_as_string(self, description: bool) -> str:
        infos = []
        if description:
            infos.append(self._name)
            infos.append(f"is_on={self._is_on}")
            infos.append(f"is_active={self._is_active}")
            infos.append(f"is_stalling={self._is_stalling}")
            infos.append(f"is_at_max={self._is_at_max}")
            infos.append(f"is_at_min={self._is_at_min}")
        else:
            infos.append(f"{self._is_on}")
            infos.append(f"{self._is_active}")
            infos.append(f"{self._is_stalling}")
            infos.append(f"{self._is_at_max}")
            infos.append(f"{self._is_at_min}")
        return ", ".join(infos)
    

class ServoVelocityValue(ComponentValue):
    def __init__(self, meta_data):
        meta_data["type_name"] = "servo velocity"
        meta_data["description"] = "servo velocity value"

        meta_data["max_range"] = 100
        meta_data["min_range"] = -100
        super().__init__(meta_data)