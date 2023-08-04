import traceback
from typing import List, Optional, TypeAlias

from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream

# TODO "make enum"
COMMAND_START_TOKEN = 0x1FA

MESSAGE_START_TOKEN = 0x1FB

STREAM_START_TOKEN = 0x1FC

EXCEPTION_START_TOKEN = 0x1F3
ALLERT_START_TOKEN = 0x1F4

OK_START_TOKEN = 0x1FD
FAIL_START_TOKEN = 0x1FE
END_TOKEN = 0x1FF

BUFFER_OFFSET_MESSAGE_TYPE = 0
BUFFER_OFFSET_DEST_ADDRESS = 1
BUFFER_OFFSET_SRC_ADDRESS = 2
BUFFER_OFFSET_ID = 3
BUFFER_OFFSET_PAYLOAD = 4

Byte: TypeAlias = int


class DataPacketPico(RemoteDataPacket):

    # TODO why does this inherit from RemoteDataPacket without forwarding init
    def __init__(self):  # noqa
        self._token_counter = 0
        self._data_buffer = []
        pass

    def decode(self) -> RemoteData:
        message_type = self._data_buffer[0]

        if message_type == COMMAND_START_TOKEN:
            print("Message sync")
            remote_data = RemoteCommand(0, "", "")
            self.do_decode(remote_data)
        elif message_type == MESSAGE_START_TOKEN:
            print("Message sync")
            remote_data = RemoteMessage(0, "", "")
            self.do_decode(remote_data)
        elif message_type == STREAM_START_TOKEN:
            print("Stream sync")
            remote_data = RemoteStream(0, "", "")
            self.do_decode(remote_data)
        else:
            print("unsync")
            remote_data = RemoteData(0, "", "")

        return remote_data

    def do_decode(self, remote_data: RemoteData) -> None:
        remote_data._destination_address = int(self._data_buffer[BUFFER_OFFSET_DEST_ADDRESS], 16)
        remote_data._source_address = int(self._data_buffer[BUFFER_OFFSET_SRC_ADDRESS], 16)
        remote_data._id = int(self._data_buffer[BUFFER_OFFSET_ID], 16)

        data_size = len(self._data_buffer) - (BUFFER_OFFSET_PAYLOAD + 1)

        payload = bytearray(int(data_size)) # TODO make with RemoteData class compatible
        index = 0
        while (index + BUFFER_OFFSET_PAYLOAD) < (len(self._data_buffer) - 1):
            value = int(self._data_buffer[index + BUFFER_OFFSET_PAYLOAD], 16)
            payload[index] = value
            index += 1

        remote_data.set_payload(payload)


    # TODO camelcase
    def putToken(self, token):  # noqa
        self._data_buffer.append(token)
        self._token_counter += 1

        return token == END_TOKEN

    def code(self, data_packet: RemoteDataPacket):
        remote_data = data_packet.get_remote_data()
        frame_size = remote_data.get_payload_size()
        frame_size += BUFFER_OFFSET_PAYLOAD + 1 # one extra for the end byte

        self._data_buffer = bytearray(frame_size)

        # command mark
        if isinstance(remote_data, RemoteCommand):
            self._data_buffer[BUFFER_OFFSET_MESSAGE_TYPE] = COMMAND_START_TOKEN
        elif isinstance(remote_data, RemoteMessage):
            self._data_buffer[BUFFER_OFFSET_MESSAGE_TYPE] = MESSAGE_START_TOKEN
        print(type(remote_data))

        self._data_buffer[BUFFER_OFFSET_DEST_ADDRESS] = remote_data.get_destination_address()
        self._data_buffer[BUFFER_OFFSET_SRC_ADDRESS] = remote_data.get_source_address()
        self._data_buffer[BUFFER_OFFSET_ID] = remote_data.get_id()
        # send Data payload

        self._data_buffer[len(self._data_buffer) - 1] = END_TOKEN
        index = BUFFER_OFFSET_PAYLOAD
        for parameter in remote_data.get_parameter_list():
            buffer = parameter.get_as_buffer()
            for byte in buffer:
                self._data_buffer[index] = byte
                index += 1

    def get_buffer(self):
        return self._data_buffer



def parse_ascii(data_buffer: List[Byte]) -> Optional[RemoteDataPacket]:
    if len(data_buffer) % 2 != 0:
        return None
    if data_buffer[-1] != END_TOKEN:
        return None

    try:
        destination_address: Byte = get_byte(data_buffer, 1)
        source_address: Byte = get_byte(data_buffer, 3)
        command: Byte = get_byte(data_buffer, 5)
        first_token = data_buffer[0]
        if first_token not in [COMMAND_START_TOKEN,
                               MESSAGE_START_TOKEN,
                               STREAM_START_TOKEN,
                               OK_START_TOKEN,
                               FAIL_START_TOKEN]:
            return None
        data_packet = RemoteDataPacket(destination_address, source_address, command)
        data_packet_size = (len(data_buffer) - 8) / 2
        data_packet.alocate(data_packet_size)

        data_index = 0
        for index in range(7, len(data_buffer) - 1, 2):
            value = get_byte(data_buffer, index)
            data_packet.set_byte(data_index, value)
            data_index += 1

    except Exception as e:
        traceback.print_exception(e)
        return None
    return data_packet
