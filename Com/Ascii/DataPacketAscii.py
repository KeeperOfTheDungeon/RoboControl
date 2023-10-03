import math
import traceback
from typing import Optional

from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteNegativeAck import RemoteNegativeAck
from RoboControl.Com.Remote.RemotePositiveAck import RemotePositiveAck
from RoboControl.Com.Remote.RemoteStream import RemoteStream

from logger import getLogger

logger = getLogger(__name__)


# TODO "make enum"
COMMAND_START_TOKEN = b'#'
COMMAND_START_TOKEN_STR = str(chr(ord(COMMAND_START_TOKEN)))

MESSAGE_START_TOKEN = b'*'
MESSAGE_START_TOKEN_STR = str(chr(ord(MESSAGE_START_TOKEN)))

STREAM_START_TOKEN = b'$'
STREAM_START_TOKEN_STR = str(chr(ord(STREAM_START_TOKEN)))

EXCEPTION_START_TOKEN = b'^'
ALLERT_START_TOKEN = b'!'

OK_START_TOKEN = b'O'
OK_START_TOKEN_STR = str(chr(ord(OK_START_TOKEN)))
FAIL_START_TOKEN = b'N'
FAIL_START_TOKEN_STR = str(chr(ord(FAIL_START_TOKEN)))

END_TOKEN = b';'

OFFSET_DESTINATION = 1
OFFSET_SOURCE = 3
OFFSET_ID = 5
OFFSET_PAYLOAD = 7

SIZE_PARAM = 2


class DataPacketAscii:

    # TODO why does this inherit from RemoteDataPacket without forwarding init
    def __init__(self):  # noqa
        self._token_counter = 0
        self._data_buffer = ""

    def decode(self) -> RemoteData:
        # print(self.data_buffer)
        index = 0
        message_type = self._data_buffer[index]
        remote_data = None
        if message_type == COMMAND_START_TOKEN_STR:
            remote_data = RemoteCommand(0, "", "")
        elif message_type == MESSAGE_START_TOKEN_STR:
            remote_data = RemoteMessage(0, "", "")
        elif message_type == STREAM_START_TOKEN_STR:
            remote_data = RemoteStream(0, "", "")
        elif message_type == OK_START_TOKEN_STR:
            remote_data = RemotePositiveAck(0, "", "")
        elif message_type == FAIL_START_TOKEN_STR:
            remote_data = RemoteNegativeAck(0, "", "")
        if remote_data:
            if parsed_remote_data := self.do_decode(remote_data):
                return parsed_remote_data

        self.error("UNSYNC")
        return RemoteData(0, "", "")

    def get_byte(self, offset: int, length: int = SIZE_PARAM):
        if offset + length >= len(self._data_buffer):
            self.error(f"Data Buffer is too small to parse bytes {offset}-{offset + length}")
            return None
        return int(self._data_buffer[offset:offset + length], 8 * SIZE_PARAM)

    def error(self, message: str, remote_data: RemoteData = None):
        logger.warning(message)
        logger.warning(self)
        logger.warning(remote_data)

    def do_decode(self, remote_data: RemoteData) -> "Optional[RemoteData]":
        content_size = len(self._data_buffer) - 2  # minus start & end tokens
        raw_payload_size = content_size - OFFSET_PAYLOAD
        if content_size < (OFFSET_ID + SIZE_PARAM):
            self.error("Data Buffer is too small to parse the command id.", remote_data=remote_data)
            return None
        remote_data.set_destination_address(self.get_byte(OFFSET_DESTINATION))
        remote_data.set_source_address(self.get_byte(OFFSET_SOURCE))
        remote_data.set_id(self.get_byte(OFFSET_ID))

        parsed_payload_size = math.ceil(raw_payload_size / SIZE_PARAM)
        payload = bytearray(parsed_payload_size)

        for param_index in range(0, raw_payload_size, SIZE_PARAM):
            value = self.get_byte(OFFSET_PAYLOAD + param_index)
            if value is None:
                break
            payload_index = math.floor(param_index / SIZE_PARAM)
            payload[payload_index] = value

        remote_data.set_payload(payload)

        # error - exception
        return remote_data

    def put_token(self, token) -> None:
        self._data_buffer += str(token, 'utf-8')
        self._token_counter += 1

    def encode(self, data_packet: RemoteDataPacket):
        remote_data = data_packet.get_remote_data()
        payload_size = remote_data.get_payload_size() * 2
        payload_size += 8

        self._data_buffer = bytearray(payload_size)

        index = 0

        # command mark
        if isinstance(remote_data, RemoteCommand):
            self._data_buffer[index] = ord(COMMAND_START_TOKEN)
        elif isinstance(remote_data, RemoteMessage):
            self._data_buffer[index] = ord(MESSAGE_START_TOKEN)

        #print(type(remote_data))
        index += 1

        destination = remote_data.get_destination_address()
        self._data_buffer[index] = get_char(destination >> 4)
        index += 1
        self._data_buffer[index] = get_char(destination & 0xf)
        index += 1

        source = remote_data.get_source_address()
        self._data_buffer[index] = get_char(source >> 4)
        index += 1
        self._data_buffer[index] = get_char(source & 0xf)
        index += 1

        command = remote_data.get_id()
        self._data_buffer[index] = get_char(command >> 4)
        index += 1
        self._data_buffer[index] = get_char(command & 0xf)
        index += 1

        # send Data payload

        self._data_buffer[len(self._data_buffer) - 1] = ord(END_TOKEN)

        for parameter in remote_data.get_parameter_list():
            buffer = parameter.get_as_buffer()
            for byte in buffer:
                self._data_buffer[index] = get_char(byte >> 4)
                index += 1
                self._data_buffer[index] = get_char(byte & 0xf)
                index += 1

    def get_ascii_buffer(self):
        return self._data_buffer

    @staticmethod
    def is_start_token(token) -> bool:
        return token in [
            COMMAND_START_TOKEN,
            MESSAGE_START_TOKEN,
            STREAM_START_TOKEN,
            OK_START_TOKEN,
            FAIL_START_TOKEN,
        ]

    @staticmethod
    def is_end_token(token) -> bool:
        return token == END_TOKEN


