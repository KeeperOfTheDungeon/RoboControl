from RoboControl.Com.PacketLogger.LoggedDataPacket import LoggedDataPacketType, LoggedDataPacket
from RoboControl.Com.PacketLogger.filter.DataPacketFilterRule import DataPacketFilterRule


class FilterRuleDirection(DataPacketFilterRule):
    name: str = "direction filter"

    def __init__(self, allow_direction: LoggedDataPacketType):
        self._allow_direction = allow_direction

    def does_pass(self, data_packet: LoggedDataPacket) -> bool:
        return data_packet.get_direction_as_string() == self._allow_direction.value

    def as_dict(self) -> dict:
        return {
            "direction": self._allow_direction.value
        }
