from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream
from RoboControl.Com.RemoteParameter import RemoteParameterUint16, RemoteParameterUint8
from RoboControl.Robot.Component.Actor.RemoteParameterServo import RemoteParameterServoFlags, RemoteParameterServoStatus, RemoteParameterServoVelocity, RemoteParameterServoPosition


INDEX_SERVO = 0

class Cmd_getServoPosition(RemoteCommand):
   

    def __init__(self, id):
        super().__init__(id,  "getPosition of a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index = None):
        cmd = Cmd_getServoPosition(id)
        if index is not None:
            cmd.set_index(index)
        return cmd
    

    

class Cmd_getServoSpeed(RemoteCommand):
 
    def __init__(self, id):
        super().__init__(id,  "get speed of a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index = None):
        cmd = Cmd_getServoSpeed(id)
        if index is not None:
            cmd.set_index(index)
        return cmd
    

   


class Cmd_getServoStatus(RemoteCommand):

    def __init__(self, id):
        super().__init__(id,  "get status of a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index = None):
        cmd = Cmd_getServoStatus(id)
        if index is not None:
            cmd.set_index(index)
        return cmd
    




class Cmd_moveServoTo(RemoteCommand):

    INDEX_POSITION = 1

    def __init__(self, id):
        super().__init__(id,  "move servo to given position")

        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_position(self, position):
        self._parameter_list[Cmd_moveServoTo.INDEX_POSITION].set_position(position)

    def get_position(self):
        return self._parameter_list[Cmd_moveServoTo.INDEX_POSITION].get_position()

    @staticmethod
    def get_command(id: int, index, position):
        cmd = Cmd_moveServoTo(id)
        # TODO java source allows skipping index and position
        cmd.set_index(index)
        cmd.set_position(position)
        return cmd
    






class Cmd_moveServoToAtSpeed(RemoteCommand):

    INDEX_POSITION = 1
    INDEX_VELOCITY = 2

    def __init__(self, id):
        super().__init__(id,  "move servo to given position at given speed")

        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))
        self._parameter_list.append(RemoteParameterServoVelocity("velocity", "servo velocity"))

    def set_index(self, index) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_position(self, position) -> None:
        self._parameter_list[Cmd_moveServoToAtSpeed.INDEX_POSITION].set_position(position)

    def get_position(self):
        return self._parameter_list[Cmd_moveServoToAtSpeed.INDEX_POSITION].get_position()

    def set_velocity(self, velocity):
        self._parameter_list[Cmd_moveServoToAtSpeed.INDEX_VELOCITY].set_velocity(velocity)

    def get_velocity(self):
        return self._parameter_list[Cmd_moveServoToAtSpeed.INDEX_VELOCITY].get_velocity()

    @staticmethod
    def get_command(id, index, position, velocity):
        cmd = Cmd_moveServoToAtSpeed(id)
        # TODO java source allows skipping index, position and velocity
        cmd.set_index(index)
        cmd.set_position(position)
        cmd.set_velocity(velocity)
        return cmd




class Cmd_servoMove(RemoteCommand):

    INDEX_VELOCITY = 1

    def __init__(self, id):
        super().__init__(id,  "move servo at given velocity")

        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoVelocity("velocity", "velocity of this movement"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_velocity(self, velocity):
        self._parameter_list[Cmd_servoMove.INDEX_VELOCITY].set_velocity(velocity)

    def get_velocity(self):
        return self._parameter_list[Cmd_servoMove.INDEX_VELOCITY].get_velocity()

    @staticmethod
    def get_command(id: int, index, velocity):
        cmd = Cmd_servoMove(id)
        # TODO java source allows skipping index and position
        cmd.set_index(index)
        cmd.set_velocity(velocity)
        return cmd
    


class Cmd_servoOff(RemoteCommand):

    def __init__(self, id):
        super().__init__(id,  "switch servo off")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, local_id):
        cmd = Cmd_servoOff(id)
        cmd.set_index(1 << local_id)
        return cmd




class Cmd_servoOn(RemoteCommand):
 
    INDEX_SERVO = 0

    def __init__(self, id):
        super().__init__(id,  "switch servo on")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, local_id):
        cmd = Cmd_servoOn(id)
        cmd.set_index(1 << local_id)  # maybe move the 1 << local_id here?
        return cmd
    


class Stream_servosDestinations(RemoteStream):
   
    def __init__(self, id):
        super().__init__(id, "servo destinations")

    @staticmethod
    def get_command(id: int, values):
        cmd = Stream_servosDestinations(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def get_destination(self, index):
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_position()

    def set_data(self, values) :
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_position(value)
            self._parameter_list.append(parameter)

    def make_parameter(self, index: int) -> RemoteParameterServoPosition:
        return RemoteParameterServoPosition(f"destination {index}", "destination for servo " + str(index))

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)

    def get_positions_count(self) -> int:
        return len(self._parameter_list)
    


    
