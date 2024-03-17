from RoboControl.Robot.Component.Actor.Actor import Actor
from RoboControl.Robot.Component.Actor.RemoteParameterServo import RemoteParameterServoStatus
# from RoboControl.Robot.Component.Actor.ServoFfProtocol import Cmd_calibrateServo, Cmd_forceFeedbackOff, \
#     Cmd_forceFeedbackOn, Cmd_getServoForceThreshold, Cmd_positionFeedbackOff, Cmd_positionFeedbackOn, \
#     Cmd_setServoForcePosition, Cmd_setServoForceThreshold, Msg_servoForceThreshold, Stream_servoRawAnalogPosition
from RoboControl.Robot.Component.Actor.ServoProtocol import Cmd_getServoPosition, Cmd_getServoSpeed, \
    Cmd_getServoStatus, Cmd_loadServoDefaults, Cmd_moveServoTo, Cmd_moveServoToAtSpeed, Cmd_saveServoDefaults, Cmd_servoMove, Cmd_servoOff, Cmd_servoOn, \
    Cmd_setServoPosition, Cmd_setServoSettings, Cmd_setServoSpeed, Msg_servoPosition, Msg_servoSettings, \
    Msg_servoSpeed, Msg_servoStatus, Stream_servosDestinations, Stream_servosPositions, Stream_servosStatus

from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.ServoValue import ServoDestinationValue
from RoboControl.Robot.Value.ServoValue import ServoPositionValue, ServoVelocityValue


