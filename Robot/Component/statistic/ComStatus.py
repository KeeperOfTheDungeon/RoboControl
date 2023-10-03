from RoboControl.Robot.AbstractRobot.AbstractListener import ComStatusListener
from RoboControl.Robot.Component.statistic.DeviceStatus import DeviceStatus


class ComStatus(DeviceStatus):
    _status_listener: list[ComStatusListener]

    def __init__(self):
        super().__init__()
        self._recived_messages = 0
        self._transfered_messages = 0
        self._lost_messages = 0
        self._invalid_messages = 0
        self._status_listener = list()

    def get_recived_messages(self):
        return self._recived_messages

    def get_transfered_messages(self):
        return self._transfered_messages

    def get_lost_messages(self):
        return self._lost_messages

    def get_invalid_messages(self):
        return self._invalid_messages

    def add_status_listener(self, listener):
        self._status_listener.append(listener)

    def remove_status_listener(self, listener):
        self._status_listener.remove(listener)

    def process_com_status_message(self, remote_data):
        self._transfered_messages = remote_data.get_transmitted_messages_count()
        self._recived_messages = remote_data.get_received_messages_count()
        self._lost_messages = remote_data.get_invalid_messages_count()
        self._invalid_messages = remote_data.get_lost_messages_count()

        for listener in self._status_listener:
            listener.com_status_changed(self)
