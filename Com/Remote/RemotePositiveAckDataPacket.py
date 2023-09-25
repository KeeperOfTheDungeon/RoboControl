from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket, DataPacketType


class RemotePositiveAckDataPacket(RemoteDataPacket):
    _type_name: str = "remote ok"
    _type: DataPacketType = DataPacketType.OK
