from abc import abstractmethod
from enum import Enum

from RoboControl.Com.PacketLogger.LoggedDataPacket import LoggedDataPacket


class DataPacketFilterRuleType(Enum):
    PASS = True
    FAIL = False


class DataPacketFilterRule:
    name: str = "generic_rule"
    filter_type: DataPacketFilterRuleType = DataPacketFilterRuleType.PASS
    """ a pass filter returns true on match when checking packets. block filter returns false. """

    @property
    def is_pass(self) -> bool:
        return True if (self.filter_type == DataPacketFilterRuleType.PASS) else False

    def set_type(self, is_pass: bool) -> None:
        self.filter_type = DataPacketFilterRuleType.PASS if is_pass else DataPacketFilterRuleType.FAIL

    @abstractmethod
    def does_pass(self, data_packet: LoggedDataPacket) -> bool:
        raise ValueError("Not implemented")

    def check(self, data_packet: LoggedDataPacket) -> bool:
        res = self.does_pass(data_packet)
        return res if self.is_pass else (not res)
