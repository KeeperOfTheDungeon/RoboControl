class RemoteDataOutput:
	_running = False

	_packet_queue = list()
	_listener_list = list()
	_remote  = False

	def __init__(self):
		pass		
 
	def run(self):
		pass

	def add_listener(self, listener):	
		pass
		
	def remove_listener(self, liustener):
		pass
		
		
	def is_runing(self):
		pass

	def set_remote(self):
		self._remote = True
        


	def transmitt(self, data_packet):
		pass

"""
	if (isRemote)
	{
		remoteData.setSource(deviceId);
	}
	else
	{
		remoteData.setDestination(deviceId);
	}
	
	
	dataPacket= remoteData.getDataPacket();
	dataPacket.setRemoteData(remoteData);
"""

