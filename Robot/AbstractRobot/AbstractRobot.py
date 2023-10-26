from typing import Optional

from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.PacketLogger.DataPacketLogger import DataPacketLogger
from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent
from RoboControl.Robot.AbstractRobot.AbstractRobotDevice import AbstractRobotDevice


class AbstractRobot():

    def __init__(self):
        self._device_list: list[AbstractRobotDevice] = list()
        self._name = "generic"
        self._type_name = "generic"
        self._connection_listener = list()
        # connection = Connection()
        # settings
        # connection listener

        self._data_packet_logger = DataPacketLogger()
        self._data_packet_logger.set_device_list(self.get_device_list())

        # FIXME is this really optional?
        self._connection: Optional[Connection] = None

    def get_name(self) -> str:
        return self._name

    def get_type_name(self) -> str:
        return self._type_name

    def connect(self, connection):
        print("connect")
        self._connection = connection
        self._connection.connect(self)
        self.on_connected()

    # FIXME why does this accept a connection parameter?
    def disconnect(self, _connection):
        self._connection.disconnect()
        # this.deviceList.setTransmitter(null);
        self.on_disconnected()

    def get_connection(self):
        return self._connection

    def add_connection_listener(self, listener) :
        self._connection_listener.append(listener)

    def remove_connection_listener(self, listener):
        self._connection_listener.remove(listener)

    def get_device_on_name(self, device_name):
        for device in self._device_list:
            if device.get_name() == device_name:
                return device
        return None

    def get_device_on_id(self, device_id):
        for device in self._device_list:
            if device.has_id(device_id):
                return device
        return None

    def get_component_on_global_id(self, device_id):
        pass

    def get_device_list(self):
        return self._device_list

    def get_device_count(self) -> int:
        return len(self._device_list)

    def on_connected(self) -> None:
        for listener in self._connection_listener:
            listener.connect(self)

    def on_disconnected(self) -> None:
        for listener in self._connection_listener:
            listener.disconnect(self)

    def get_data_packet_logger(self) -> DataPacketLogger:
        return self._data_packet_logger

    def set_data_packet_logger(self, data_packet_logger: DataPacketLogger):
        self._data_packet_logger = data_packet_logger
