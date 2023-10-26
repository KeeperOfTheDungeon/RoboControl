from typing import Optional

from RoboControl.Com.PacketLogger.DataPacketLogger import DataPacketLogger
from RoboControl.Com.RemoteData import RemoteData
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput
from RoboControl.Com.ComStatistic import ComStatistic


REMOTE_CHANEL_ID: int = 1
REMOTE_NODE_ID: int = 1


class Connection:  # ConnectionControlInterface, RemoteDataTransmitter
    _data_packet_logger: DataPacketLogger

    def __init__(self, name: str = ""):
        self.device_id = REMOTE_CHANEL_ID
        self.connection_name: str = name
        self.connection_partner: str = ""

        self.statistic = ComStatistic()
        self._data_output: RemoteDataOutput = RemoteDataOutput(self.statistic)
        self._data_input: RemoteDataInput = RemoteDataInput(self.statistic)

    def connect(self, data_packet_receiver) -> bool:
        self._data_input.add_listener(data_packet_receiver)

    def disconnect(self) -> None:
        self._data_input.running = False

    def is_remote(self) -> None:
        return self._data_output.get_remote()

    def set_remote(self) -> None:
        self._data_output.set_remote()

    def transmitt(self, remote_data: RemoteData) -> bool:
        # print("c : Transmitt")
        if self._data_output is None:
            print("Can't transmit as _data_output isn't set.")
            return False
        if self.is_remote():
            remote_data.set_source_address(self.device_id)
        else:
            remote_data.set_destination_address(self.device_id)
  
        data_packet: Optional[RemoteDataPacket] = remote_data.get_data_packet()
        
        if data_packet is None:
            raise ValueError(f"Incompatible remote_data type ({type(remote_data)}): {remote_data}")
        data_packet.set_remote_data(remote_data)
        # TODO find a solution for Pico
        if self._data_packet_logger is not None:
            self._data_packet_logger.add_output_packet(data_packet)
        print("c : Transmitting")
        # print(self._data_output)
        self._data_output.transmitt(data_packet)
        
        return True

    def set_data_packet_logger(self, data_packet_logger: DataPacketLogger) -> None:
        self._data_packet_logger = data_packet_logger

    def get_data_packet_logger(self) -> DataPacketLogger:
        return self._data_packet_logger

    def get_connection_name(self) -> str:
        return self.connection_name

    def get_partner_name(self) -> str:
        return self.connection_partner

    def get_statistic(self) -> ComStatistic:
        return self.statistic
