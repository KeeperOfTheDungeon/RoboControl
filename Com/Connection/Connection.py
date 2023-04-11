from typing import Callable, TypeAlias

from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput

REMOTE_CHANEL_ID = 1
REMOTE_NODE_ID = 1

# FIXME what exactly are listeners?
Listener: TypeAlias = [Callable or any]


class Connection:
    _data_output = RemoteDataOutput()
    _data_input = RemoteDataInput()

    def __init__(self):
        self.device_id = REMOTE_CHANEL_ID
        self.connection_name = ""
        self.connection_partner = ""

    def connect(self, data_packet_receiver: Listener) -> None:
        self._data_input.add_listener(data_packet_receiver)
        pass

    def disconnect(self) -> None:
        pass

    def set_remote(self) -> None:
        self._data_output.set_remote()
        pass

    def transmitt(self, data_packet: RemoteDataPacket) -> None:
        self._data_output.transmitt(data_packet)
