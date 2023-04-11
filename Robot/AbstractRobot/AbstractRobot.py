from typing import Optional, TypeAlias, Callable

from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.AbstractRobot import AbstractDevice
from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent

# FIXME what exactly are listeners?
Listener: TypeAlias = [Callable or any]


class AbstractRobot:

    def __init__(self):
        self._device_list: list[AbstractDevice] = list()
        self._name = "generic"
        self._type_name = "generic"
        self._connection_listener: list[Listener] = list()
        # connection = Connection()
        # settings
        # connection listener

        # dataPacket logger

        # FIXME is this really optional?
        self._connection: Optional[Connection] = None

    def get_name(self) -> str:
        return self._name

    def connect(self, connection: Connection) -> None:
        print("connect")
        self._connection = connection
        self._connection.connect(self)
        self.on_connected()

    # FIXME why does this accept a connection parameter?
    def disconnect(self, connection: Connection) -> None:
        # this.deviceList.setTransmitter(null);
        # this.onDisconnected();
        pass

    def receive(self, data_packet: RemoteDataPacket) -> None:

        # FIXME .get_source_addres() ? (which is also a typo)
        source = data_packet.get_source()

        for device in self._device_list:
            if device.sget_id() == source:
                device.deliver_packet(data_packet)
            # data logger log data packet

    def get_connection(self) -> Connection:
        return self._connection

    def add_connection_listener(self, listener: Listener) -> None:
        self._connection_listener.append(listener)

    def remove_connection_listener(self, listener: Listener) -> None:
        pass

    def get_device_on_name(self, device_name: str) -> AbstractDevice:
        pass

    def get_device_on_id(self, device_id: int) -> AbstractDevice:
        for device in self._device_list:
            if device.has_id(device_id):
                return device

        return None

    def get_component_on_global_id(self, device_id: int) -> AbstractComponent:
        pass

    def get_device_list(self) -> list[AbstractDevice]:
        pass

    def get_device_count(self) -> int:
        return len(self._device_list)

    def on_connected(self) -> None:
        for listener in self._connection_listener:
            listener.connect(self)

    def on_disconnected(self) -> None:
        for listener in self._connection_listener:
            listener.disconnect(self)
