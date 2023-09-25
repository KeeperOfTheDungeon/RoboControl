from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteExceptionDataPacket import RemoteExceptionDataPacket
from RoboControl.Com.Remote.RemoteNegativeAckDataPacket import RemoteNegativeAckDataPacket


class RemoteNegativeAck(RemoteData):
    _type_name: str = "fail"

    def get_data_packet(self) -> RemoteNegativeAckDataPacket:
        packet = RemoteNegativeAckDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)
