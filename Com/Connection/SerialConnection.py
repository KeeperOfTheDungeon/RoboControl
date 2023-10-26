from typing import Optional, Dict

import serial.tools.list_ports
from serial import Serial
from serial.tools.list_ports_common import ListPortInfo

from RoboControl.Com.Ascii.AsciiInput import AsciiInput
from RoboControl.Com.Ascii.AsciiOutput import AsciiOutput
from RoboControl.Com.Connection.Connection import Connection


# from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii


class SerialConnection(Connection):
    port: str = "COM4"  # comPortName

    open_streams: Dict[str, Optional[Serial]] = {}

    def __init__(self):
        super().__init__(name="serial connection")

        # FIXME this isn't really optional is it
        self._serial_stream: Optional[Serial] = None  # commPort

    def connect(self, data_packet_receiver) -> bool:
        """ "connect to serial interface" """

        # try { portIdentifier = CommPortIdentifier.getPortIdentifier(comPortName);
        # if ( portIdentifier.isCurrentlyOwned()==false ) return False

        baudrate: int = 115200
        timeout: int = 2000
        if not self.open_streams.get(self.port):
            SerialConnection.open_streams[self.port] = serial.Serial(
                self.port, baudrate=baudrate, timeout=timeout,
                # already default: bytesize=EIGHTBITS, parity=PARITY_NONE, stopbits=STOPBITS_ONE,
            )
        self._serial_stream = SerialConnection.open_streams[self.port]
        # commPort = portIdentifier.open(this.getClass().getName(),2000);
        # if ( ! commPort instanceof SerialPort ) return False

        self._data_input = AsciiInput(self._serial_stream, self.statistic)  # getInputStream
        self._data_input.run_threaded()

        self._data_output = AsciiOutput(self._serial_stream, self.statistic)  # getOutputStream

        self.connection_partner = self.port

        super().connect(data_packet_receiver)

        # } catch (Exception e)//catch (NoSuchPortException e) { e.printStackTrace(); }

        return True

    def disconnect(self) -> None:
        """ "disconnect from serial interface" """
        super().disconnect()
        SerialConnection.open_streams[self.port] = None
        if self._serial_stream is not None:
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

    def get_port_name(self) -> str:
        return self.port
