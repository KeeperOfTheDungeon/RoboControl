


class ComponentValue:
    def __init__(self, meta_data: dict):
        self._name: str = meta_data.get("name", "generic")
        self._type_name: str = meta_data.get("type_name", "generic")
        self._description: str = meta_data.get("description", "generic")

        self._max_range: float = meta_data["max_range"]  # sys.sys.float_info.max
        self._min_range: float = meta_data["min_range"]  # sys.sys.float_info.min
        self._value: float = 0

        self._overflow: bool = False
        self._underflow: bool = False
        self._valid: bool = False

        self._notifyAllways: bool = True
        self._value_changed_listener_list = list()  # this.listeners

    def set_name(self, name: str):
        self._name = name

    def get_name(self) -> str:
        return self._name

    def has_name(self, name) -> bool:
        return self._name == name

    def get_type_name(self) -> str:
        return self._type_name

    def get_type_description(self) -> str:
        return self._description

    def set_range(self, min_range: float, max_range: float) -> None:
        """ "set minimum und maximum range of this float value" """
        self._max_range = max_range
        self._min_range = min_range

    def get_min_range(self) -> float:
        return self._min_range

    def get_max_range(self) -> float:
        return self._max_range

    def set_overflow_value(self) -> None:
        self._value = self._max_range
        self._overflow = True
        self._underflow = False
        self._valid = True

    def set_underflow_value(self) -> None:
        self._value = self._min_range
        self._overflow = False
        self._underflow = True
        self._valid = True

    def set_value(self, value):
        value_changed = False

        if self._notifyAllways:
            value_changed = True
        elif value != self._value:
            value_changed = True

        if value > self._max_range:
            self.set_overflow_value()
        elif value < self._min_range:
            self.set_underflow_value()
        else:
            self._overflow = False
            self._underflow = False
            self._value = value
            self._valid = True

        if value_changed:
            self.notify_value_changed()
        return self._value

    def get_value(self) -> float:
        return self._value

    def is_valid(self) -> bool:
        return self._valid

    def add_listener(self, listener):
        self._value_changed_listener_list.append(listener)

    def remove_listener(self, listener):
        self._value_changed_listener_list.remove(listener)

    def notify_value_changed(self):
        for listener in self._value_changed_listener_list:
            listener.component_value_changed(self)

    def actualize(self):
        return False

    def __str__(self):
        return self._name

    @staticmethod
    def to_formated_fraction_string(value: float, fraction: int) -> str:
        # TODO why not just fstring?
        value_as_string = str(value)
        separator_index = value_as_string.index('.')
        fraction_size = len(value_as_string) - separator_index
        if fraction_size > fraction:
            fraction_size = fraction + 1
        return value_as_string[0:separator_index + fraction_size]
