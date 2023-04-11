from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii
from RoboControl.Com.Ascii.AsciiOutput import AsciiOutput
from RoboControl.Com.Ascii.AsciiInput import AsciiInput

import serial.tools.list_ports


class SerialConnection(Connection):

    def __init__(self):
        pass

    def connect(self, data_packet_receiver):
        ports = list(serial.tools.list_ports.comports())

        for p in ports:
            print(p[1])

        port = "COM3"

        self._serial_stream = serial.Serial(port, 115200)

        self._data_output = AsciiOutput(self._serial_stream)
        self._data_input = AsciiInput(self._serial_stream)
        super().connect(data_packet_receiver)

        pass
