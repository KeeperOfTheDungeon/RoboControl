import datetime


# from RoboControl.Com.PacketLogger.LoggedDataPacket import DisplayDataWidth_e, render_data

# from RoboControl.Com.PacketLogger.LoggedDataPacket import render_data, DisplayDataWidth_e


class DataPacketType:
    COMMAND = "COMMAND"
    MESSAGE = "MESSAGE"
    STREAM = "STREAM"
    EXCEPTION = "EXCEPTION"
    # TODO typo in alert
    ALLERT = "ALLERT"
    OK = "OK"
    FAIL = "FAIL"
    INVALID = "INVALID"
    GENERIC = "GENERIC"


class RemoteDataPacket:
    _type_name: str = "generic remote command"
    _type: DataPacketType = DataPacketType.GENERIC

    def __init__(
            self, destination_address: int, source_address: int, command: int,
            data_size: int = None, override_type: DataPacketType = None
    ):
        self._destination_address = destination_address  # default =? 0
        self._source_address = source_address  # default =? 0
        self._id = command  # default =? 0
        self._timestamp = datetime.datetime.now()

        self.data: bytearray = bytearray(data_size) if data_size else bytearray()

        self._remote_data = None

        self._type = override_type or self._type

    def set_source_address(self, source_address: int):
        self._source_address = source_address

    def set_destination_address(self, destination_address: int):
        self._destination_address = destination_address

    def get_source_address(self) -> int:
        return self._source_address

    def get_destination_address(self) -> int:
        return self._destination_address

    def allocate(self, size: int) -> None:
        self.data = bytearray(size)

    def set_byte(self, position: int, value: int) -> None:
        """ set a byte in payload array
        version :1.0
        date : 2022.02.01
        author dungeon keeper
        """
        self.data[position] = value

    def get_byte(self, position):
        """ get a byte from payload array
        version :1.0
        date : 2022.02.01
        author dungeon keeper
        """
        return self.data[position]

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_int_16(self, position: int, value: int) -> None:
        self.data[position] = value >> 8
        self.data[position + 1] = value & 0xff

    def get_int_16(self, position: int) -> int:
        if (position + 1) >= len(self.data):
            return 0
        value = (self.data[position] << 8) & 0xff00
        value |= self.data[position + 1] & 0xff
        return value

    def set_int_24(self, position: int, value: int) -> None:
        self.data[position] = (value >> 16) & 0xff
        self.data[position + 1] = (value >> 8) & 0xff
        self.data[position + 2] = value & 0xff

    def get_int_24(self, position: int) -> int:
        if (position + 2) >= len(self.data):
            return 0
        value = (self.data[position] << 16) & 0xff0000
        value |= (self.data[position + 1] << 8) & 0xff00
        value |= self.data[position + 2] & 0xff
        return value

    def set_int_32(self, position: int, value: int) -> None:
        self.data[position] = (value >> 24) & 0xff
        self.data[position + 1] = (value >> 16) & 0xff
        self.data[position + 2] = (value >> 8) & 0xff
        self.data[position + 3] = value & 0xff

    def get_int_32(self, position: int) -> int:
        if (position + 3) >= len(self.data):
            # TODO does this make sense
            return 0
        value = (self.data[position] << 24) & 0xff000000
        value |= (self.data[position + 1] << 16) & 0xff0000
        value |= (self.data[position + 2] << 8) & 0xff00
        value |= self.data[position + 3] & 0xff
        return value

    def get_type_name(self) -> str:
        return self._type_name

    def get_id(self) -> int:
        return self._id

    def get_parameters_as_string(self, description: bool) -> str:
        return self._remote_data.get_parameters_as_string(description) if self.has_remote_data() else ""

    def set_remote_data(self, remote_data) -> None:
        self._remote_data = remote_data

    def get_remote_data(self):
        return self._remote_data

    def get_data_size(self) -> int:
        return len(self.data)

    def get_type(self) -> DataPacketType:
        return self._type

    def __str__(self) -> str:
        # return "null" if self._type is None else str(self._type)
        res = f"RemoteDataPacket({self._id})"
        res += f"\n\t(source) {self._source_address} -> {self._destination_address} (destination)"
        # res += f"\n\tdata: {render_data(self, DisplayDataWidth_e.WIDTH_8, True)}" #dont work with pico
        res += f"\n\tremote_data: " + str(self._remote_data).split("\n")[0].strip()
        return res

    def get_bit(self, position: int, bit: int):
        bit_mask = (1 << bit)
        return (self.data[position] & bit_mask) > 0

    # def get_data_buffer(self) -> bytebuffer:
    #    return bytebuffer(self.data)

    def has_remote_data(self):
        return self._remote_data is not None

    def get_timestamp(self):
        return self._timestamp

    def get_payload(self):
        return self.get_remote_data().get_payload()


class RemoteCommandDataPacket(RemoteDataPacket):
    _type_name: str = "remote command"
    _type: DataPacketType = DataPacketType.COMMAND


class RemoteMessageDataPacket(RemoteDataPacket):
    _type_name: str = "remote message"
    _type: DataPacketType = DataPacketType.MESSAGE


class RemoteStreamDataPacket(RemoteDataPacket):
    _type_name: str = "remote stream data"
    _type: DataPacketType = DataPacketType.STREAM


class RemoteExceptionDataPacket(RemoteDataPacket):
    _type_name: str = "remote exception"
    _type: DataPacketType = DataPacketType.EXCEPTION


class RemotePositiveAckDataPacket(RemoteDataPacket):
    _type_name: str = "remote ok"
    _type: DataPacketType = DataPacketType.OK


class RemoteNegativeAckDataPacket(RemoteDataPacket):
    _type_name: str = "remote fail"
    _type: DataPacketType = DataPacketType.FAIL  #
