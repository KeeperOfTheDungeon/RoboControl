import warnings
from asyncio import sleep
import math
import threading
from serial import Serial

from RoboControl.Com.ComStatistic import ComStatistic
from RoboControl.Com.Connection import RemoteDataInput, RemoteDataOutput
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.RemoteData import RemoteData, RemoteCommand, RemoteMessage, RemoteNegativeAck, RemotePositiveAck, RemoteStream

from RoboControl.Com.RemoteDataPacket import RemoteCommandDataPacket, RemoteMessageDataPacket, RemoteStreamDataPacket





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
            remote_data = RemoteCommand(0,  "")
        elif message_type == MESSAGE_START_TOKEN_STR:
            remote_data = RemoteMessage(0,  "")
        elif message_type == STREAM_START_TOKEN_STR:
            remote_data = RemoteStream(0,  "")
        elif message_type == OK_START_TOKEN_STR:
            remote_data = RemotePositiveAck(0,  "")
        elif message_type == FAIL_START_TOKEN_STR:
            remote_data = RemoteNegativeAck(0,  "")
        if remote_data:
            if parsed_remote_data := self.do_decode(remote_data):
                return parsed_remote_data

        print("UNSYNC")
        return RemoteData(0, "")

    def get_byte(self, offset: int, length: int = SIZE_PARAM):
        if offset + length >= len(self._data_buffer):
            print(f"Data Buffer is too small to parse bytes {offset}-{offset + length}")
            return None
        return int(self._data_buffer[offset:offset + length], 8 * SIZE_PARAM)

 
    def do_decode(self, remote_data: RemoteData):
        content_size = len(self._data_buffer) - 2  # minus start & end tokens
        raw_payload_size = content_size - OFFSET_PAYLOAD
        if content_size < (OFFSET_ID + SIZE_PARAM):
            print("Data Buffer is too small to parse the command id.", remote_data)
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


