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
    def get_command(id: int, values: list = None) -> "Stream_servosStatus":
        cmd = Stream_servosStatus(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def set_parameter(
            self, index: int,
            is_on: bool, is_active: bool, is_reverse: bool, is_at_min: bool, is_at_max: bool, is_stalling: bool
    ):
        self._parameter_list[index].set_on(is_on)
        self._parameter_list[index].set_active(is_active)
        self._parameter_list[index].set_reverse(is_reverse)
        self._parameter_list[index].set_at_min(is_at_min)
        self._parameter_list[index].set_at_max(is_at_max)
        self._parameter_list[index].set_stalling(is_stalling)

    def set_data(self, values: list) -> None:
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_on(value.is_on())
            parameter.set_active(value.is_active())
            parameter.set_reverse(value.is_reverse())
            parameter.set_at_min(value.is_at_min())
            parameter.set_at_max(value.is_at_max())
            parameter.set_stalling(value.is_stalling())
            self._parameter_list.append(parameter)

    def make_parameter(self, index: int) -> RemoteParameterServoStatus:
        return RemoteParameterServoStatus(f"status {index}", "status for servo " + str(index))

    def parse_data_packet_data(self, data_packet: "RemoteDataPacket") -> None:
        return self.parse_data_packet_data_dynamic(data_packet)
