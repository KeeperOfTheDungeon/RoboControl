import logging

from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStreamDataPacket import RemoteStreamDataPacket


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
