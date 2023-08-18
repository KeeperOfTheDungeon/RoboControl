#from typing import Callable, TypeAlias

from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket

# FIXME what exactly are listeners?
#Listener: TypeAlias = [Callable or any]


class RemoteDataInput:
    running = False

    _listener_list: list[Listener] = list()

    def run(self) -> None:
        pass

    def add_listener(self, listener: Listener) -> None:
        self._listener_list.append(listener)
        pass

    def remove_listener(self, listener: Listener) -> None:
        pass

    def deliver_packet(self, remote_data: RemoteDataPacket) -> None:
        for listener in self._listener_list:
            listener.receive(remote_data)

    # FIXME typo
    def is_runing(self) -> bool:
        pass
