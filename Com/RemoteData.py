from RoboControl.Com.RemoteDataPacket import RemoteCommandDataPacket, RemoteExceptionDataPacket, RemoteMessageDataPacket, RemoteNegativeAckDataPacket, RemoteStreamDataPacket
from RoboControl.Com.RemoteDataPacket import RemotePositiveAckDataPacket

from RoboControl.Com.RemoteParameter import RemoteParameter

# noinspection PyShadowingBuiltins
class RemoteData:
    _type_name: str = "generic"
    _description: str = "generic remote data"

    def __init__(self, id: int, name: str, description: str):
        self._name = name
        self._description = description

        self._id = id
        self._destination_address = 0
        self._source_address = 0

        self._parameter_list: List[RemoteParameter] = list()
        self._payload = bytearray()

    def set_id(self, id: int) -> None:
        self._id = id

    def get_id(self) -> int:
        return self._id

    def get_payload_size(self) -> int:  # getBufferSize()
        size = 0
        for parameter in self._parameter_list:
            size += parameter.get_byte_size()
        return size

    def has_id(self, id: int) -> bool:
        return self._id == id

    def get_destination_address(self) -> int:
        return self._destination_address

    def set_destination_address(self, destination: int) -> None:
        self._destination_address = destination

    def get_source_address(self) -> int:
        return self._source_address

    def set_source_address(self, source: int) -> None:
        self._source_address = source

    # noinspection PyMethodMayBeStatic
    def get_data_packet(self) -> "RemoteDataPacket":
        return None

    def make_data_packet(self, data_packet: "RemoteDataPacket") -> "RemoteDataPacket":
        data_packet.set_remote_data(self)
        message_data = bytearray(self.get_payload_size())
        for parameter in self._parameter_list:
            message_data.extend(parameter.get_as_buffer())
        data_packet.set_data(message_data)
        return data_packet

    def parse_data_packet_data(self, data_packet: "RemoteDataPacket") -> None:
        payload = data_packet.get_payload()
        if self.get_payload_size() != len(payload):
            logger.warning("wrong payload %s", payload)
        else:
            # print("correct payload")
            index = 0
            # print(payload)
            for parameter in self._parameter_list:
                index += parameter.parse_from_buffer(payload, index)

    def parse_data_packet(self, data_packet: "RemoteDataPacket") -> None:
        self._source_address = data_packet.get_source_address()
        self._destination_address = data_packet.get_destination_address()
        self.parse_data_packet_data(data_packet)

    def set_payload(self, payload) -> None:
        self._payload = payload

    def get_payload(self):
        return self._payload

    def __str__(self) -> str:
        res = f"RemoteData"
        res += f"\n\tClass({self.__class__.__name__})"
        res += f"\n\tName({self._name})"
        res += f"\n\t(source) {self._source_address} -> {self._destination_address} (destination)"
        res += f"\n\t(id) {self._id}"
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

class RemoteCommand(RemoteData):
    _type_name: str = "command"

    def get_data_packet(self) -> RemoteCommandDataPacket:
        data_packet = RemoteCommandDataPacket(self.get_destination_address(), self.get_source_address(), self.get_id())
        return self.make_data_packet(data_packet)

    @staticmethod
    def get_command(*args, **kwargs):
        raise ValueError("You are trying to create a generic RemoteCommand!")


class RemoteMessage(RemoteData):
    _type_name: str = "message"

    def get_data_packet(self) -> RemoteMessageDataPacket:
        data_packet = RemoteMessageDataPacket(self.get_destination_address(), self.get_source_address(), self.get_id())
        return self.make_data_packet(data_packet)
    

class RemoteStream(RemoteData):
    _type_name: str = "stream"

    def set_data(self, *args, **kwargs):
        raise ValueError("WIP")

    def get_data_packet(self) -> RemoteStreamDataPacket:
        packet = RemoteStreamDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)

    def make_parameter(self, index: int) -> RemoteParameter:
        raise ValueError("Not implemented: make_parameter")

    def parse_data_packet_data_dynamic(self, data_packet: "RemoteDataPacket") -> None:
        cursor, param_index = 0, 0
        data_buffer = data_packet.get_payload()
        while cursor <= (len(data_buffer) - 1):
            parameter = self.make_parameter(param_index)
            if param_index >= len(self._parameter_list):
                logging.warning(f"Ignoring parameter {param_index} as there are only {len(self._parameter_list)}: {data_buffer}")
            else:
                self._parameter_list[param_index] = parameter
            cursor += parameter.parse_from_buffer(data_buffer, cursor)
            param_index += 1



class RemoteException(RemoteData):
    _type_name: str = "exception"

    def get_data_packet(self) -> RemoteExceptionDataPacket:
        packet = RemoteExceptionDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)
    

class RemoteNegativeAck(RemoteData):
    _type_name: str = "fail"

    def get_data_packet(self) -> RemoteNegativeAckDataPacket:
        packet = RemoteNegativeAckDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)

    
class RemotePositiveAck(RemoteData):
    _type_name: str = "ok"

    def get_data_packet(self) -> RemotePositiveAckDataPacket:
        packet = RemotePositiveAckDataPacket(self._destination_address, self._source_address, self._id)
        return self.make_data_packet(packet)
