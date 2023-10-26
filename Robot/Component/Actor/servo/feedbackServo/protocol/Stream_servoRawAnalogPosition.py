from typing import List, Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.RemoteParameter import RemoteParameterUint16
from RoboControl.Com.RemoteData import RemoteStream
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition


class Stream_servoRawAnalogPosition(RemoteStream):
    _parameter_list: List[Union[RemoteParameterUint16, RemoteParameterServoPosition]]

    def __init__(self, id: int = LegControllerProtocol.STREAM_SERVO_RAW_ANALOG_VALUES):
        super().__init__(id, "servoAnalogRawPositions", "actual analog positions")

    def set_data(self, destinations) :
        for index, position in enumerate(destinations):
            parameter = RemoteParameterUint16(
                f"position {index}",
                f"position for servo {index}"
            )
            parameter.set_value(position)
            self._parameter_list.append(parameter)

    def parse_data_packet_data(self, data_packet):
        data_buffer: bytearray = data_packet.get_data()
        data_index = 0
        for index, _ in enumerate(data_buffer):
            # TODO why not RemoteParameterServoPosition
            parameter = RemoteParameterUint16(
                f"position {index}",
                f"position for servo {index}"
            )
            data_index += parameter.parse_from_buffer(data_buffer, data_index)
            self._parameter_list.append(parameter)

    def get_positions_count(self) -> int:
        return len(self._parameter_list)

    def get_position(self, index: int) -> float:
        if index < len(self._parameter_list):
            parameter: RemoteParameterServoPosition = self._parameter_list[index]
            return parameter.get_position()
        return 0

    @staticmethod
    def get_command(id: int, positions: List[float]):
        cmd = Stream_servoRawAnalogPosition(id)
        cmd.set_data(positions)
        return cmd
