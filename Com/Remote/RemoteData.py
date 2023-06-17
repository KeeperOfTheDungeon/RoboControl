from typing import List

from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter


# noinspection PyShadowingBuiltins
class RemoteData:
    _type_name: str = "generic"

    def __init__(self, id, name, description):
        self._source_address = 0
        self._destination_address = 0
        self._id = id

        self._name = name
        self._description = description
        self._parameter_list: List[RemoteParameter] = list()
        self._payload = bytearray()

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def get_payload_size(self):
        size = 0
        for parameter in self._parameter_list:
            size += parameter.get_byte_size()
        return size

    def has_id(self, id):
        return self._id == id

    def get_destination_address(self):
        return self._destination_address

    def set_destination_address(self, destination):
        self._destination_address = destination

    def get_source_address(self):
        return self._source_address

    def set_source_address(self, source):
        self._source_address = source

    # noinspection PyMethodMayBeStatic
    def get_data_packet(self) -> None:
        return None

    def make_data_packet(self, data_packet: "RemoteDataPacket") -> "RemoteDataPacket":
        data_packet.set_remote_data(self)
        message_data = bytearray(self.get_payload_size())
        for parameter in self._parameter_list:
            message_data.extend(parameter.get_as_buffer())
        data_packet.set_data(message_data)
        return data_packet

    def parse_data_packet_data(self, data_packet: "RemoteDataPacket") -> None:
        data_index = 0
        data_buffer = data_packet.get_data()
        for parameter in self._parameter_list:
            data_index += parameter.parse_from_buffer(data_buffer, data_index)
        # TODO and?

    def parse_data_packet(self, data_packet: "RemoteDataPacket") -> None:
        self._source_address = data_packet.get_source_address()
        self._destination_address = data_packet.get_destination_address()
        self.parse_data_packet_data(data_packet)

    def set_payload(self, payload):
        self._payload = payload

    def get_payload(self):
        return self._payload

    def parse_payload(self, payload):

        if self.get_payload_size() != len(payload):
            print("wrong payload")
        else:
            print("correct payload")
            index = 0
            print(payload)
            for parameter in self._parameter_list:
                index += parameter.parse_from_buffer(payload, index)

    def __str__(self) -> str:
        res = f"RemoteData({self._name}, id={self._id}): {self._description}"
        res += f"\n\t(source) {self._source_address} -> {self._destination_address} (destination)"
        res += f"\n\tpayload: " + ",".join([str(b) for b in self._payload])
        res += f"\n\tparams: " + self.get_parameters_as_string(True)
        return res

    def get_name(self) -> str:
        return self._name

    def get_description(self) -> str:
        return self._description

    def get_type_name(self) -> str:
        return self._type_name

    def get_parameter_count(self) -> int:
        return len(self._parameter_list)

    def get_parameters_as_string(self, description: bool) -> str:
        return ",".join([p.get_as_string(description) for p in self._parameter_list])

    def get_parameter_list(self) -> List[RemoteParameter]:
        return self._parameter_list
