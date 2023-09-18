from abc import ABC, abstractmethod

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteException import RemoteException
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream


class RemoteDecoder(ABC):
    @abstractmethod
    def decode(self, remote_data: RemoteData) -> bool:
        pass

    @abstractmethod
    def decode_command(self, remote_data: RemoteCommand) -> bool:
        pass

    @abstractmethod
    def decode_message(self, remote_data: RemoteMessage) -> bool:
        pass

    @abstractmethod
    def decode_stream(self, remote_data: RemoteStream) -> bool:
        pass

    @abstractmethod
    def decode_exception(self, remote_data: RemoteException) -> bool:
        pass
