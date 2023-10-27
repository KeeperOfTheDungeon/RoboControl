import struct
from RoboControl.Com.RemoteData import RemoteStream

from RoboControl.Com.RemoteParameter import RemoteParameter
from RoboControl.Robot.Math.Radiant import Radiant


class RemoteParameterServoVelocity(RemoteParameter):
    def __init__(self, name, description):
        super().__init__(name, description, 2)
        self._velocity: float = 0

    def set_velocity(self, velocity):
        self._velocity = velocity

    def get_velocity(self):
        return self._velocity

    def get_buffer_size(self) -> int:
        return self._byte_size

    def put_data(self, data):
        v = self._velocity * 314.16
        data.join(struct.pack("f", v))

    def parse_from_buffer(self, data_buffer, index):
        position = data_buffer[index:index + self._byte_size]
        position /= 314.16
        self._velocity = position
        return self._byte_size

    def get_as_string(self, description):
        res = ""
        if description:
            res += f"{self._name}="
            res += f"{Radiant.convert_radiant_to_degree(self._velocity)}°"
        else:
            res += f"{self._velocity}"
        return res
    





class RemoteParameterServoPosition(RemoteParameter):

    BYTE_SIZE = 2

    def __init__(self, name, description):
        super().__init__(name, description, RemoteParameterServoPosition.BYTE_SIZE)
        self._value = 0  # position

    def set_position(self, position):
        self._value = position

    def get_position(self):
        return self._value

    def parse_from_buffer(self, data_buffer, index):
        # WIP why?
        position = data_buffer[index] << 8
        position |= data_buffer[index + 1]

        if position > 0x7fff:
            position = position - 0x10000

        # below is same as the java version
        position = float(position)
        self._value = position / 10000

        return self._byte_size

    def get_as_buffer(self):
        position = int(self._value * 10000)
        buffer = bytearray(self._byte_size)
        buffer[0] = (position & 0xff00) >> 8
        buffer[1] = position & 0xff

        return buffer

    def get_as_string(self, description: bool) -> str:
        if description:
            return self.get_name() + "=" + f"{Radiant.convert_radiant_to_degree(self._value):.2f}°"
        return str(self._value)

    def put_data(self, data_buffer):
        data_buffer.append(self._value * 10000)
        return data_buffer



class RemoteParameterServoFlags(RemoteParameter):

    FLAG_REVERSE = 0
    FLAG_ON = 1
    FLAG_FORCEFEEDBACK_ON = 2
    FLAG_POSITIONFEEDBACK_ON = 3


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
            flags |= (1 << RemoteParameterServoFlags.FLAG_REVERSE)
        if self._is_on:
            flags |= (1 << RemoteParameterServoFlags.FLAG_ON)
        if self._is_force_feedback_on:
            flags |= (1 << RemoteParameterServoFlags.FLAG_FORCEFEEDBACK_ON)
        if self._is_position_feedback_on:
            flags |= (1 << RemoteParameterServoFlags.FLAG_POSITIONFEEDBACK_ON)
        data_buffer.append(flags)

    @staticmethod
    def _has_flag(flags, flag):
        res = flags & (1 << flag)
        return res > 0

    def parse_from_buffer(self, data_buffer: bytearray, index):
        flags = data_buffer[index]
        if self._has_flag(flags, RemoteParameterServoFlags.FLAG_REVERSE):
            self._is_reverse = True
        if self._has_flag(flags, RemoteParameterServoFlags.FLAG_ON):
            self._is_on = True
        if self._has_flag(flags, RemoteParameterServoFlags.FLAG_FORCEFEEDBACK_ON):
            self._is_force_feedback_on = True
        if self._has_flag(flags, RemoteParameterServoFlags.FLAG_POSITIONFEEDBACK_ON):
            self._is_position_feedback_on = True
        return self._byte_size

    def get_as_string(self, description: bool):
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



class RemoteParameterServoStatus(RemoteParameter):

    FLAG_IS_ON = 0
    FLAG_IS_ACTIVE = 1
    FLAG_REVERSE = 2
    FLAG_IS_AT_MIN = 3
    FLAG_IS_AT_MAX = 4
    FLAG_IS_STALLING = 5


    def __init__(self, name, description):
        super().__init__(name, description, 2)

        self._reverse = False
        self._on = False
        self._active = False
        self._is_at_min = False
        self._is_at_max = False
        self._stalling = False

    def set_reverse(self, status):
        self._reverse = status

    def is_reverse(self):
        return self._reverse

    def set_on(self, status):
        self._on = status

    def is_on(self):
        return self._on

    def set_active(self, status):
        self._active = status

    def is_active(self):
        return self._active

    def set_at_min(self, status):
        self._is_at_min = status

    def is_at_min(self):
        return self._is_at_min

    def set_at_max(self, status):
        self._is_at_max = status

    def is_at_max(self):
        return self._is_at_max

    def set_stalling(self, status):
        self._stalling = status

    def is_stalling(self):
        return self._stalling

    def parse_from_buffer(self, data_buffer, index):

        flags = data_buffer[index]

        if (flags & (1 << RemoteParameterServoStatus.FLAG_REVERSE)) > 0:
            self._reverse = True
        else:
            self._reverse = False

        if (flags & (1 << RemoteParameterServoStatus.FLAG_IS_ON)) > 0:
            self._on = True
        else:
            self._on = False

        if (flags & (1 << RemoteParameterServoStatus.FLAG_IS_ACTIVE)) > 0:
            self._active = True
        else:
            self._active = False

        if (flags & (1 << RemoteParameterServoStatus.FLAG_IS_AT_MIN)) > 0:
            self._is_at_min = True
        else:
            self._is_at_min = False

        if (flags & (1 << RemoteParameterServoStatus.FLAG_IS_AT_MAX)) > 0:
            self._is_at_max = True
        else:
            self._is_at_max = False

        if (flags & (1 << RemoteParameterServoStatus.FLAG_IS_STALLING)) > 0:
            self._stalling = True

        else:
            self._stalling = False

        return self._byte_size

    def get_as_buffer(self):

        flags = 0

        if self._reverse:
            flags |= (1 << RemoteParameterServoStatus.FLAG_REVERSE)

        if self._on:
            flags |= (1 << RemoteParameterServoStatus.FLAG_IS_ON)

        if self._active:
            flags |= (1 << RemoteParameterServoStatus.FLAG_IS_ACTIVE)

        if self._is_at_min:
            flags |= (1 << RemoteParameterServoStatus.FLAG_IS_AT_MIN)

        if self._is_at_max:
            flags |= (1 << RemoteParameterServoStatus.FLAG_IS_AT_MAX)

        if self._stalling:
            flags |= (1 << RemoteParameterServoStatus.FLAG_IS_STALLING)

        buffer = bytearray(self._byte_size)
        buffer[0] = flags

        return buffer

    def get_as_string(self, description: bool) -> str:
        infos = []
        if description:
            infos.append(self._name)
            infos.append(f"on={self.is_on()}")
            infos.append(f"reverse={self.is_reverse()}")
            infos.append(f"active={self.is_active()}")
            infos.append(f"isAtMin={self.is_at_min()}")
            infos.append(f"isAtMax={self.is_at_max()}")
            infos.append(f"stalling={self.is_stalling()}")
        else:
            infos.append(f"{self.is_on()}")
            infos.append(f"{self.is_reverse()}")
        return ", ".join(infos)
