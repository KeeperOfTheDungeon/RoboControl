from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter


class RemoteParameterInt(RemoteParameter):
    _value: int

    def __init__(self, name, description, min_value, max_value, size):
        super().__init__(name, description, size)
        self._min_value = min_value
        self._max_value = max_value
        self._value = 0

    def set_value(self, value: int) -> None:
        if value > self._max_value:
            value = self._max_value
        elif value < self._min_value:
            value = self._min_value
        self._value = value

    def get_value(self) -> int:
        return self._value

    def to_string(self) -> str:
        return self._name + str(self._value)
