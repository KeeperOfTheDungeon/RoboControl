from typing import List, Union

from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Com.RemoteParameter import RemoteParameterUint32
from RoboControl.Com.Remote.RemoteStream import RemoteStream

INDEX_TRANSMITTED_MESSAGES = 0
INDEX_RECEIVED_MESSAGES = 1
INDEX_INVALID_MESSAGES = 2
INDEX_LOST_MESSAGES = 3
INDEX_LOST_UNDELIVERABLE = 4
INDEX_COM_STATUS = 5


class Stream_comStatistics(RemoteStream):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterUint32]]

    def __init__(self, id):
        super().__init__(id, "comStatus", "status of the com system")

        self._parameter_list.append(RemoteParameterUint32("transmitted", "number of transmitted messages"))
        self._parameter_list.append(RemoteParameterUint32("received", "number of recived messages thrue this device"))
        self._parameter_list.append(
            RemoteParameterUint32("invalid", "number of invalid messages received thrue this device"))
        self._parameter_list.append(RemoteParameterUint32("lost", "number of lost mesages"))
        self._parameter_list.append(RemoteParameterUint32("undeliverable", "number of undeliverable mesages"))
        self._parameter_list.append(RemoteParameterUint8("status", "actual status of the device com system"))

    def get_transmitted_messages_count(self):
        return self._parameter_list[INDEX_TRANSMITTED_MESSAGES].get_value()

    def get_received_messages_count(self):
        return self._parameter_list[INDEX_RECEIVED_MESSAGES].get_value()

    def get_invalid_messages_count(self):
        return self._parameter_list[INDEX_INVALID_MESSAGES].get_value()

    def get_lost_messages_count(self):
        return self._parameter_list[INDEX_LOST_MESSAGES].get_value()

    def set_data(
            self, transmitted: int, received: int, invalid: int, lost: int, status: int, undeliverable: int
    ) -> None:
        self._parameter_list[INDEX_TRANSMITTED_MESSAGES].set_value(transmitted)
        self._parameter_list[INDEX_RECEIVED_MESSAGES].set_value(received)
        self._parameter_list[INDEX_INVALID_MESSAGES].set_value(invalid)
        self._parameter_list[INDEX_LOST_MESSAGES].set_value(lost)
        self._parameter_list[INDEX_LOST_UNDELIVERABLE].set_value(undeliverable)
        self._parameter_list[INDEX_COM_STATUS].set_value(status)

    @staticmethod
    def get_command(
            id: int,
            transmitted: int = None, received: int = None, invalid: int = None, lost: int = None, status: int = None, undeliverable: int = None
    ):
        cmd = Stream_comStatistics(id)
        if transmitted and received and invalid and lost and status and undeliverable:
            cmd.set_data(transmitted, received, invalid, lost, status, undeliverable)
        return cmd
