from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoStatus import RemoteParameterServoStatus


class Stream_servosStatus(RemoteStream):
    _parameter_list: List[RemoteParameterServoStatus]

    def __init__(self, id: int = LegControllerProtocol.STREAM_SERVOS_STATUS):
        super().__init__(id, "servosStatus", "status from servos")

    def is_on(self, index: int) -> bool:
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_on()
        return False

    def is_active(self, index: int) -> bool:
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_active()
        return False

    def is_reverse(self, index: int) -> bool:
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_reverse()
        return False

    def is_at_min(self, index: int) -> bool:
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_at_min()
        return False

    def is_at_max(self, index: int) -> bool:
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_at_max()
        return False

    def is_stalling(self, index: int) -> bool:
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_stalling()
        return False

    @staticmethod
    def get_command(
            id: int,
            is_on: bool = None,
            is_active: bool = None,
            is_reverse: bool = None,
            is_at_min: bool = None,
            is_at_max: bool = None,
            is_stalling: bool = None,
    ):
        cmd = Stream_servosStatus(id)
        if None not in [is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling]:
            cmd.set_data(is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling)
        return cmd

    def set_data(
            self, is_on: bool, is_active: bool, is_reverse: bool, is_at_min: bool, is_at_max: bool, is_stalling: bool
    ):
        # TODO this sounds wrong
        parameter = self._parameter_list[0]
        parameter.set_on(is_on)
        parameter.set_active(is_active)
        parameter.set_reverse(is_reverse)
        parameter.set_at_min(is_at_min)
        parameter.set_at_max(is_at_max)
        parameter.set_stalling(is_stalling)

    def parse_data_packet_data(self, data_packet: RemoteDataPacket) -> None:
        data_buffer: bytearray = data_packet.get_data()
        data_index = 0
        for index, _ in enumerate(data_buffer):
            parameter = RemoteParameterServoStatus(
                f"status {index}",
                f"status for servo {index}"
            )
            data_index += parameter.parse_from_buffer(data_buffer, data_index)
            self._parameter_list.append(parameter)
