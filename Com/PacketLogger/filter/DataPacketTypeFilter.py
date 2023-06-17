from RoboControl.Com.PacketLogger.filter.DataPacketFilterRule import DataPacketFilterRule
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket, DataPacketType


class DataPacketTypeFilter(DataPacketFilterRule):
    name = "type filter"
    _type: DataPacketType

    def check(self, data_packet: RemoteDataPacket) -> bool:
        res = data_packet.get_type() == self._type
        if not self._pass_filter:
            res = not res
        return res

    def get_name(self) -> str:
        return DataPacketTypeFilter.name
