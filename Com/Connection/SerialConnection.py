from typing import TypeAlias, Callable, Optional, Dict

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

    open_streams: Dict[str, Optional[Serial]] = {}

    def __init__(self):
        super().__init__()

        # FIXME this isn't really optional is it
        self._serial_stream: Optional[Serial] = None

    def connect(self, data_packet_receiver: Listener) -> None:
        if not self.open_streams.get(self.port):
            SerialConnection.open_streams[self.port] = serial.Serial(self.port, 115200)
        self._serial_stream = SerialConnection.open_streams[self.port]

        self._data_output = AsciiOutput(self._serial_stream)
        self._data_input = AsciiInput(self._serial_stream)
        super().connect(data_packet_receiver)
    
    def disconnect(self) -> None:
        SerialConnection.open_streams[self.port] = None
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
