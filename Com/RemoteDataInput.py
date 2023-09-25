# disabled for micropython  # from typing import Callable, TypeAlias

from RoboControl.Com.ComStatistic import ComStatistic
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket

# Listener: TypeAlias = [Callable or any]
# "DataPacketReceiver": TypeAlias = Listener


class RemoteDataInput:
    _listener_list: "list[DataPacketReceiver]" = list()

    def __init__(self, statistic: ComStatistic):
        self.statistic = statistic
        self.running = False
        # self.set_daemon(True)

    def run(self) -> None:
        pass

    def add_listener(self, listener: "DataPacketReceiver") -> None:
        """
        "ad a listener to the distribution list so this listener will become every incoming data packets received thru this input"
        :param listener:
        :return:
        """
        # print(" RDI : add_listener", self._listener_list)
        self._listener_list.append(listener)

    def remove_listener(self, listener: "DataPacketReceiver") -> None:
        """
        remove a listener from the distribution list, so this listener will not become any mor packets
        :param listener: to be removed from distribution list
        :return:
        """
        self._listener_list.remove(listener)

    def deliver_packet(self, data_packet: RemoteDataPacket) -> None:
        """ "Deliver a new received data packet to all members of the distribution list (listeners)" """
        # print(self._listener_list)
        if data_packet is not None:
            for listener in self._listener_list:
                listener.receive(data_packet)

    def is_running(self) -> bool:
        return self.running
