from typing import List

from RoboControl.Com.PacketLogger.filter.FilterRuleBlock import FilterRuleBlock


class DataPacketFilter:
    _name: str
    blocks: List[FilterRuleBlock]

    def get_name(self) -> str:
        """ "Get actual name of this filter" """
        return self._name

    def set_name(self, new_name: str) -> None:
        """ "set new Name of this filter" """
        self._name = new_name

    def add_filter_block(self) -> None:
        new_rule_block = FilterRuleBlock()
        self.blocks.append(new_rule_block)

    def __str__(self):
        return self._name
