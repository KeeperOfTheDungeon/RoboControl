from typing import List

from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Actor.servo.Servo import Servo
from RoboControl.Robot.Component.Actor.servo.feedbackServo.protocol.Stream_servoRawAnalogPosition import \
    Stream_servoRawAnalogPosition
from RoboControl.Robot.Component.Actor.servo.forceFeedback.protocol.Msg_servoForceThreshold import \
    Msg_servoForceThreshold
from RoboControl.Robot.Component.Actor.servo.protocol.Msg_servoPosition import Msg_servoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.Msg_servoSpeed import Msg_servoSpeed
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoStatus import RemoteParameterServoStatus
from RoboControl.Robot.Component.Actor.servo.protocol.Stream_servosDestinations import Stream_servosDestinations
from RoboControl.Robot.Component.Actor.servo.protocol.Stream_servosPositions import Stream_servosPositions
from RoboControl.Robot.Component.Actor.servo.protocol.Stream_servosStatus import Stream_servosStatus
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Component.Actor.servo.protocol.Msg_servoSettings import Msg_servoSettings


class ServoSet(ComponentSet, List[Servo]):
    def __init__(self, components, protocol):
        # self._msg_distance = protocol['msg_distance']
        self._msg_settings = protocol['msg_settings']
        self._stream_positions = protocol['stream_servoPositions']
        self._stream_destinations = protocol['stream_servoDestinations']
        self._stream_statuses = protocol['stream_servoStatuses']

        actors = list()

        for component in components:
            actor = Servo(component)
            actors.append(actor)

        super().__init__(actors)

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        cmd = Msg_servoSettings.get_command(self._msg_settings)
        processor = RemoteProcessor(cmd, self)
        return msg_list + [processor]

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

    """def decode_stream(self, remote_data):
        if isinstance(remote_data,Stream_servosPositions):
            self.process_stream_positions(remote_data)
        if isinstance(remote_data,Stream_servosDestinations):
            self.process_stream_destinations(remote_data)
    """

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

    def process_servo_settings(self, remote_data: Msg_servoSettings) -> None:
        servo: Servo = self.get_component_on_local_id(remote_data.get_index())
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

    def process_servo_speed(self, remote_data: Msg_servoSpeed) -> None:
        """ "decode servo speed message and sets the new speed value in servo component" """
        servo: Servo = self.get_component_on_local_id(remote_data.get_index())
        if servo is None:
            return
        servo.set_speed(remote_data.get_speed())

    def process_servo_force_threshold(self, remote_data: Msg_servoForceThreshold) -> None:
        """ "decode servo force threshold message and sets the new force threshold value in servo component" """
        servo: Servo = self.get_component_on_local_id(remote_data.get_index())
        if servo is None:
            return
        servo.set_force_threshold(remote_data.get_force_threshold())

    def process_servos_positions(self, servo_positions: Stream_servosPositions) -> None:
        """ "decode servos positions from remoteStreamData" """
        for index in range(servo_positions.get_parameter_count()):
            servo: Servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            servo.set_position(servo_positions.get_position(index))

    def process_servos_destinations(self, servo_destinations: Stream_servosDestinations) -> None:
        for index in range(servo_destinations.get_parameter_count()):
            servo: Servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            servo.set_destination(servo_destinations.get_destination(index))

    def process_servos_status(self, servos_status: "Stream_servosStatus") -> None:
        for index in range(servos_status.get_parameter_count()):
            servo: Servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            servo.set_active(servos_status.is_active(index))
            servo.set_at_max(servos_status.is_at_max(index))
            servo.set_at_min(servos_status.is_at_min(index))
            servo.set_stalling(servos_status.is_stalling(index))
            servo.set_on(servos_status.is_on(index))
            servo.set_reverse(servos_status.is_reverse(index))

    def process_servo_position(self, servo_position: Msg_servoPosition) -> None:
        """ "decode servo position from DataPacket" """
        servo: Servo = self.get_component_on_local_id(servo_position.get_index())
        if servo is None:
            return
        servo.set_position(servo_position.get_position())

    def process_servos_raw_analog_values(self, raw_analog_values: Stream_servoRawAnalogPosition) -> None:
        for index in range(raw_analog_values.get_parameter_count()):
            servo: Servo = self.get_component_on_local_id(index)
            if servo is None:
                continue
            print("Servo : ", index, " Value : ", raw_analog_values.get_position(index))

    def decode_stream(self, remote_data: RemoteStream) -> bool:
        if isinstance(remote_data, Stream_servosPositions):
            self.process_servos_positions(remote_data)
        elif isinstance(remote_data, Stream_servosDestinations):
            self.process_servos_destinations(remote_data)
        elif isinstance(remote_data, Stream_servosStatus):
            self.process_servos_status(remote_data)
        elif isinstance(remote_data, Stream_servoRawAnalogPosition):
            self.process_servos_raw_analog_values(remote_data)
        return False

    def decode_message(self, remote_data: RemoteMessage) -> bool:
        if isinstance(remote_data, Msg_servoSpeed):
            self.process_servo_speed(remote_data)
        elif isinstance(remote_data, Msg_servoPosition):
            self.process_servo_position(remote_data)
        elif isinstance(remote_data, Msg_servoSettings):
            self.process_servo_settings(remote_data)
        elif isinstance(remote_data, Msg_servoForceThreshold):
            self.process_servo_force_threshold(remote_data)
        return False
    
    def get_component_on_local_id(self, id: int) -> Servo:
        # noinspection PyTypeChecker
        return super().get_component_on_local_id(id)
