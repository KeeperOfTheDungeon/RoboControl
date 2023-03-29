from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class RemoteMessageDataPacket(RemoteDataPacket):
	def __init__(self):
		super().__init__(self, "remote message")
		pass

"""

	
public RemoteMessageDataPacket(int destination, int source, int command)
{
	super(destination, source, command );
	this.type = DataPacketType.MESSAGE;
}
"""	
