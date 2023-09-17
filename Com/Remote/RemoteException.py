from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteExceptionDataPacket import RemoteExceptionDataPacket


class RemoteException(RemoteData):
    _type_name: str = "exception"
