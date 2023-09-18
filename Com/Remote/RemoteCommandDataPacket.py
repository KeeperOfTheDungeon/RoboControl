from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket, DataPacketType


class RemoteCommandDataPacket(RemoteDataPacket):
    _type_name: str = "remote command"
    _type: DataPacketType = DataPacketType.COMMAND
