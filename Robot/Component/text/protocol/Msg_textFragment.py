from typing import List, Union

from RoboControl.Com.RemoteParameter import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.RemoteParameter import RemoteParameterUint8
from RoboControl.Robot.Device.Generic.DataHub import DataHubProtocol

INDEX_TEXT = 0
INDEX_START_CHAR = 1
INDEX_FIRST_CHAR = 2


class Msg_textFragment(RemoteMessage):
    """ "Message containing fragment of a text" """
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterUint16]]

    def __init__(self, id: int = DataHubProtocol.MSG_TEXT_FRAGMENT):
        super().__init__(id, "textFragment", "message containing fragment of a text")
        self._parameter_list.append(RemoteParameterUint8("index", "text index"))
        self._parameter_list.append(RemoteParameterUint16("char index", "index of the first char in message"))

    def get_index(self):
        return self._parameter_list[INDEX_TEXT].get_value()

    def get_start_index(self):
        return self._parameter_list[INDEX_START_CHAR].get_value()

    def set_data(self, index: int, start_char: int) -> None:
        self._parameter_list[INDEX_TEXT].set_value(index)
        self._parameter_list[INDEX_START_CHAR].set_value(start_char)

    def get_fragment(self) -> List[float]:
        data = [None for i in range(self.get_payload_size() - INDEX_FIRST_CHAR)]
        cursor = 0
        for index in range(INDEX_FIRST_CHAR, self.get_payload_size()):
            data[cursor] = self._parameter_list[index].get_character()
            cursor += 1
        return data

    def parse_data_packet_data(self, data_packet: RemoteDataPacket) -> None:
        # print("size = dataPacket.getDataSize(); ", data_packet.get_data_size())
        raise ValueError("WIP: RemoteParameterTextCharacter")
        element_count = (data_packet.get_data_size() - 3) / 2
        for index in range(element_count):
            self._parameter_list.append(
                RemoteParameterTextCharacter(
                    f"character {index}",
                    "character"
                )
            )
        super().parse_data_packet_data(data_packet)

    @staticmethod
    def get_command(id: int, index: int = None, user_defined: int = None) -> "Msg_textFragment":
        res = Msg_textFragment(id)
        if None not in [index, user_defined]:
            res.set_data(index, user_defined)
        return res
