import datetime
from enum import Enum
from typing import Optional


class LoggedDataPacketType(str, Enum):
    IN = "in"
    OUT = "out"


# noinspection PyPep8Naming
class DisplayDataWidth_e(str, Enum):
    WIDTH_8 = "WIDTH_8"
    WIDTH_16 = "WIDTH_16"
    WIDTH_24 = "WIDTH_24"
    WIDTH_32 = "WIDTH_32"


# noinspection PyPep8Naming
class DisplayFormat_e(str, Enum):
    DECIMAL = "DECIMAL"
    HEXADECIMAL = "HEXADECIMAL"
    NATIVE = "NATIVE"
    NATIVE_WITH_DESCRIPTION = "NATIVE_WITH_DESCRIPTION"


class LoggedDataPacket:
    def __init__(self, data_packet: "RemoteDataPacket", data_packet_type: LoggedDataPacketType, number: int):
        self._data_packet = data_packet
        self._data_packet_type = data_packet_type
        self._number = number

    def get_data_packet(self) -> "RemoteDataPacket":
        return self._data_packet

    def get_destination(self) -> int:
        return self._data_packet.get_destination_address()

    def get_source(self) -> int:
        return self._data_packet.get_source_address()

    def get_command(self) -> int:
        return self._data_packet.get_command()

    def get_command_name(self) -> str:
        remote_data = self._data_packet.get_remote_data()
        if remote_data is None:
            return "undefined"
        answer = remote_data.get_name()
        return answer or "-"

    def get_type_name(self) -> str:
        remote_data = self._data_packet.get_remote_data()
        return "undefined" if remote_data is None else remote_data.get_type_name()

    def get_number(self) -> int:
        return self._number

    def get_timestamp(self) -> datetime.datetime:
        return self._data_packet.get_timestamp()

    def get_data_as_hex_string(self) -> str:  # noqa
        raise ValueError("WIP: self.get_data_as_hex_string() isn't implemented")
        """
        res = []
        for d in self._data_packet.data:
            r = Integer.to_hex_string(d)
            if len(r) == 1:
                r = "0" + r
            elif len(r) > 2:
                r = r[-2:]
            res.append(r)
        return ",".join(res)
        """

    def get_parameters_as_string(self, description: bool) -> str:
        return self._data_packet.get_parameters_as_string(description)

    def get_direction_as_string(self) -> Optional[str]:
        if isinstance(self._data_packet_type, LoggedDataPacketType):
            return self._data_packet_type.value
        return None

    def get_data_as_string(self, *args) -> str:
        return render_data(self._data_packet, *args)

    @staticmethod
    def get_data_as_hex_string_string24(*args) -> str:  # noqa
        raise ValueError("WIP: get_data_as_hex_string_string24 not implemented")
        """
        //2012.02.9
        public String getDataAsHexStringString24()
        {
            String returnString="";
            int index ;
            if (dataPacket.getDataSize()!=0) {
                for (index=0;index<dataPacket.getDataSize()-2;index+=3) {
                    if (index!=0) {
                        returnString+=",";
                    }
                    returnString += Integer.toHexString(dataPacket.getInt24(index));
                }
            }
            return(returnString);
        }
        """


def render_data(data_packet: "RemoteDataPacket", data_width: DisplayDataWidth_e = None, as_hexadecimal: bool = False) -> str:
    if data_packet.get_data() is None:
        return ""
    if not data_width:
        return ",".join(data_packet.data)
    res = []
    index = 0
    while index < len(data_packet.data):
        if data_width == DisplayDataWidth_e.WIDTH_8:
            value = data_packet.get_byte(index)
        elif data_width == DisplayDataWidth_e.WIDTH_16:
            value = data_packet.get_int_16(index)
            index += 1
        elif data_width == DisplayDataWidth_e.WIDTH_24:
            value = data_packet.get_int_24(index)
            index += 2
        elif data_width == DisplayDataWidth_e.WIDTH_32:
            value = data_packet.get_int_32(index)
            index += 3
        else:
            raise ValueError(f"Invalid data_width: {data_width}")
        if as_hexadecimal:
            res.append(hex(value))
        else:
            res.append(value)
        index += 1
    return ",".join([str(v) for v in res])
