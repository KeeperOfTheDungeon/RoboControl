#import datetime
#from enum import Enum
#from typing import Optional

#from RoboControl.Com.PacketLogger.LoggedDataPacket import render_data, DisplayDataWidth_e


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
    _type_name: str = "generic"
    _type: DataPacketType = DataPacketType.GENERIC

    # _source_address = 0
    # destination_address = 0
    # command  = 0
    # reply  = 0

    def __init__(self, destination_address: int, source_address: int, command: int):
        self._destination_address = destination_address
        self._source_address = source_address
        self._command = command
        self._timestamp = datetime.datetime.now()

        self.data = None

        self._remote_data: Optional["RemoteData"] = None

    def set_source_address(self, source_address: int):
        self._source_address = source_address

    def set_destination_address(self, destination_address: int):
        self._destination_address = destination_address

    def get_source_address(self):
        return self._source_address

    def get_destination_address(self):
        return self._destination_address

    def alocate(self, size):
        self.data = bytearray(size)

    def do_decode(self, remote_data: "RemoteData") -> None:  # data_buffer
        pass

    def decode(self) -> "RemoteData":
        pass

    def code(self, data_packet):
        pass

    def set_byte(self, position, value):
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

    def set_int_16(self, position, value):
        self.data[position] = value >> 8
        self.data[position + 1] = value & 0xff

    def get_int_16(self, position):
        if (position + 1) >= len(self.data):
            # TODO does this make sense
            return 0
        value = (self.data[position] << 8) & 0xff00
        value |= self.data[position + 1] & 0xff
        return value

    def set_int_24(self, position, value):
        self.data[position] = (value >> 16) & 0xff
        self.data[position + 1] = (value >> 8) & 0xff
        self.data[position + 2] = value & 0xff

    def get_int_24(self, position):
        if (position + 2) >= len(self.data):
            # TODO does this make sense
            return 0
        value = (self.data[position] << 16) & 0xff0000
        value |= (self.data[position + 1] << 8) & 0xff00
        value |= self.data[position + 2] & 0xff
        return value

    def set_int_32(self, position, value):
        self.data[position] = (value >> 24) & 0xff
        self.data[position + 1] = (value >> 16) & 0xff
        self.data[position + 2] = (value >> 8) & 0xff
        self.data[position + 3] = value & 0xff

    def get_int_32(self, position):
        if (position + 3) >= len(self.data):
            # TODO does this make sense
            return 0
        value = (self.data[position] << 24) & 0xff000000
        value |= (self.data[position + 1] << 16) & 0xff0000
        value |= (self.data[position + 2] << 8) & 0xff00
        value |= self.data[position + 3] & 0xff
        return value

    def get_type_name(self) -> str:
        # TODO this should use the type enum
        return self._type_name

    def get_command(self):
        return self._command

    def get_timestamp(self) -> datetime.datetime:
        return self._timestamp

    def get_parameters_as_string(self, description: bool) -> str:
        return self._remote_data.get_parameters_as_string(description)

    def set_remote_data(self, remote_data: "RemoteData") -> None:
        self._remote_data = remote_data

    def get_remote_data(self) -> "RemoteData":
        return self._remote_data

    def get_data_size(self) -> int:
        return len(self.data)

    def get_type(self) -> DataPacketType:
        return self._type

    def __str__(self) -> str:
        res = f"RemoteDataPacket({self._command})"
        res += f"\n\t(source) {self._source_address} -> {self._destination_address} (destination)"
        res += f"\n\tdata: {render_data(self, DisplayDataWidth_e.WIDTH_8, True)}"
        res += f"\n\tremote_data: " + str(self._remote_data).split("\n")[0].strip()
        return res
