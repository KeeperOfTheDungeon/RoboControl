from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket, DataPacketType


class RemoteExceptionDataPacket(RemoteDataPacket):
    _type_name: str = "remote exception"
    _type: DataPacketType = DataPacketType.EXCEPTION