class Servo(Actor):
    _setup_listener = list()
    _sensor_listener = list()

    def __init__(self, meta_data):
        super().__init__(meta_data)

        self._offset = 800
        self._scale = 15707
        self._speed: int = 0
        self._force_threshold: int = 0

        self._is_on = False
        self._is_force_feedback_on = False
        self._is_position_feedback_on = False
        self._is_active = False
        self._is_in_reverse_mode = False
        self._is_stalling = False

        self._velocity_control = ServoVelocityValue(meta_data)
        self._velocity_control.add_listener(self)
        self._velocity = ServoVelocityValue(meta_data)
        self._velocity.add_listener(self)

        self._destination_control = ServoDestinationValue(meta_data)
        self._destination_control.add_listener(self)
        self._destination = ServoDestinationValue(meta_data)
        self._destination.add_listener(self)

        self._position = ServoPositionValue(meta_data)
        self._position.add_listener(self)
        self._position_control = ServoPositionValue(meta_data)
        self._position_control.add_listener(self)

        protocol = meta_data.get("protocol")
        self._cmd_getServoSpeed = protocol["cmd_getServoSpeed"]
        self._cmd_setServoSpeed = protocol["cmd_setServoSpeed"]
        self._cmd_servoOn = protocol["cmd_servoOn"]
        self._cmd_servoOff = protocol["cmd_servoOff"]
        self._cmd_getServoStatus = protocol["cmd_getServoStatus"]
        self._cmd_getServoPosition = protocol["cmd_getServoPosition"]
        self._cmd_setServoPosition = protocol["cmd_setServoPosition"]
        # self._cmd_getServoForceThreshold = protocol["cmd_getServoForceThreshold"]
        # self._cmd_calibrateServo = protocol["cmd_calibrateServo"]
        self._cmd_servoMove = protocol['cmd_servoMove']
        self._cmd_servoMoveTo = protocol['cmd_servoMoveTo']
        self._cmd_servoMoveToAtSpeed = protocol['cmd_servoMoveToAtSpeed']
        # self._cmd_setServoForceThreshold = protocol["cmd_setServoForceThreshold"]
        # self._cmd_setServoForcePosition = protocol["cmd_setServoForcePosition"]
        # self._cmd_forceFeedBackOn = protocol["cmd_forceFeedBackOn"]
        # self._cmd_forceFeedBackOff = protocol["cmd_forceFeedBackOff"]
        # self._cmd_positionFeedBackOn = protocol["cmd_positionFeedBackOn"]
        # self._cmd_positionFeedBackOff = protocol["cmd_positionFeedBackOff"]

    def set_servo_setup(self, min_range: float, max_range: float, offset: int, scale: int, reverse: bool) -> None:
        self._position.set_range(min_range, max_range)
        self._destination.set_range(min_range, max_range)
        self._offset = offset
        self._scale = scale
        self._is_in_reverse_mode = reverse

        for listener in self._setup_listener:
            listener.servo_setup_changed(self)

    def set_speed(self, speed: int):
        if self._speed == speed:
            return False
        self._speed = speed
        for listener in self._setup_listener:
            listener.servo_speed_changed(self._global_id, speed)
        return True

    def set_force_threshold(self, threshold: int):
        if self._force_threshold == threshold:
            return False
        self._force_threshold = threshold
        for listener in self._setup_listener:
            listener.servo_force_threshold_changed(self._global_id, threshold)
        return True
    
    def get_force_threshold(self):
        return self._force_threshold

    def set_position(self, new_position: float) -> None:
        self._position.set_value(new_position)

    def get_position(self) -> float:
        return self._position.get_value()

    def set_destination(self, new_destination: float) -> None:
        self._destination.set_value(new_destination)

    def get_angle_value(self) -> ServoPositionValue:
        return self._position

    def get_velocity_control_value(self) -> ServoVelocityValue:
        return self._velocity_control

    def get_destination_control_value(self) -> ServoDestinationValue:
        return self._destination_control

    def get_destination_value(self) -> ServoDestinationValue:
        return self._destination
    
    def get_destination(self) -> float:
        return self._destination.get_value()

    """
    set_real_position(new_position: int)
    get_real_position() -> int
    """

    def get_min_range(self) -> float:
        return self._position.get_min_range()
    
    def set_min_range(self, value: float):
        self._position.set_min_range(value)
        self._destination.set_min_range(value)

    def get_max_range(self) -> float:
        return self._position.get_max_range()
    
    def set_max_range(self, value: float):
        self._position.set_max_range(value)
        self._destination.set_max_range(value)

    def get_offset(self) -> int:
        return self._offset
    
    def set_offset(self, value: int):
        self._offset = value

    def get_speed(self) -> int:
        return self._speed

    def get_scale(self) -> int:
        return self._scale

    def get_position_as_degree(self) -> float:
        return self._position.get_value_as_degree()

    def set_on(self, status: bool):
        if self._is_on == status:
            return False
        self._is_on = bool(status)
        self._position.set_on(status)
        for listener in self._sensor_listener:
            listener.is_on(self)
        return True

    def is_on(self):
        return self._is_on

    def set_force_feedback_on(self, status: bool):
        if self._is_force_feedback_on == status:
            return False
        self._is_force_feedback_on = status
        for listener in self._sensor_listener:
            listener.force_feedback_on(self)
        return True

    def is_force_feedback_on(self):
        return self._is_force_feedback_on

    def set_position_feedback_on(self, status: bool):
        if self._is_position_feedback_on == status:
            return False
        self._is_position_feedback_on = status
        for listener in self._sensor_listener:
            listener.position_feedback_on(self)
        return True

    def is_position_feedback_on(self):
        return self._is_position_feedback_on

    def set_at_min(self, status: bool):
        if self._position.is_at_min() == status:
            return False
        self._position.set_at_min(status)
        for listener in self._sensor_listener:
            listener.is_at_min(self)
        return True

    def is_at_min(self):
        return self._position.is_at_min()

    def set_at_max(self, status: bool):
        if self._position.is_at_max() == status:
            return False
        self._position.set_at_max(status)
        for listener in self._sensor_listener:
            listener.is_at_max(self)
        return True

    def is_at_max(self):
        return self._position.is_at_max()

    def set_active(self, status: bool):
        if self._is_active == status:
            return False
        self._is_active = status
        for listener in self._sensor_listener:
            listener.is_active(self)
        return True

    def is_active(self):
        return self._is_active

    def set_reverse(self, direction: bool):
        """
        "set servos inverse flag if inverse servo change its driving direction from left to right to from right to left"

        :param direction: true for inverted , false for normal
        :return:
        """
        if self._is_in_reverse_mode == direction:
            return False
        self._is_in_reverse_mode = direction
        self._position.set_inverse(direction)
        return True

    def is_reverse(self):
        return self._is_in_reverse_mode

    def set_stalling(self, status: bool):
        if self._is_stalling == status:
            return False
        self._is_stalling = status
        self._position.set_stalling(status)
        return True

    def is_stalling(self):
        return self._is_stalling

    def remote_servo_on(self):
        cmd = Cmd_servoOn.get_command(self._cmd_servoOn, self._local_id)
        return self.send_data(cmd)

    def remote_servo_off(self):
        cmd = Cmd_servoOff.get_command(self._cmd_servoOff, self._local_id)
        return self.send_data(cmd)

    def remote_get_servo_position(self):
        cmd = Cmd_getServoPosition.get_command(self._cmd_getServoPosition, self._local_id)
        return self.send_data(cmd)

    def remote_get_servo_speed(self):
        cmd = Cmd_getServoSpeed.get_command(self._cmd_getServoSpeed, self._local_id)
        return self.send_data(cmd)

    def remote_set_servo_speed(self, speed: float):
        cmd = Cmd_setServoSpeed.get_command(self._cmd_setServoSpeed, speed, self._local_id)
        return self.send_data(cmd)

    # def remote_get_servo_force_threshold(self):
    #     cmd = Cmd_getServoForceThreshold.get_command(self._cmd_getServoForceThreshold, self._local_id)
    #     return self.send_data(cmd)

    def remote_get_servo_status(self):
        cmd = Cmd_getServoStatus.get_command(self._cmd_getServoStatus, self._local_id)
        return self.send_data(cmd)

    # def remote_calibrate_servo(self):
    #     cmd = Cmd_calibrateServo.get_command(self._cmd_calibrateServo, self._local_id)
    #     return self.send_data(cmd)

    def remote_move_servo(self, velocity: float):
        cmd = Cmd_servoMove.get_command(self._cmd_servoMove, self._local_id, velocity)
        return self.send_data(cmd)

    def remote_move_servo_to(self, position: float):
        cmd = Cmd_moveServoTo.get_command(self._cmd_moveServoTo, self._local_id, position)
        return self.send_data(cmd)

    def remote_move_servo_to_at_speed(self, position: float, speed: float):
        cmd = Cmd_moveServoToAtSpeed.get_command(self._cmd_moveServoToAtSpeed, self._local_id, position, speed)
        return self.send_data(cmd)

    def remote_set_servo_position(self, position: float):
        cmd = Cmd_setServoPosition.get_command(self._cmd_setServoPosition, self._local_id, position)
        return self.send_data(cmd)

    # def remote_set_servo_force_threshold(self, value: int):
    #     cmd = Cmd_setServoForceThreshold.get_command(self._cmd_setServoForceThreshold, self._local_id, value)
    #     return self.send_data(cmd)

    # def remote_set_servo_force_position(self, value: int):
    #     cmd = Cmd_setServoForcePosition.get_command(self._cmd_setServoForcePosition, self._local_id, value)
    #     return self.send_data(cmd)

    def remote_set_servo_defaults(
            self, min_range: float, max_range: float, offset: int, scale: int, inverse: bool
    ):
        cmd = Cmd_setServoSettings.get_command(min_range, max_range, offset, scale, inverse)
        return self.send_data(cmd)

    # def remote_force_feedback_is_on(self):
    #     cmd = Cmd_forceFeedbackOn.get_command(self._cmd_forceFeedBackOn, self._local_id)
    #     return self.send_data(cmd)

    # def remote_force_feedback_is_off(self):
    #     cmd = Cmd_forceFeedbackOff.get_command(self._cmd_forceFeedBackOff, self._local_id)
    #     return self.send_data(cmd)

    # def remote_position_feedback_is_on(self):
    #     cmd = Cmd_positionFeedbackOn.get_command(self._cmd_positionFeedBackOn, self._local_id)
    #     return self.send_data(cmd)

    # def remote_position_feedback_is_off(self):
    #     cmd = Cmd_positionFeedbackOff.get_command(self._cmd_positionFeedBackOff, self._local_id)
    #     return self.send_data(cmd)

    def get_servo_value(self) -> ServoPositionValue:
        return self._position

    def remote_get_value(self):
        raise ValueError("WIP")

    def component_value_changed(self, component_value: ComponentValue) -> None:
        if component_value == self._velocity_control:
            self.remote_move_servo(self._velocity_control.get_value())
        elif component_value == self._destination_control:
            position = self._destination_control.get_value()
            velocity = self._destination_control.get_velocity()
            if velocity == 0:
                self.remote_move_servo_to(position)
            else:
                self.remote_move_servo_to_at_speed(position, velocity)
        elif component_value == self._position:
            for listener in self._sensor_listener:
                listener.servo_position_changed(self)

    def get_data_values(self):
        val = super().get_data_values()
        # val.add(self._position)
        return val


