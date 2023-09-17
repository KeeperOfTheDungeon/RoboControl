from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStreamDataPacket import RemoteStreamDataPacket


class RemoteStream(RemoteData):
    _type_name: str = "stream"

    def set_data(self, *args, **kwargs):
        pass

  