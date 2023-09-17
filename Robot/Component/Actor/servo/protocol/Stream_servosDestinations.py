from typing import List

from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition


class Stream_servosDestinations(RemoteStream):
    _parameter_list: List[RemoteParameterServoPosition]

    def __init__(self, id: int):
        super().__init__(id, "servoDestinations", "servo destinations")

    @staticmethod
    def get_command(id: int, size: int):
        cmd = Stream_servosDestinations(id)
        for index in range(0, size):
            parameter = RemoteParameterServoPosition(
                f"destination {index}", f"destination for servo {index}"
            )
            cmd._parameter_list.append(parameter)
        return cmd

    def get_destination(self, index):
        if index < len(self._parameter_list):
            return self._parameter_list[index].get_position()
        return 0

    def get_positions_count(self) -> int:
        return len(self._parameter_list)

    def set_data(self, destinations: List[float]) -> None:
        for index, position in enumerate(destinations):
            parameter = RemoteParameterServoPosition(
                f"destination {index}",
                f"destination for servo {index}"
            )
            parameter.set_position(position)
            self._parameter_list.append(parameter)

    def parse_data_packet_data(self, data_packet: RemoteDataPacket) -> None:
        data_buffer: bytearray = data_packet.get_data()
        data_index = 0
        for index, _ in enumerate(data_buffer):
            parameter = RemoteParameterServoPosition(
                f"destination {index}",
                f"destination for servo {index}"
            )
            data_index += parameter.parse_from_buffer(data_buffer, data_index)
            self._parameter_list.append(parameter)