class Cmd_setServoPosition(RemoteCommand):

    INDEX_POSITION = 1

    def __init__(self, id):
        super().__init__(
            id, 
            "set servo position, if received, servo try to reach this position at full speed"
        )
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_position(self, position):
        self._parameter_list[Cmd_setServoPosition.INDEX_POSITION].set_position(position)

    def get_position(self):
        return self._parameter_list[Cmd_setServoPosition.INDEX_POSITION].get_position()

    @staticmethod
    def get_command(id: int, local_id, position) :
        cmd = Cmd_setServoPosition(id)
        cmd.set_index(local_id)
        cmd.set_position(position)
        return cmd





class Cmd_setServoSettings(RemoteCommand):

    INDEX_MIN_RANGE = 1
    INDEX_MAX_RANGE = 2
    INDEX_OFFSET = 3
    INDEX_SCALE = 4
    INDEX_FLAGS = 5
   
    def __init__(self, id):
        super().__init__(id,  "set settings for a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("min range", "servo min range"))
        self._parameter_list.append(RemoteParameterServoPosition("max range", "servo max range"))
        self._parameter_list.append(RemoteParameterUint16("offset", "servo offset"))
        self._parameter_list.append(RemoteParameterUint16("scale", "servo scale"))
        self._parameter_list.append(RemoteParameterServoFlags())

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self) -> int:
        """ "get sensor index for sensor corresponding to this message" """
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_min_range(self):
        return self._parameter_list[Cmd_setServoSettings.INDEX_MIN_RANGE].get_position()

    def get_max_range(self):
        return self._parameter_list[Cmd_setServoSettings.INDEX_MAX_RANGE].get_position()

    def get_offset(self):
        return self._parameter_list[Cmd_setServoSettings.INDEX_OFFSET].get_value()

    def is_reverse(self):
        return self._parameter_list[Cmd_setServoSettings.INDEX_FLAGS].is_reverse()

    def set_data(self, min_range, max_range, offset, scale, reverse):
        self._parameter_list[Cmd_setServoSettings.INDEX_MIN_RANGE].set_position(min_range)
        self._parameter_list[Cmd_setServoSettings.INDEX_MAX_RANGE].set_position(max_range)
        self._parameter_list[Cmd_setServoSettings.INDEX_OFFSET].set_value(offset)
        self._parameter_list[Cmd_setServoSettings.INDEX_SCALE].set_value(scale)
        self._parameter_list[Cmd_setServoSettings.INDEX_FLAGS].set_reverse(reverse)

    @staticmethod
    def get_command(id, local_id, *args):
        cmd = Cmd_setServoSettings(id)
        cmd.set_index(local_id)
        if args:
            cmd.set_data(*args)
        return cmd



class Cmd_setServoSpeed(RemoteCommand):

    INDEX_SPEED = 1
    
    def __init__(self, id):
        super().__init__(
            id, 
            "set servos actual speed"
        )
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("speed", "servo speed"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_speed(self, speed) -> None:
        self._parameter_list[Cmd_setServoSpeed.INDEX_SPEED].set_value(speed)

    def get_speed(self):
        return self._parameter_list[Cmd_setServoSpeed.INDEX_SPEED].get_value()

    @staticmethod
    def get_command(id, local_id, speed = None):
        cmd = Cmd_setServoSpeed(id)
        cmd.set_index(local_id)
        if speed:
            cmd.set_speed(speed)
        return cmd



class Msg_servoPosition(RemoteMessage):
   
    INDEX_POSITION = 1

    def __init__(self, id):
        super().__init__(id,  "actual servo position")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, position: int = None,
    ):
        cmd = Msg_servoPosition(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_position(self) -> float:
        return self._parameter_list[Msg_servoPosition.INDEX_POSITION].get_value()

    def set_data(self, index: int, position: float) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[Msg_servoPosition.INDEX_POSITION].set_value(position)


class Msg_servoSettings(RemoteMessage):
    
    INDEX_MIN_RANGE = 1
    INDEX_MAX_RANGE = 2
    INDEX_OFFSET = 3
    INDEX_SCALE = 4
    INDEX_FLAGS = 5

    def __init__(self, id):
        super().__init__(id,  "actual servo settings")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("min range", "servo min range"))
        self._parameter_list.append(RemoteParameterServoPosition("max range", "servo max range"))
        self._parameter_list.append(RemoteParameterUint16("offset", "servo offset"))
        self._parameter_list.append(RemoteParameterUint16("scale", "servo scale"))
        self._parameter_list.append(RemoteParameterServoFlags())
        # self._parameter_list.append(RemoteParameterServoStatus("scale", "servo scale"))

    @staticmethod
    def get_command(
            id: int,
            index= None, min_range = None, max_range = None,
            offset = None, scale = None, reverse = None
    ):
        cmd = Msg_servoSettings(id)
        if None not in [index, min_range, max_range, offset, scale, reverse]:
            cmd.set_data(index, min_range, max_range, offset, scale, reverse)
        return cmd

    def set_data(self,
                 index: int, min_range, max_range, offset, scale, reverse
                 ):
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[Msg_servoSettings.INDEX_MIN_RANGE].set_position(min_range)
        self._parameter_list[Msg_servoSettings.INDEX_MAX_RANGE].set_position(max_range)
        self._parameter_list[Msg_servoSettings.INDEX_OFFSET].set_value(offset)
        self._parameter_list[Msg_servoSettings.INDEX_SCALE].set_value(scale)
        self._parameter_list[Msg_servoSettings.INDEX_FLAGS].set_reverse(reverse)

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_min_range(self):
        return self._parameter_list[Msg_servoSettings.INDEX_MIN_RANGE].get_position()

    def get_max_range(self):
        return self._parameter_list[Msg_servoSettings.INDEX_MAX_RANGE].get_position()

    def get_offset(self):
        return self._parameter_list[Msg_servoSettings.INDEX_OFFSET].get_value()

    def get_scale(self):
        return self._parameter_list[Msg_servoSettings.INDEX_SCALE].get_value()

    def is_reverse(self):
        return self._parameter_list[Msg_servoSettings.INDEX_FLAGS].is_reverse()

    def is_on(self):
        return self._parameter_list[Msg_servoSettings.INDEX_FLAGS].is_on()

    def is_force_feedback_on(self):
        return self._parameter_list[Msg_servoSettings.INDEX_FLAGS].is_force_feedback_on()

    def is_position_feedback_on(self):
        return self._parameter_list[Msg_servoSettings.INDEX_FLAGS].is_position_feedback_on()


