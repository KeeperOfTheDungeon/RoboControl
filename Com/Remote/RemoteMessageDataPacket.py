from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket, DataPacketType


class RemoteMessageDataPacket(RemoteDataPacket):
    _type_name: str = "remote message"
    _type: DataPacketType = DataPacketType.MESSAGE
