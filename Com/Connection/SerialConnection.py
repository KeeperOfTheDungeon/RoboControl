from typing import TypeAlias, Callable, Optional

import serial.tools.list_ports
from serial import Serial
from serial.tools.list_ports_common import ListPortInfo

from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii
from RoboControl.Com.Ascii.AsciiOutput import AsciiOutput
from RoboControl.Com.Ascii.AsciiInput import AsciiInput

# FIXME what exactly are listeners?
Listener: TypeAlias = [Callable or any]


class SerialConnection(Connection):
    port: str = "COM4"

    def __init__(self):
        super().__init__()

        # FIXME this isn't really optional is it
        self._serial_stream: Optional[Serial] = None

    def connect(self, data_packet_receiver: Listener) -> None:
        self._serial_stream = serial.Serial(self.port, 115200)
        self._data_output = AsciiOutput(self._serial_stream)
        self._data_input = AsciiInput(self._serial_stream)
        super().connect(data_packet_receiver)
    
    def disconnect(self) -> None:
        super().disconnect()
        self._serial_stream.close()

    @staticmethod
    def get_ports() -> list[ListPortInfo]:
        return list(serial.tools.list_ports.comports())

    def set_port(self, port: str) -> "SerialConnection":
        available_ports = [p.name for p in self.get_ports()]
        if port not in available_ports:
            raise ValueError(f"Port '{port}' is invalid. Please pick from: {available_ports}")
        self.port = port
        return self
