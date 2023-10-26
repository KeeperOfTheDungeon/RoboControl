from RoboControl.Com.PacketLogger.LoggedDataPacket import LoggedDataPacket
from RoboControl.Com.PacketLogger.filter.DataPacketFilterRule import DataPacketFilterRule
from RoboControl.Com.RemoteDataPacket import DataPacketType


class FilterRuleDataPacketType(DataPacketFilterRule):
    name: str = "type filter"

    def __init__(self, allow_type: DataPacketType):
        self._allow_type = allow_type

    def does_pass(self, data_packet: LoggedDataPacket) -> bool:
        return data_packet.get_data_packet().get_type() == self._allow_type

    def as_dict(self) -> dict:
        return {
            "type": self._allow_type
        }
