from RoboControl.Com.Remote.RemoteMessageDataPacket import RemoteMessageDataPacket
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class RemoteMessage(RemoteData):
    _type_name: str = "message"

    def get_data_packet(self) -> RemoteDataPacket:
        data_packet = RemoteMessageDataPacket(self.get_destination_address(), self.get_source_address(), self.get_id())
        return self.make_data_packet(data_packet)
