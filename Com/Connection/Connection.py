#from typing import Callable, TypeAlias, Optional

#from RoboControl.Com.PacketLogger.DataPacketLogger import DataPacketLogger
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput

REMOTE_CHANEL_ID = 1
REMOTE_NODE_ID = 1

# FIXME what exactly are listeners?
#Listener: TypeAlias = [Callable or any]


class Connection:
    _data_output = RemoteDataOutput()
    _data_input = RemoteDataInput()
   # _data_packet_logger: DataPacketLogger

    def __init__(self, name: str = ""):
        self.device_id = REMOTE_CHANEL_ID
        self.connection_name = name
        self.connection_partner = ""

    def connect(self, data_packet_receiver: Listener) -> None:
        self._data_input.add_listener(data_packet_receiver)
        pass

    def disconnect(self) -> None:
        self._data_input.running = False

    def set_remote(self) -> None:
        self._data_output.set_remote()

    def transmitt(self, remote_data: RemoteData) -> bool:
        if self._data_output is None:
            print("Can't transmit as _data_output isn't set.")
            return False
        if self._data_output.get_remote():
            remote_data.set_source_address(self.device_id)
        else:
            remote_data.set_destination_address(self.device_id)
        data_packet: Optional[RemoteDataPacket] = remote_data.get_data_packet()
        if data_packet is None:
            raise ValueError(f"Incompatible remote_data type ({type(remote_data)}): {remote_data}")
        data_packet.set_remote_data(remote_data)
        if self._data_packet_logger is not None:
            self._data_packet_logger.add_output_packet(data_packet)
        self._data_output.transmitt(data_packet)
        return True

    def set_data_packet_logger(self, data_packet_logger: DataPacketLogger):
        self._data_packet_logger = data_packet_logger

    def get_data_packet_logger(self) -> DataPacketLogger:
        return self._data_packet_logger

    def get_connection_name(self) -> str:
        return self.connection_name

    def get_partner_name(self) -> str:
        return self.connection_partner

    # TODO
    # def get_statistics(self) -> ComStatistics:
    #    return self.statistics
