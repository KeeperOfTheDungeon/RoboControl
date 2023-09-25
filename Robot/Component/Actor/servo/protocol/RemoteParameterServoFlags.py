# disabled for micropython  # from typing import Union

from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter

FLAG_REVERSE = 0
FLAG_ON = 1
FLAG_FORCEFEEDBACK_ON = 2
FLAG_POSITIONFEEDBACK_ON = 3

# FLAGS = Union[FLAG_REVERSE, FLAG_ON, FLAG_FORCEFEEDBACK_ON, FLAG_POSITIONFEEDBACK_ON]


class RemoteParameterServoFlags(RemoteParameter):
    def __init__(self, name: str = "servo flags", description: str = "servo flags"):
        super().__init__(name, description, 1)

        self._is_reverse: bool = None
        self._is_on: bool = None
        self._is_force_feedback_on: bool = None
        self._is_position_feedback_on: bool = None

        self._value: int = None

    def get_buffer_size(self) -> int:
        return self._byte_size

    def set_reverse(self, status: bool) -> None:
        self._is_reverse = status

    def set_on(self, status: bool) -> None:
        self._is_on = status

    def is_reverse(self) -> bool:
        return self._is_reverse

    def is_on(self) -> bool:
        return self._is_on

    def is_force_feedback_on(self) -> bool:
        return self._is_force_feedback_on

    def is_position_feedback_on(self) -> bool:
        return self._is_position_feedback_on

    def put_data(self, data_buffer: bytearray) -> None:
        flags = 0
        if self._is_reverse:
            flags |= (1 << FLAG_REVERSE)
        if self._is_on:
            flags |= (1 << FLAG_ON)
        if self._is_force_feedback_on:
            flags |= (1 << FLAG_FORCEFEEDBACK_ON)
        if self._is_position_feedback_on:
            flags |= (1 << FLAG_POSITIONFEEDBACK_ON)
        data_buffer.append(flags)

    @staticmethod
    def _has_flag(flags: int, flag: "FLAGS"):
        res = flags & (1 << flag)
        return res > 0

    def parse_from_buffer(self, data_buffer: bytearray, index: int) -> int:
        flags = data_buffer[index]
        if self._has_flag(flags, FLAG_REVERSE):
            self._is_reverse = True
        if self._has_flag(flags, FLAG_ON):
            self._is_on = True
        if self._has_flag(flags, FLAG_FORCEFEEDBACK_ON):
            self._is_force_feedback_on = True
        if self._has_flag(flags, FLAG_POSITIONFEEDBACK_ON):
            self._is_position_feedback_on = True
        return self._byte_size

    def get_as_string(self, description: bool) -> str:
        infos = []
        if description:
            infos.append(self._name)
            infos.append(f"on={self._is_on}")
            infos.append(f"reverse={self._is_reverse}")
            infos.append(f"forcefeedback={self._is_force_feedback_on}")
            infos.append(f"positionfeedback={self._is_position_feedback_on}")
        else:
            infos.append(f"{self._is_on}")
            infos.append(f"{self._is_reverse}")
            infos.append(f"{self._is_force_feedback_on}")
            infos.append(f"{self._is_position_feedback_on}")
        return ", ".join(infos)
