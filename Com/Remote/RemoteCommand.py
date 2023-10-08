from RoboControl.Com.Remote.RemoteCommandDataPacket import RemoteCommandDataPacket
from RoboControl.Com.Remote.RemoteData import RemoteData


class RemoteCommand(RemoteData):
    _type_name: str = "command"

    def get_data_packet(self) -> RemoteCommandDataPacket:
        data_packet = RemoteCommandDataPacket(self.get_destination_address(), self.get_source_address(), self.get_id())
        return self.make_data_packet(data_packet)

    @staticmethod
    def get_command(*args, **kwargs):
        raise ValueError("You are trying to create a generic RemoteCommand!")
