from typing import List

from RoboControl.Com.Connection import Connection
from RoboControl.Com.PacketLogger.LoggedDataPacket import LoggedDataPacket, DisplayFormat_e, DisplayDataWidth_e, \
    LoggedDataPacketType
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.AbstractRobot.AbstractRobotDevice import AbstractRobotDevice
from RoboControl.Com.PacketLogger.TableModel import TableModel, Column, TimestampColumn, PacketColumn


class DataPacketLogger(TableModel):
    DEFAULT_MAX_SIZE = 200

    _device_list: List[AbstractRobotDevice]

    def __init__(self):
        super().__init__()
        self._data_column = PacketColumn("data")
        for column in [
            Column("nr"),
            TimestampColumn("timestamp"),
            Column("type"),
            Column("direction"),
            Column("destination"),
            Column("source"),
            Column("name"),
            self._data_column,
        ]:
            self.add_column(column)
        self.max_size = self.DEFAULT_MAX_SIZE
        self._cursor = 0

    def set_device_list(self, device_list: List[AbstractRobotDevice]) -> None:
        self._device_list = device_list

    def get_as_native(self) -> str:
        raise ValueError("WIP")

    def get_as_raw(self, row: int):
        raise ValueError("WIP")
        row: LoggedDataPacket = self.rows[row]
        return row.get_data_as_string(self.rows.get_standard_data_width(), False)

    def set_data_width(self, new_width: DisplayDataWidth_e) -> None:
        self._data_column.set_data_width(new_width)
        self.on_change()

    def set_display_format(self, new_format: DisplayFormat_e) -> None:
        self._data_column.set_data_format(new_format)
        self.on_change()

    def _add_packet(self, data_packet: RemoteDataPacket, data_packet_type: LoggedDataPacketType) -> bool:
        packet = LoggedDataPacket(data_packet, data_packet_type, self._cursor)
        self._cursor += 1

        def parse_device(device_list, device_id) -> str:
            if Connection.REMOTE_CHANEL_ID == device_id:
                return "Connection"
            return device_list[device_id].get_name()

        values = [
            int(packet.get_number()),
            packet.get_timestamp(),
            packet.get_type_name(),
            packet.get_direction_as_string(),
            parse_device(self._device_list, packet.get_destination()),
            parse_device(self._device_list, packet.get_source()),
            packet.get_command_name() + " (" + str(packet.get_command()) + ")",
            packet,
        ]
        return self.add_row(values)

    def add_input_packet(self, data_packet: RemoteDataPacket) -> bool:
        return self._add_packet(data_packet, LoggedDataPacketType.IN)

    def add_output_packet(self, data_packet: RemoteDataPacket) -> bool:
        return self._add_packet(data_packet, LoggedDataPacketType.OUT)
