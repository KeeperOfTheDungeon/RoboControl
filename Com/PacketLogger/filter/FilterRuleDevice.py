from RoboControl.Com.PacketLogger.LoggedDataPacket import LoggedDataPacket
from RoboControl.Com.PacketLogger.filter.DataPacketFilterRule import DataPacketFilterRule


class FilterRuleDestination(DataPacketFilterRule):
    name: str = "destination device filter"

    def __init__(self, device_id: int):
        self._device_id = device_id

    def does_pass(self, data_packet: LoggedDataPacket) -> bool:
        return data_packet.get_data_packet().get_destination_address() == self._device_id

    def as_dict(self) -> dict:
        return {
            "destination": self._device_id
        }


class FilterRuleSource(DataPacketFilterRule):
    name: str = "source device filter"

    def __init__(self, device_id: int):
        self._device_id = device_id

    def does_pass(self, data_packet: LoggedDataPacket) -> bool:
        return data_packet.get_data_packet().get_source_address() == self._device_id

    def as_dict(self) -> dict:
        return {
            "source": self._device_id
        }
