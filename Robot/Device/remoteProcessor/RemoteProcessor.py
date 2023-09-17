from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteException import RemoteException
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream

# WIP check if this merged right

class RemoteProcessor:

    def __init__(self, remote_data, remote_processor):
        self._remote_data = remote_data
        self._remote_processor = remote_processor

    def has_remote_id(self, id):
        if self._remote_data.get_id() == id:
            return True
        return False

    def get_remote_data(self):
        return self._remote_data

    def get_remote_id(self):
        return self._remote_data.get_id()

    def execute(self, remote_data):
        # vorsortierung um sp#tzer ifs zu sparen
        if isinstance(remote_data, RemoteCommand):
            # self._remote_processor.decode_command(remote_data)
            self._remote_processor(remote_data)
        elif isinstance(remote_data, RemoteMessage):
            self._remote_processor(remote_data)
        elif isinstance(remote_data, RemoteStream):
            # self._remote_processor.decode_stream(remote_data)
            self._remote_processor(remote_data)
        elif isinstance(remote_data, RemoteException):
            self._remote_processor(remote_data)
        pass
