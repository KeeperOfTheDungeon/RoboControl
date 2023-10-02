from RoboControl.Robot.Math.Radiant import Radiant
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.RadiantValue import RadiantValue


class ServoPositionValue(RadiantValue):  # ServoAngleValue
    _is_at_max: bool
    _is_at_min: bool

    _is_active: bool
    _is_on: bool

    _is_inverse: bool
    _is_stalling: bool

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

    def on_change(self, source: ComponentValue) -> None:
        # if source == self._min_servo_range:
        # 	self._min_range = source.get_value()
        # elif source == self._max_servo_range:
        # 	self._max_range = source.get_value()
        self.set_value(source.get_value())
