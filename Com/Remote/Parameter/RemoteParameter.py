class RemoteParameter:
    def __init__(self, name: str, description: str, size: int):
        self._name = name
        self._description = description
        self._byte_size = size
        self._value: object = None

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_byte_size(self) -> int:
        return self._byte_size

    def get_as_buffer(self):
        raise ValueError("WIP RemoteParameter.get_as_buffer not yet implemented")

    def put_data(self, data_buffer):
        raise ValueError("WIP RemoteParameter.put_data not yet implemented")

    def parse_from_buffer(self, data_buffer, index):
        raise ValueError("WIP RemoteParameter.parse_from_buffer not yet implemented")

    def get_as_string(self, description: bool) -> str:
        if description:
            return self._name + "=" + str(self._value)
        return str(self._value)

    def set_value(self, value: object) -> None:
        self._value = value

    def get_value(self) -> object:
        return self._value

