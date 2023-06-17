from typing import List

from RoboControl.Com.PacketLogger.LoggedDataPacket import DisplayDataWidth_e, DisplayFormat_e, LoggedDataPacket, \
    LoggedDataPacketType
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class DataPacketLoggerEvent:
    def on_logger_change(self) -> None:
        raise ValueError("WIP")


class DataPacketLogger(list):
    DEFAULT_MAX_SIZE: int = 200

    def __init__(self):
        super().__init__()

        self._max_size: int = DataPacketLogger.DEFAULT_MAX_SIZE
        self._packet_count: int = 0
        self._standard_data_width: DisplayDataWidth_e = DisplayDataWidth_e.WIDTH_8
        self._standard_display_format: DisplayFormat_e = DisplayFormat_e.DECIMAL

        self._listeners: List[DataPacketLoggerEvent] = []

        self.is_recording: bool = False

    def reset_packet_count(self) -> None:
        self._packet_count = 0

    def get_packet_count(self) -> int:
        return self._packet_count

    def get_max_size(self) -> int:
        return self._max_size

    def set_max_size(self, new_max_size: int) -> None:

        self._max_size = 1 if new_max_size < 1 else new_max_size
        while len(self) > self._max_size:
            self.pop(0)

    def _add_packet(self, data_packet: RemoteDataPacket, data_packet_type: LoggedDataPacketType) -> bool:
        has_changed = False
        self._packet_count += 1
        if len(self) >= self._max_size:
            self.pop(0)  # WIP check: this.removeFirst() for IN, this.remove() for OUT
        if self.is_recording:
            packet = LoggedDataPacket(data_packet, data_packet_type, self._packet_count)
            self.append(packet)
            has_changed = True
        if has_changed:
            self._on_list_change()
        return has_changed

    def add_input_packet(self, data_packet: RemoteDataPacket) -> bool:
        return self._add_packet(data_packet, LoggedDataPacketType.IN)

    def add_output_packet(self, data_packet: RemoteDataPacket) -> bool:
        return self._add_packet(data_packet, LoggedDataPacketType.OUT)

    def add_listener(self, listener: DataPacketLoggerEvent):
        self._listeners.append(listener)

    def _on_list_change(self) -> None:
        for listener in self._listeners:
            listener.on_logger_change()

    def start_recording(self) -> None:
        self.is_recording = True

    def stop_recording(self) -> None:
        self.is_recording = False

    def on_log_size_change(self) -> None:
        self._on_list_change()

    def clear_list(self) -> None:
        self.clear()
        self._on_list_change()

    def set_new_log_size(self, new_size: int) -> None:
        raise ValueError("WIP: set_new_log_size not implemented")

    def set_data_width(self, new_width: DisplayDataWidth_e) -> None:
        self._standard_data_width = new_width
        self._on_list_change()

    def set_display_format(self, new_format: DisplayFormat_e) -> None:
        self._standard_display_format = new_format
        self._on_list_change()

    def record_in(self, _status: bool) -> None:
        raise ValueError("WIP: record_in not implement")

    def record_out(self, _status: bool) -> None:
        raise ValueError("WIP: record_out not implement")

    def get_standard_data_width(self) -> DisplayDataWidth_e:
        return self._standard_data_width

    def get_standard_display_format(self) -> DisplayFormat_e:
        return self._standard_display_format