class Msg_servoSpeed(RemoteMessage):

    INDEX_SPEED = 1

    def __init__(self, id):
        super().__init__(id,  "actual servo speed")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterUint16("speed", "servo speed"))

    @staticmethod
    def get_command(
            id: int,
            index = None, speed = None,
    ):
        cmd = Msg_servoSpeed(id)
        if None not in [index, speed]:
            cmd.set_data(index, speed)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_speed(self):
        return self._parameter_list[Msg_servoSpeed.INDEX_SPEED].get_value()

    def set_data(self, index, speed):
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[Msg_servoSpeed.INDEX_SPEED].set_value(speed)


    
class Msg_servoStatus(RemoteMessage):
    
    INDEX_STATUS = 1

    def __init__(self, id):
        super().__init__(id,  "actual servo status")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoStatus("status", "servo status"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            is_on = None, is_active = None, is_reverse = None,
            is_at_min = None, is_at_max = None, is_stalling = None,
    ) -> "Msg_servoStatus":
        cmd = Msg_servoStatus(id)
        if None not in [
            index, is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling
        ]:
            cmd.set_data(index, is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_speed(self):
        return self._parameter_list[INDEX_SERVO].get_value()

    def set_data(
            self, index,
            is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling
    ) :
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[Msg_servoStatus.INDEX_STATUS].set_on(is_on)
        self._parameter_list[Msg_servoStatus.INDEX_STATUS].set_active(is_active)
        self._parameter_list[Msg_servoStatus.INDEX_STATUS].set_reverse(is_reverse)
        self._parameter_list[Msg_servoStatus.INDEX_STATUS].set_at_min(is_at_min)
        self._parameter_list[Msg_servoStatus.INDEX_STATUS].set_at_max(is_at_max)
        self._parameter_list[Msg_servoStatus.INDEX_STATUS].set_stalling(is_stalling)




class Stream_servosPositions(RemoteStream):

    def __init__(self, id):
        super().__init__(id,  "actual servo positions")

    @staticmethod
    def get_command(id, values = None):
        cmd = Stream_servosPositions(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def get_position(self, index: int):
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_position()

    def set_data(self, values):
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_position(value)
            self._parameter_list.append(parameter)

    def make_parameter(self, index: int):
        return RemoteParameterServoPosition(f"position {index}", "position for servo " + str(index))

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)

    def get_positions_count(self):
        return len(self._parameter_list)
    

    
class Stream_servosStatus(RemoteStream):
    
    def __init__(self, id):
        super().__init__(id,  "status from servos")

    def is_on(self, index: int):
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_on()
        return False

    def is_active(self, index: int):
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_active()
        return False

    def is_reverse(self, index: int):
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_reverse()
        return False

    def is_at_min(self, index: int):
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_at_min()
        return False

    def is_at_max(self, index: int):
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_at_max()
        return False

    def is_stalling(self, index: int):
        if index < self.get_parameter_count():
            return self._parameter_list[index].is_stalling()
        return False

    @staticmethod
    def get_command(id, values = None):
        cmd = Stream_servosStatus(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def set_parameter(
            self, index: int,
            is_on, is_active, is_reverse, is_at_min, is_at_max, is_stalling
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

    def make_parameter(self, index):
        return RemoteParameterServoStatus(f"status {index}", "status for servo " + str(index))

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)