class ServoSet(ComponentSet):
    def __init__(self, components, protocol):
        self._msg_settings = protocol['msg_settings']
        self._msg_servo_status = protocol['msg_servo_status']
        self._msg_servo_speed = protocol['msg_servo_speed']
        self._msg_servo_position = protocol['msg_servo_position']
        self._stream_positions = protocol['stream_servoPositions']
        self._stream_destinations = protocol['stream_servoDestinations']
        self._stream_statuses = protocol['stream_servoStatuses']
        self._cmd_servoOn = protocol['cmd_servoOn']
        self._cmd_servoOff = protocol['cmd_servoOff']
        self._cmd_getServoPosition = protocol['cmd_getServoPosition']
        self._cmd_setServoPosition = protocol['cmd_setServoPosition']
        self._cmd_servoMove = protocol['cmd_servoMove']
        self._cmd_servoMoveTo = protocol['cmd_servoMoveTo']
        self._cmd_servoMoveToAtSpeed = protocol['cmd_servoMoveToAtSpeed']
        self._cmd_saveServoDefaults = protocol['cmd_saveDefaults']
        self._cmd_loadServoDefaults = protocol['cmd_loadDefaults']
        self._cmd_getServoSpeed = protocol['cmd_getServoSpeed']
        self._cmd_setServoSpeed = protocol['cmd_setServoSpeed']

        actors = list()

        for component in components:
            actor = Servo(component)
            actors.append(actor)

        super().__init__(actors)

    def get_command_processors(self):
        command_list = super().get_command_processors()
        
        command_list.append(RemoteProcessor(Cmd_servoOn(self._cmd_servoOn), self))
        command_list.append(RemoteProcessor(Cmd_servoOff(self._cmd_servoOff), self))
        command_list.append(RemoteProcessor(Cmd_getServoPosition(self._cmd_getServoPosition), self)) # BROKEN
        command_list.append(RemoteProcessor(Cmd_setServoPosition(self._cmd_setServoPosition), self))
        command_list.append(RemoteProcessor(Cmd_servoMove(self._cmd_servoMove), self))
        command_list.append(RemoteProcessor(Cmd_moveServoTo(self._cmd_servoMoveTo), self))
        command_list.append(RemoteProcessor(Cmd_moveServoToAtSpeed(self._cmd_servoMoveToAtSpeed), self))
        command_list.append(RemoteProcessor(Cmd_saveServoDefaults(self._cmd_saveServoDefaults), self))
        command_list.append(RemoteProcessor(Cmd_loadServoDefaults(self._cmd_loadServoDefaults), self))
        command_list.append(RemoteProcessor(Cmd_getServoSpeed(self._cmd_getServoSpeed), self))
        command_list.append(RemoteProcessor(Cmd_setServoSpeed(self._cmd_setServoSpeed), self))
        
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        cmd = Msg_servoSettings.get_command(self._msg_settings)
        processor = RemoteProcessor(cmd, self)
        msg_list.append(processor)

        cmd = Msg_servoStatus.get_command(self._msg_servo_status)
        processor = RemoteProcessor(cmd, self)
        msg_list.append(processor)

        cmd = Msg_servoStatus.get_command(self._msg_servo_speed)
        processor = RemoteProcessor(cmd, self)
        msg_list.append(processor)
        
        msg_list.append(RemoteProcessor(Msg_servoPosition(self._msg_servo_position), self))

        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()

        if self._stream_positions != 0:
            initial_values = [0 for i in self]
            cmd = Stream_servosPositions.get_command(self._stream_positions, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)

        if self._stream_destinations != 0:
            initial_values = [0 for i in self]
            cmd = Stream_servosDestinations.get_command(self._stream_destinations, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)

        if self._stream_statuses != 0:
            initial_values = [RemoteParameterServoStatus("WIP", "WIP") for i in self]
            cmd = Stream_servosStatus.get_command(self._stream_statuses, initial_values)
            processor = RemoteProcessor(cmd, self)
            stream_list.append(processor)

        return stream_list

    def process_stream_positions(self, stream_positions):
        for sensor in self:
            index = sensor.get_local_id()
            value = stream_positions.get_position(index)
            sensor.set_position(value)

    def process_stream_destinations(self, stream_destitions):
        for sensor in self:
            index = sensor.get_local_id()
            value = stream_destitions.get_destination(index)
            sensor.set_destination(value)

    def process_servo_settings(self, remote_data):
        servo = self.get_component_on_local_id(remote_data.get_index())
        if servo is None:
            return
        servo.set_servo_setup(
            remote_data.get_min_range(),
            remote_data.get_max_range(),
            remote_data.get_offset(),
            remote_data.get_scale(),
            remote_data.is_reverse(),
        )
        servo.set_on(remote_data.is_on())
        # servo.set_remote_feedback_on(remote_data.force_feedback_is_on())
        # servo.set_position_feedback_on(remote_data.position_feedback_is_on())

    def process_servo_speed(self, remote_data):
        """ "decode servo speed message and sets the new speed value in servo component" """
        servo = self.get_component_on_local_id(remote_data.get_index())
        if servo is None:
            return
        servo.set_speed(remote_data.get_speed())

    def process_servo_force_threshold(self, remote_data) -> None:
        """ "decode servo force threshold message and sets the new force threshold value in servo component" """
        servo = self.get_component_on_local_id(remote_data.get_index())
        if servo is None:
            return
        servo.set_force_threshold(remote_data.get_force_threshold())

    def process_servos_positions(self, servo_positions):
        """ "decode servos positions from remoteStreamData" """
        for index in range(servo_positions.get_parameter_count()):
            servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            servo.set_position(servo_positions.get_position(index))

    def process_servos_destinations(self, servo_destinations):
        for index in range(servo_destinations.get_parameter_count()):
            servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            servo.set_destination(servo_destinations.get_destination(index))

    def process_servos_status(self, servos_status):
        for index in range(servos_status.get_parameter_count()):
            servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            servo.set_active(servos_status.is_active(index))
            servo.set_at_max(servos_status.is_at_max(index))
            servo.set_at_min(servos_status.is_at_min(index))
            servo.set_stalling(servos_status.is_stalling(index))
            servo.set_on(servos_status.is_on(index))
            servo.set_reverse(servos_status.is_reverse(index))

    def process_servo_position(self, servo_position: Msg_servoPosition):
        """ "decode servo position from DataPacket" """
        servo = self.get_component_on_local_id(servo_position.get_index())
        if servo is None:
            return
        servo.set_position(servo_position.get_position())

    def process_servos_raw_analog_values(self, raw_analog_values):
        for index in range(raw_analog_values.get_parameter_count()):
            servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            print("Servo : ", index, " Value : ", raw_analog_values.get_position(index))
            
    def process_servo_on(self, remote_command: Cmd_servoOn):
        index = remote_command.get_index()
        self.servo_on(index)
        return True
        
    def process_servo_off(self, remote_command: Cmd_servoOff):
        index = remote_command.get_index()
        self.servo_off(index)
        return True
    
    def process_get_servo_position(self, remote_command: Cmd_getServoPosition):
        index = remote_command.get_index()
        return self.remote_get_position_response(index)
    
    def process_set_servo_position(self, remote_command: Cmd_setServoPosition):
        index = remote_command.get_index()
        position = self.get_position(index)
        self.set_position(position)
        return True
    
    def process_get_servo_status(self, remote_command: Cmd_getServoStatus):
        index = remote_command.get_index()
        return self.remote_get_status_response(index)

    def process_save_defaults(self, remote_command: Cmd_saveServoDefaults):
        index = remote_command.get_index()
        self.save_defaults(index)
        return True
    
    def process_load_defaults(self, remote_command: Cmd_loadServoDefaults):
        index = remote_command.get_index()
        self.load_defaults(index)
        return True

    def process_servo_move(self, remote_command: Cmd_servoMove):
        index = remote_command.get_index()
        velocity = remote_command.get_velocity()
        self.move(index, velocity)
        return True
    
    def process_move_servo_to(self, remote_command: Cmd_moveServoTo):
        index = remote_command.get_index()
        position = remote_command.get_position()
        self.move_to(index, position)
        return True
    
    def process_move_servo_to_at_speed(self, remote_command: Cmd_moveServoToAtSpeed):
        index = remote_command.get_index()
        position = remote_command.get_position()
        speed = remote_command.get_velocity()
        self.move_to_at_speed(index, position, speed)
        return True
    
    def process_set_servo_speed(self, remote_command: Cmd_setServoSpeed):
        index = remote_command.get_index()
        speed = remote_command.get_speed()
        self.set_speed(index, speed)
        return True
    
    def process_get_servo_speed(self, remote_command: Cmd_getServoSpeed):
        index = remote_command.get_index()
        return self.remote_get_speed_response(index)
        

    def decode_stream(self, remote_data):
        if isinstance(remote_data, Stream_servosPositions):
            self.process_servos_positions(remote_data)
        elif isinstance(remote_data, Stream_servosDestinations):
            self.process_servos_destinations(remote_data)
        elif isinstance(remote_data, Stream_servosStatus):
            self.process_servos_status(remote_data)
        return False

    def decode_message(self, remote_data):
        if isinstance(remote_data, Msg_servoSpeed):
            self.process_servo_speed(remote_data)
        elif isinstance(remote_data, Msg_servoPosition):
            self.process_servo_position(remote_data)
        elif isinstance(remote_data, Msg_servoSettings):
            self.process_servo_settings(remote_data)
        return False
    
    def decode_command(self, remote_data):
        if isinstance(remote_data, Cmd_servoOn):
            self.process_servo_on(remote_data)
        elif isinstance(remote_data, Cmd_servoOff):
            self.process_servo_off(remote_data)
        elif isinstance(remote_data, Cmd_getServoPosition):
            self.process_get_servo_position(remote_data)
        elif isinstance(remote_data, Cmd_setServoPosition):
            self.process_set_servo_position(remote_data)
        elif isinstance(remote_data, Cmd_saveServoDefaults):
            self.process_save_defaults(remote_data)
        elif isinstance(remote_data, Cmd_loadServoDefaults):
            self.process_load_defaults(remote_data)
        elif isinstance(remote_data, Cmd_servoMove):
            self.process_servo_move(remote_data)
        elif isinstance(remote_data, Cmd_moveServoTo):
            self.process_move_servo_to(remote_data)
        elif isinstance(remote_data, Cmd_moveServoToAtSpeed):
            self.process_move_servo_to_at_speed(remote_data)
        elif isinstance(remote_data, Cmd_getServoSpeed):
            self.process_get_servo_speed(remote_data)
        elif isinstance(remote_data, Cmd_setServoSpeed):
            self.process_set_servo_speed(remote_data)
        elif isinstance(remote_data, Cmd_getServoStatus):
            self.process_get_servo_status(remote_data)
        return False 

    def get_component_on_local_id(self, id):
        # noinspection PyTypeChecker
        return super().get_component_on_local_id(id)