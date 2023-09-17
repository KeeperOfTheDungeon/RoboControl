from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteExceptionDataPacket import RemoteExceptionDataPacket


class RemoteException(RemoteData):
    _type_name: str = "exception"

    def get_data_packet(self) -> RemoteExceptionDataPacket:
        packet = RemoteExceptionDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)
