from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket, DataPacketType


class RemoteNegativeAckDataPacket(RemoteDataPacket):
    _type_name: str = "remote fail"
    _type: DataPacketType = DataPacketType.FAIL
