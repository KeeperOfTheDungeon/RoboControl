from typing import List

from RoboControl.Com.PacketLogger.LoggedDataPacket import LoggedDataPacketType, LoggedDataPacket
from RoboControl.Com.PacketLogger.filter.DataPacketFilterRule import DataPacketFilterRule
from RoboControl.Com.PacketLogger.filter.FilterRuleDataPacketType import FilterRuleDataPacketType
from RoboControl.Com.PacketLogger.filter.FilterRuleDevice import FilterRuleSource, FilterRuleDestination
from RoboControl.Com.PacketLogger.filter.FilterRuleDirection import FilterRuleDirection
from RoboControl.Com.Remote.RemoteDataPacket import DataPacketType


class DataPacketFilter:
    ALLOW_ALL: str = "all"

    def __init__(self, name):
        self.name: str = name
        self._rules: List[DataPacketFilterRule] = []

    def append(self, rule: DataPacketFilterRule) -> None:
        self._rules.append(rule)

    @property
    def size(self) -> int:
        return len(self._rules)

    def get_rules(self):
        return self._rules

    def check(self, data_packet: LoggedDataPacket) -> bool:
        for rule in self._rules:
            if not rule.check(data_packet):
                return False
        return True

    def __repr__(self):
        return f"DataPacketFilter({self.name},{self.size})"

    __str__ = __repr__

    @staticmethod
    def get_example_filters() -> List["DataPacketFilter"]:
        empty = DataPacketFilter(DataPacketFilter.ALLOW_ALL)
        r1 = FilterRuleDirection(LoggedDataPacketType.IN)
        r5 = FilterRuleSource(1)
        r5.set_type(False)
        f1 = DataPacketFilter("inFromExt")
        f1.append(r1)
        f1.append(r5)
        r2 = FilterRuleDirection(LoggedDataPacketType.IN)
        r6 = FilterRuleSource(1)
        r2.set_type(False)
        f2 = DataPacketFilter("outFromCon")
        f2.append(r2)
        f2.append(r6)
        f3 = DataPacketFilter("notStream")
        r7 = FilterRuleDataPacketType(DataPacketType.STREAM)
        r7.set_type(False)
        f3.append(r7)
        return [empty, f1, f2, f3]
