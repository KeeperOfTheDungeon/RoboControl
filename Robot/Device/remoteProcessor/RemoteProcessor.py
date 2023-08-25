from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteException import RemoteException
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream

class RemoteProcessor:

	def __init__(self, remote_data, remote_processor):
		self._remote_data = remote_data 
		self._remote_processor = remote_processor


	def has_remote_id(self, id):
		if self._remote_data.get_id() == id:
			return True

	def get_remote_id(self):
		return self._remote_data.get_id()




	def get_remote_data(self):
		return self._remote_data

	def execute(self, remote_data):

	# vorsortierung um sp#tzer ifs zu sparen
		if isinstance(remote_data, RemoteCommand):
			#self._remote_processor.decode_command(remote_data)
			self._remote_processor(remote_data)
			
		elif isinstance(remote_data, RemoteMessage):
			self._remote_processor(remote_data)

		elif isinstance(remote_data, RemoteStream):
			#self._remote_processor.decode_stream(remote_data)
			self._remote_processor(remote_data)

		elif isinstance(remote_data, RemoteException):
			self._remote_processor(remote_data)

		pass

"""	
		if (this.remoteDecoder!=null)
	{
		if (remoteData instanceof RemoteCommand)
		{
			this.remoteDecoder.decodeCommand((RemoteCommand)remoteData);
		}
		else if (remoteData instanceof RemoteMessage)
		{
			this.remoteDecoder.decodeMessage((RemoteMessage)remoteData);
		}
		else if (remoteData instanceof RemoteStream)
		{
			this.remoteDecoder.decodeStream((RemoteStream)remoteData);
		}
		else if (remoteData instanceof RemoteException)
		{
			this.remoteDecoder.decodeException((RemoteException)remoteData);
		}
	//	else if (remoteData instanceof RemoteAllert)
		{
		//	this.remoteDecoder.decodeException((RemoteException)remoteData);*/
		}
	}
	"""
"""


public void execute(R remoteData)
{
	if (this.remoteDecoder!=null)
	{
		if (remoteData instanceof RemoteCommand)
		{
			this.remoteDecoder.decodeCommand((RemoteCommand)remoteData);
		}
		else if (remoteData instanceof RemoteMessage)
		{
			this.remoteDecoder.decodeMessage((RemoteMessage)remoteData);
		}
		else if (remoteData instanceof RemoteStream)
		{
			this.remoteDecoder.decodeStream((RemoteStream)remoteData);
		}
		else if (remoteData instanceof RemoteException)
		{
			this.remoteDecoder.decodeException((RemoteException)remoteData);
		}
	//	else if (remoteData instanceof RemoteAllert)
		{
		//	this.remoteDecoder.decodeException((RemoteException)remoteData);*/
		}
	}
}

"""