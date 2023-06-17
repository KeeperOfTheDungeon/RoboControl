from RoboControl.Com.PacketLogger.filter.DataPacketFilterRule import DataPacketFilterRule
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class FilterRuleDirection(DataPacketFilterRule):
    _device_id: int
    name: str = "direction filter"

    def check(self, data_packet: RemoteDataPacket) -> bool:
        raise ValueError("WIP FilterRuleDirection.check not implemented")
        return False

    def set_device_id(self, device_id: int) -> None:
        """
        "Set this filters device ID"
        :param device_id: "id of device that should be filtered"
        :return:
        """
        self._device_id = device_id

    def get_name(self):
        return FilterRuleDirection.name
