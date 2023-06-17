from RoboControl.Com.Remote.RemoteCommandDataPacket import RemoteCommandDataPacket
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class RemoteCommand(RemoteData):
    _type_name: str = "command"

    def get_data_packet(self) -> RemoteDataPacket:
        data_packet = RemoteCommandDataPacket(self.get_destination_address(), self.get_source_address(), self.get_id())
        return self.make_data_packet(data_packet)
