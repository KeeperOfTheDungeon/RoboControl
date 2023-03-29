from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class RemoteStreamDataPacket(RemoteDataPacket):
	def __init__(self):
		super().__init__(self, "remote stream data")
		pass
	


"""
	
public RemoteStreamDataPacket(int destination, int source, int command)
{
	super(destination, source, command );
	this.type = DataPacketType.STREAM;
}
"""	
