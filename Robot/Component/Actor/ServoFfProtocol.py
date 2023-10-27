from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream
from RoboControl.Com.RemoteParameter import RemoteParameterUint16, RemoteParameterUint8
from RoboControl.Robot.Component.Actor.RemoteParameterServo import RemoteParameterServoPosition


INDEX_SERVO = 0



class Cmd_calibrateServo(RemoteCommand):
    
    def __init__(self, id: int):
        super().__init__(id, "calibrate analog position measure for this servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_calibrateServo":
        cmd = Cmd_calibrateServo(id)
        if index is not None:
            cmd.set_data(index)
        return cmd
    


class Cmd_positionFeedbackOff(RemoteCommand):
    
    def __init__(self, id: int):
        super().__init__(id,  "switch positionFeedback off")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_positionFeedbackOff":
        cmd = Cmd_positionFeedbackOff(id)
        if index is not None:
            cmd.set_data(1 << index)
        return cmd
    


class Cmd_positionFeedbackOn(RemoteCommand):
  

    def __init__(self, id: int):
        super().__init__(id,  "switch positionFeedback on")
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



class Stream_servoRawAnalogPosition(RemoteStream):
 

    def __init__(self, id):
        super().__init__(id,  "actual analog positions")

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
    def get_command(id: int, positions):
        cmd = Stream_servoRawAnalogPosition(id)
        cmd.set_data(positions)
        return cmd
    




class Cmd_forceFeedbackOff(RemoteCommand):
   
    def __init__(self, id: int):
        super().__init__(id,  "switch forceFeedback off")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None):
        cmd = Cmd_forceFeedbackOff(id)
        if index is not None:
            cmd.set_data(1 << index)
        return cmd
    
class Cmd_forceFeedbackOn(RemoteCommand):
    
    def __init__(self, id: int):
        super().__init__(id,  "switch forceFeedback on")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None):
        cmd = Cmd_forceFeedbackOn(id)
        if index is not None:
            cmd.set_data(1 << index)
        return cmd
    
class Cmd_getServoForcePosition(RemoteCommand):
    

    def __init__(self, id: int):
        super().__init__(id,  "get force position of a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_getServoForcePosition":
        cmd = Cmd_getServoForcePosition(id)
        if index is not None:
            cmd.set_data(index)
        return cmd
    
class Cmd_getServoForceThreshold(RemoteCommand):
    
    def __init__(self, id: int):
        super().__init__(id,  "get force theshold of a servo")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)

    set_index = set_data

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    @staticmethod
    def get_command(id: int, index: int = None):
        cmd = Cmd_getServoForceThreshold(id)
        if index is not None:
            cmd.set_data(index)
        return cmd
    



class Cmd_setServoForcePosition(RemoteCommand):
    
    INDEX_SPEED = 1
    
    def __init__(self, id: int):
        super().__init__(id,  "set servos force position")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterUint16("speed", "new servo force position"))

    def set_data(self, index: int, position: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[Cmd_setServoForcePosition.INDEX_SPEED].set_value(position)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_speed(self) -> int:
        return self._parameter_list[Cmd_setServoForcePosition.INDEX_SPEED].get_value()

    @staticmethod
    def get_command(
            id: int,
            index: int = None, position: int = None
    ):
        cmd = Cmd_setServoForcePosition(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd
    

class Cmd_setServoForceThreshold(RemoteCommand):
    INDEX_SPEED = 1

    def __init__(self, id: int):
        super().__init__(id,  "set servos force threshold")
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterUint16("speed", "new servo force threshold"))

    def set_data(self, index: int, position: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[Cmd_setServoForceThreshold.INDEX_SPEED].set_value(position)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_speed(self) -> int:
        return self._parameter_list[Cmd_setServoForceThreshold.INDEX_SPEED].get_value()

    @staticmethod
    def get_command(
            id: int,
            index: int = None, position: int = None
    ):
        cmd = Cmd_setServoForceThreshold(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd
    

class Msg_servoForceThreshold(RemoteMessage):
    
    INDEX_SPEED = 1

    def __init__(self, id):
        super().__init__(id,  "actual servo force threshold")
        self._servo_index = 0
        self._servo_position = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("speed", "servo force threshold"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            position: int = None,
    ):
        cmd = Msg_servoForceThreshold(id)
        if None not in [index, position]:
            cmd.set_data(index, position)
        return cmd

    def get_index(self) -> int:
        """ "get sensor index for sensor corresponding to this message" """
        return self._parameter_list[INDEX_SERVO].get_value()

    def get_force_threshold(self) -> int:
        """
        :return: "gradient"
        """
        return self._parameter_list[Msg_servoForceThreshold.INDEX_SPEED].get_value()

    def set_data(self, index: int, position: int) -> None:
        self._parameter_list[INDEX_SERVO].set_value(index)
        self._parameter_list[Msg_servoForceThreshold.INDEX_SPEED].set_value(position)


