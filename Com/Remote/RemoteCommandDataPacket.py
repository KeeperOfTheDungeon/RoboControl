from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class RemoteCommandDataPacket(RemoteDataPacket):
	def __init__(self):
		super().__init__(self, "remote command")
		pass

"""
	
public RemoteCommandDataPacket(int destination, int source, int command)
{
	super(destination, source, command );
	this.type = DataPacketType.COMMAND;
}
	
"""