def parse_ascii(data_buffer: bytearray):
    if isinstance(data_buffer, str):
        _b = bytearray()
        _b.extend(data_buffer.encode("utf-8"))
        data_buffer = _b
    if len(data_buffer) % 2 != 0:
        return None
    if data_buffer[-1] != ord(END_TOKEN):
        print("END_TOKEN not available")
        return None


    destination_address: int = get_byte(data_buffer, 1)
    source_address: int = get_byte(data_buffer, 3)
    command: int = get_byte(data_buffer, 5)
    first_token = data_buffer[0]

    if first_token not in [ord(t) for t in [
        COMMAND_START_TOKEN,  # DataPacketType.COMMAND
        MESSAGE_START_TOKEN,  # DataPacketType.MESSAGE
        STREAM_START_TOKEN,  # DataPacketType.STREAM
        OK_START_TOKEN,  # DataPacketType.OK
        FAIL_START_TOKEN  # DataPacketType.FAIL
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


    return data_packet


class AsciiOutput(RemoteDataOutput):
    def __init__(self, serial_output: Serial, statistic: ComStatistic):
        super().__init__(statistic)
        self._output_stream: Serial = serial_output

        self._data_out_buffer = bytearray(256)
        self.out_byte_pointer = 0

    def transmitt(self, data_packet: RemoteDataPacket) -> bool:
        if not self._output_stream or not self._output_stream.is_open:
            print("Can't transmit as _output_stream isn't open.")
            return False
        # print("transmit:")
        # print("\n".join(["|  " + line for line in str(data_packet).splitlines()]))
        # print("\n".join(["|  |  " + line for line in str(data_packet.get_remote_data()).splitlines()]))
        # data_packet.set_source_address(1)
        self._packet_queue.append(data_packet)

        self.transmitt_packet(data_packet)
        return True

    def transmitt_packet(self, data_packet: RemoteDataPacket):
        ascii_data = DataPacketAscii()
        ascii_data.encode(data_packet)
        self.send(ascii_data)
        print(
            data_packet.get_type(),
            data_packet.get_remote_data().get_name(),
            data_packet.get_source_address(), "->", data_packet.get_destination_address(),
            data_packet.get_parameters_as_string(True),
            ": " + str(ascii_data.get_ascii_buffer())
        )

    def send(self, ascii_data):
        self._output_stream.write(ascii_data.get_ascii_buffer())

    @staticmethod
    def get_hex_hi_value(data_byte: int) -> int:  # Byte
        return AsciiOutput.get_hex_lo_value(data_byte >> 4)

    @staticmethod
    def get_hex_lo_value(data_byte: int) -> int:  # Byte
        value = data_byte & 0x0f
        if value > 9:
            value += 0x37
        else:
            value += 0x30
        return value

    def send_byte(self, token: int) -> bool:  # Byte
        self.send_token(self.get_hex_hi_value(token))
        self.send_token(self.get_hex_lo_value(token))
        return True

    def send_token(self, token: int) -> bool:  # Byte
        if self._output_stream is not None:
            self._data_out_buffer[self.out_byte_pointer] = token
            self.out_byte_pointer += 1
            self.statistic.count_up_sent_chars()
        return True

    def transmit(self, data_packet: RemoteDataPacket) -> bool:
        # TODO "transmit exception -> break & error !!"
        self.out_byte_pointer = 0
        # packet_type = data_packet.get_type()
        if isinstance(data_packet, RemoteCommandDataPacket):  # DataPacketType.COMMAND
            self.send_token(DataPacketAscii.COMMAND_START_TOKEN)
        elif isinstance(data_packet, RemoteMessageDataPacket):  # DataPacketType.MESSAGE
            self.send_token(DataPacketAscii.MESSAGE_START_TOKEN)
        elif isinstance(data_packet, RemoteStreamDataPacket):  # DataPacketType.STREAM
            self.send_token(DataPacketAscii.STREAM_START_TOKEN)
        else:
            raise ValueError("Trying to transmit an invalid packet type.")
        self.send_byte(data_packet.get_destination_address())
        self.send_byte(data_packet.get_source_address())
        self.send_byte(data_packet.get_command())
        for index in range(0, len(data_packet.get_data())):
            self.send_byte(data_packet.get_byte(index))
        self.send_token(DataPacketAscii.END_TOKEN)
        self.statistic.count_up_sent_packet_chars()

        self._output_stream.write(self._data_out_buffer)


class AsciiInput(RemoteDataInput):

    def __init__(self, serial_input: Serial, statistic: ComStatistic):
        super().__init__(statistic)
        self._serial_input = serial_input

    def run_threaded(self):
        self.running = True
        x = threading.Thread(target=self.run)
        x.start()

    def run(self) -> None:
        print("x is running")

        receiving_packet = False
        ascii_data_packet = DataPacketAscii()

        while self.running:
            # try
            while (
                    self.running and self._serial_input
                    and self._serial_input.is_open
                    and self._serial_input.in_waiting < 1
            ):
                warnings.filterwarnings('ignore', category=RuntimeWarning)
                sleep(0.001)

            if not self.running:
                break

            self.statistic.count_up_recived_chars(1)

            token = self._serial_input.read(1)

            if DataPacketAscii.is_start_token(token):
                if receiving_packet:
                    self.statistic.count_up_error_packets()
                receiving_packet = True
                ascii_data_packet = DataPacketAscii()

            ascii_data_packet.put_token(token)

            if DataPacketAscii.is_end_token(token):
                if not receiving_packet:
                    self.statistic.count_up_error_packets(1)
                    continue
                remote_data = ascii_data_packet.decode()
                # data_packet_buffer = copy(data_packet._data_buffer)
                # data_packet = DataPacketAscii.parse_ascii(data_packet_buffer)

                # self.deliver_packet(remote_data)
                data_packet = remote_data.get_data_packet()
                self.deliver_packet(data_packet)

                self.statistic.count_up_recived_packets(1)
                receiving_packet = False
                ascii_data_packet = DataPacketAscii()

 

