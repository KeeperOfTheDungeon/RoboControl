from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket, DataPacketType


class RemoteStreamDataPacket(RemoteDataPacket):
	_type_name: str = "remote stream data"
	_type: DataPacketType = DataPacketType.STREAM
