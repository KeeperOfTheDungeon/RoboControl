from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteExceptionDataPacket import RemoteExceptionDataPacket
from RoboControl.Com.Remote.RemotePositiveAckDataPacket import RemotePositiveAckDataPacket


class RemotePositiveAck(RemoteData):
    _type_name: str = "ok"

    def get_data_packet(self) -> RemotePositiveAckDataPacket:
        packet = RemotePositiveAckDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)
