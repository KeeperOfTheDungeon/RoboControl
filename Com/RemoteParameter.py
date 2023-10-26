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
    
class RemoteParameterInt8(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, -128, 127, 1)

    def put_data(self, data_buffer):
        data_buffer.append(self._value + 128)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index] - 128
        return self._byte_size

    def get_as_buffer(self):
        buffer = bytearray(self._byte_size)
        buffer[0] = self._value

        return buffer
    
class RemoteParameterUint8(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, 0, 0xff, 1)

    def put_data(self, data_buffer):
        data_buffer.append(self._value)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index]
        return self._byte_size

    def get_as_buffer(self):
        buffer = bytearray(self._byte_size)
        buffer[0] = self._value

        return buffer
    
class RemoteParameterInt16(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, -0x8000, 0x7fff, 2)

    def put_data(self, data_buffer):
        data_buffer.append(self._value + 0x8000)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index] << 8
        self._value |= data_buffer[index + 1]

        self._value -= 0x8000
        return self._byte_size
    
class RemoteParameterUint16(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, 0, 0xffff, 2)

    def put_data(self, data_buffer):
        data_buffer.append((self._value & 0xff00) >> 8)
        data_buffer.append(self._value & 0xff)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index] << 8
        self._value |= data_buffer[index + 1]
        return self._byte_size
    
class RemoteParameterInt24(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, -0x800000, 0x7fffff, 3)

    def put_data(self, data_buffer):
        data_buffer.append(self._value + 0x800000)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index + 1] << 16
        self._value |= data_buffer[index + 2] << 8
        self._value |= data_buffer[index + 3]

        self._value -= 0x800000
        return self._byte_size
    

class RemoteParameterUint24(RemoteParameterInt):
    def __init__(self, name, description):
        super().__init__(name, description, 0, 0xffffff, 3)

    def put_data(self, data_buffer):
        data_buffer.append((self._value & 0xff0000) >> 16)
        data_buffer.append((self._value & 0xff00) >> 8)
        data_buffer.append(self._value & 0xff)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index] << 16
        self._value |= data_buffer[index + 1] << 8
        self._value |= data_buffer[index + 2]
        return self._byte_size
    

class RemoteParameterInt32(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, -0x80000000, 0x7fffffff, 4)

    def put_data(self, data_buffer):
        data_buffer.append(self._value + 0x80000000)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index] << 24
        self._value |= data_buffer[index + 1] << 16
        self._value |= data_buffer[index + 2] << 8
        self._value |= data_buffer[index + 3]

        self._value -= 0x80000000
        return self._byte_size
    
class RemoteParameterUint32(RemoteParameterInt):

    def __init__(self, name, description):
        super().__init__(name, description, 0, 0xffffffff, 4)

    def put_data(self, data_buffer):
        data_buffer.append((self._value & 0xff000000) >> 24)
        data_buffer.append((self._value & 0xff0000) >> 16)
        data_buffer.append((self._value & 0xff00) >> 8)
        data_buffer.append(self._value & 0xff)

    def parse_from_buffer(self, data_buffer, index):
        self._value = data_buffer[index] << 24
        self._value |= data_buffer[index + 1] << 16
        self._value |= data_buffer[index + 2] << 8
        self._value |= data_buffer[index + 3]
        return self._byte_size