from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition


class Stream_servosDestinations(RemoteStream):
    _parameter_list: List[RemoteParameterServoPosition]

    def __init__(self, id: int = LegControllerProtocol.STREAM_SERVOS_DESTINATIONS):
        super().__init__(id, "servoDestinations", "servo destinations")

    @staticmethod
    def get_command(id: int, values: list[int] = None) -> "Stream_servosDestinations":
        cmd = Stream_servosDestinations(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def get_destination(self, index: int) -> int:
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_position()

    def set_data(self, values: list[int]) -> None:
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_position(value)
            self._parameter_list.append(parameter)

    def make_parameter(self, index: int) -> RemoteParameterServoPosition:
        return RemoteParameterServoPosition(f"destination {index}", "destination for servo " + str(index))

    def parse_data_packet_data(self, data_packet: "RemoteDataPacket") -> None:
        return self.parse_data_packet_data_dynamic(data_packet)

    def get_positions_count(self) -> int:
        return len(self._parameter_list)
