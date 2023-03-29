from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class RemoteExceptionDataPacket(RemoteDataPacket):
	def __init__(self):
		super().__init__(self, "remote exception")
		pass


