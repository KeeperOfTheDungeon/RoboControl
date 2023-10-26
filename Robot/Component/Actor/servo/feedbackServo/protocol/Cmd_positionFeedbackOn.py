from typing import List

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8

INDEX_SERVO = 0


class Cmd_positionFeedbackOn(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int):
        super().__init__(id, "positionFeedbackOn", "switch positionFeedback on")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_positionFeedbackOn":
        cmd = Cmd_positionFeedbackOn(id)
        if index is not None:
            cmd.set_data(1 << index)
        return cmd