def get_char(data_byte):
    if data_byte > 9:
        value = data_byte + 0x37
    else:
        value = data_byte + 0x30
    return value


def hex_char_to_nibble(data_byte: int) -> int:
    if (data_byte > 0x40) & (data_byte < 0x47):
        data_byte -= 0x37
    elif (data_byte > 0x60) & (data_byte < 0x67):
        data_byte -= 0x57
    elif (data_byte > 0x2f) & (data_byte < 0x3a):
        data_byte -= 0x30
    else:
        raise ValueError(f"ConversionException(databyte) for {data_byte}")
    return data_byte


def get_byte(buffer: bytearray, position: int) -> int:
    hi = hex_char_to_nibble(buffer[position]) << 4
    lo = hex_char_to_nibble(buffer[position + 1])
    return hi + lo


def parse_ascii(data_buffer: bytearray) -> Optional[RemoteDataPacket]:
    if isinstance(data_buffer, str):
        _b = bytearray()
        _b.extend(data_buffer.encode("utf-8"))
        data_buffer = _b
    if len(data_buffer) % 2 != 0:
        return None
    if data_buffer[-1] != ord(END_TOKEN):
        print("END_TOKEN not available")
        return None

    try:
        destination_address: int = get_byte(data_buffer, 1)
        source_address: int = get_byte(data_buffer, 3)
        command: int = get_byte(data_buffer, 5)
        first_token = data_buffer[0]
        """
        if first_token == COMMAND_START_TOKEN:
            packet_type = DataPacketType.COMMAND
        elif first_token == MESSAGE_START_TOKEN:
            packet_type = DataPacketType.MESSAGE
        elif first_token == STREAM_START_TOKEN:
            packet_type = DataPacketType.STREAM
        elif first_token == OK_START_TOKEN:
            packet_type = DataPacketType.OK
        elif first_token == FAIL_START_TOKEN:
            packet_type = DataPacketType.FAIL
        """
        if first_token not in [ord(t) for t in [
            COMMAND_START_TOKEN,
            MESSAGE_START_TOKEN,
            STREAM_START_TOKEN,
            OK_START_TOKEN,
            FAIL_START_TOKEN
        ]]:
            print("first_token", first_token)
            return None
        data_packet = RemoteDataPacket(destination_address, source_address, command)
        data_packet_size = math.ceil((len(data_buffer) - 8) / 2)
        data_packet.allocate(data_packet_size)

        data_index = 0
        for index in range(7, len(data_buffer) - 1, 2):
            value = get_byte(data_buffer, index)
            data_packet.set_byte(data_index, value)
            data_index += 1

    except Exception as e:
        print(traceback.format_exc())
        traceback.print_exception(e)
        return None
    return data_packet

