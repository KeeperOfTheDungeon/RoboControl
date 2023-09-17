from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStreamDataPacket import RemoteStreamDataPacket


class RemoteStream(RemoteData):
    _type_name: str = "stream"

    def set_data(self, *args, **kwargs):
        raise ValueError("WIP")

    def get_data_packet(self) -> RemoteStreamDataPacket:
        packet = RemoteStreamDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)
