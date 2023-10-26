from abc import ABC, abstractmethod

from RoboControl.Com.RemoteData import RemoteCommand ,RemoteMessage, RemoteStream,  RemoteException



class RemoteDecoder(ABC):
    @abstractmethod
    def decode(self, remote_data) -> bool:
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
