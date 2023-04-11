from typing import TypeAlias, Callable, Optional

import serial.tools.list_ports
from serial import Serial

from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii
from RoboControl.Com.Ascii.AsciiOutput import AsciiOutput
from RoboControl.Com.Ascii.AsciiInput import AsciiInput

# FIXME what exactly are listeners?
Listener: TypeAlias = [Callable or any]


class SerialConnection(Connection):

    def __init__(self):
        super().__init__()

        # FIXME this isn't really optional is it
        self._serial_stream: Optional[Serial] = None

    def connect(self, data_packet_receiver: Listener) -> None:
        ports = list(serial.tools.list_ports.comports())

        for p in ports:
            print(p[1])

        port = "COM3"

        self._serial_stream = serial.Serial(port, 115200)

        self._data_output = AsciiOutput(self._serial_stream)
        self._data_input = AsciiInput(self._serial_stream)
        super().connect(data_packet_receiver)
