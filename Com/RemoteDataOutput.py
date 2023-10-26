from typing import TypeAlias

from RoboControl.Com.ComStatistic import ComStatistic
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket

Byte: TypeAlias = int


class RemoteDataOutput:
    _packet_queue = list()
    _listener_list = list()
    _is_remote = False
    _is_running = False

    def __init__(self, statistic: ComStatistic):
        self.statistic = statistic

    def run(self):
        pass

    def add_listener(self, listener):
        pass

    def remove_listener(self, liustener):
        pass

    def is_running(self):
        return self._is_running

    def set_remote(self):
        self._is_remote = True

    def get_remote(self):
        return self._is_remote

    def transmitt(self, data_packet: RemoteDataPacket):
        print ("RDO : default Transmitter")
        return False

    def send_byte(self, token: Byte) -> bool:
        return False
