import traceback

from serial import Serial

from RoboControl.Com.ComStatistic import ComStatistic
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput
from RoboControl.Com.Ascii import DataPacketAscii
from RoboControl.Com.Remote.RemoteCommandDataPacket import RemoteCommandDataPacket
from RoboControl.Com.Remote.RemoteMessageDataPacket import RemoteMessageDataPacket
from RoboControl.Com.Remote.RemoteStreamDataPacket import RemoteStreamDataPacket


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
        ascii_data = DataPacketAscii.DataPacketAscii()
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

        try:
            self._output_stream.write(self._data_out_buffer)
            # self._output_stream.flush()
        except Exception as e:
            print(traceback.format_exc())
            traceback.print_exception(e)
        return False
