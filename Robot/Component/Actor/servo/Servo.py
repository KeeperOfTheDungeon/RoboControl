from typing import Type, List

from RoboControl.Com.RemoteData import RemoteCommand
from RoboControl.Robot.Component.Actor.Actor import Actor
from RoboControl.Robot.Component.Actor.servo.feedbackServo.protocol.Cmd_calibrateServo import Cmd_calibrateServo
from RoboControl.Robot.Component.Actor.servo.feedbackServo.protocol.Cmd_positionFeedbackOff import \
    Cmd_positionFeedbackOff
from RoboControl.Robot.Component.Actor.servo.feedbackServo.protocol.Cmd_positionFeedbackOn import Cmd_positionFeedbackOn
from RoboControl.Robot.Component.Actor.servo.forceFeedback.protocol.Cmd_forceFeedbackOff import Cmd_forceFeedbackOff
from RoboControl.Robot.Component.Actor.servo.forceFeedback.protocol.Cmd_forceFeedbackOn import Cmd_forceFeedbackOn
from RoboControl.Robot.Component.Actor.servo.forceFeedback.protocol.Cmd_getServoForceThreshold import \
    Cmd_getServoForceThreshold
from RoboControl.Robot.Component.Actor.servo.forceFeedback.protocol.Cmd_setServoForcePosition import \
    Cmd_setServoForcePosition
from RoboControl.Robot.Component.Actor.servo.forceFeedback.protocol.Cmd_setServoForceThreshold import \
    Cmd_setServoForceThreshold
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_getServoPosition import Cmd_getServoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_getServoSpeed import Cmd_getServoSpeed
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_getServoStatus import Cmd_getServoStatus
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_moveServoTo import Cmd_moveServoTo
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_moveServoToAtSpeed import Cmd_moveServoToAtSpeed
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_servoMove import Cmd_servoMove
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_servoOff import Cmd_servoOff
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_servoOn import Cmd_servoOn
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_setServoPosition import Cmd_setServoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_setServoSettings import Cmd_setServoSettings
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_setServoSpeed import Cmd_setServoSpeed
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.servo.ServoDestinationValue import ServoDestinationValue
from RoboControl.Robot.Value.servo.ServoPositionValue import ServoPositionValue
from RoboControl.Robot.Value.servo.ServoVelocityValue import ServoVelocityValue


class Servo(Actor):
    _setup_listener = list()
    _sensor_listener: list() 

    def __init__(self, meta_data):
        super().__init__(meta_data)

        self._offset = 800
        self._scale = 15707
        self._speed: int = None
        self._force_threshold: int = None

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

        self.component_protocol = meta_data["protocol"]

    def set_servo_setup(self, min_range: float, max_range: float, offset: int, scale: int, reverse: bool) -> None:
        self._position.set_range(min_range, max_range)
        self._offset = offset
        self._scale = scale
        self._is_in_reverse_mode = reverse

        for listener in self._setup_listener:
            listener.servo_setup_changed(self)

    def set_speed(self, speed: int) -> bool:
        if self._speed == speed:
            return False
        self._speed = speed
        for listener in self._setup_listener:
            listener.servo_speed_changed(self._global_id, speed)
        return True

    def set_force_threshold(self, threshold: int) -> bool:
        if self._force_threshold == threshold:
            return False
        self._force_threshold = threshold
        for listener in self._setup_listener:
            listener.servo_force_threshold_changed(self._global_id, threshold)
        return True

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

    """
    set_real_position(new_position: int)
    get_real_position() -> int
    """

    def get_min_range(self) -> float:
        return self._position.get_min_range()

    def get_max_range(self) -> float:
        return self._position.get_max_range()

    def get_offset(self) -> int:
        return self._offset

    def get_speed(self) -> int:
        return self._speed

    def get_scale(self) -> int:
        return self._scale

    def get_position_as_degree(self) -> float:
        return self._position.get_value_as_degree()

    def set_on(self, status: bool) -> bool:
        if self._is_on == status:
            return False
        self._is_on = bool(status)
        self._position.set_on(status)
        for listener in self._sensor_listener:
            listener.is_on(self)
        return True

    def is_on(self) -> bool:
        return self._is_on

    def set_force_feedback_on(self, status: bool) -> bool:
        if self._is_force_feedback_on == status:
            return False
        self._is_force_feedback_on = status
        for listener in self._sensor_listener:
            listener.force_feedback_on(self)
        return True

    def is_force_feedback_on(self) -> bool:
        return self._is_force_feedback_on

    def set_position_feedback_on(self, status: bool) -> bool:
        if self._is_position_feedback_on == status:
            return False
        self._is_position_feedback_on = status
        for listener in self._sensor_listener:
            listener.position_feedback_on(self)
        return True

    def is_position_feedback_on(self) -> bool:
        return self._is_position_feedback_on

    def set_at_min(self, status: bool) -> bool:
        if self._position.is_at_min() == status:
            return False
        self._position.set_at_min(status)
        for listener in self._sensor_listener:
            listener.is_at_min(self)
        return True

    def is_at_min(self):
        return self._position.is_at_min()

    def set_at_max(self, status: bool) -> bool:
        if self._position.is_at_max() == status:
            return False
        self._position.set_at_max(status)
        for listener in self._sensor_listener:
            listener.is_at_max(self)
        return True

    def is_at_max(self):
        return self._position.is_at_max()

    def set_active(self, status: bool) -> bool:
        if self._is_active == status:
            return False
        self._is_active = status
        for listener in self._sensor_listener:
            listener.is_active(self)
        return True

    def is_active(self):
        return self._is_active

    def set_reverse(self, direction: bool) -> bool:
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

    def is_reverse(self) -> bool:
        return self._is_in_reverse_mode

    def set_stalling(self, status: bool) -> bool:
        if self._is_stalling == status:
            return False
        self._is_stalling = status
        self._position.set_stalling(status)
        return True

    def is_stalling(self) -> bool:
        return self._is_stalling

    def _get_command(self, protocol_class: Type[RemoteCommand], protocol_key: str, *args) -> RemoteCommand:
        if self.component_protocol is None:
            return None
        cmd_id = self.component_protocol[protocol_key]
        return protocol_class.get_command(
            cmd_id,
            # 1 << self._local_id,  # FIXME this is different from the java source?
            self._local_id,
            *args
        )

    def remote_servo_on(self) -> bool:
        cmd = self._get_command(Cmd_servoOn, "cmd_servoOn")
        return self.send_data(cmd)

    def remote_servo_off(self) -> bool:
        cmd = self._get_command(Cmd_servoOff, "cmd_servoOff")
        return self.send_data(cmd)

    def remote_get_servo_position(self) -> bool:
        cmd = self._get_command(Cmd_getServoPosition, "cmd_getServoPosition")
        return self.send_data(cmd)

    def remote_get_servo_speed(self) -> bool:
        cmd = self._get_command(Cmd_getServoSpeed, "cmd_getServoSpeed")
        return self.send_data(cmd)

    def remote_get_servo_force_threshold(self) -> bool:
        cmd = self._get_command(Cmd_getServoForceThreshold, "cmd_getServoForceThreshold")
        return self.send_data(cmd)

    def remote_get_servo_status(self) -> bool:
        cmd = self._get_command(Cmd_getServoStatus, "cmd_getServoStatus")
        return self.send_data(cmd)

    def remote_calibrate_servo(self):
        cmd = self._get_command(Cmd_calibrateServo, "cmd_calibrateServo")
        return self.send_data(cmd)

    def remote_move_servo(self, velocity: float) -> bool:
        cmd = self._get_command(Cmd_servoMove, "cmd_servoMove", velocity)
        return self.send_data(cmd)

    def remote_move_servo_to(self, position: float) -> bool:
        cmd = self._get_command(Cmd_moveServoTo, "cmd_moveServoTo", position)
        return self.send_data(cmd)

    def remote_move_servo_to_at_speed(self, position: float, speed: float) -> bool:
        cmd = self._get_command(Cmd_moveServoToAtSpeed, "cmd_moveServoTo", position, speed)
        return self.send_data(cmd)

    def remote_set_servo_position(self, position: float) -> bool:
        cmd = self._get_command(Cmd_setServoPosition, "cmd_setServoPosition", position)
        return self.send_data(cmd)

    def remote_set_servo_speed(self, speed: float) -> bool:
        cmd = self._get_command(Cmd_setServoSpeed, "cmd_setServoSpeed", speed)
        return self.send_data(cmd)

    def remote_set_servo_force_threshold(self, value: int) -> bool:
        cmd = self._get_command(
            Cmd_setServoForceThreshold, "cmd_setServoForceThreshold", value
        )
        return self.send_data(cmd)

    def remote_set_servo_force_position(self, value: int) -> bool:
        cmd = self._get_command(
            Cmd_setServoForcePosition, "cmd_setServoForcePosition", value
        )
        return self.send_data(cmd)

    def remote_set_servo_defaults(
            self, min_range: float, max_range: float, offset: int, scale: int, inverse: bool
    ) -> bool:
        cmd = self._get_command(
            Cmd_setServoSettings, "cmd_setServoSettings",
            min_range, max_range, offset, scale, inverse
        )
        return self.send_data(cmd)

    def remote_force_feedback_is_on(self) -> bool:
        cmd = self._get_command(Cmd_forceFeedbackOn, "cmd_forceFeedbackOn")
        return self.send_data(cmd)

    def remote_force_feedback_is_off(self) -> bool:
        cmd = self._get_command(Cmd_forceFeedbackOff, "cmd_forceFeedbackOff")
        return self.send_data(cmd)

    def remote_position_feedback_is_on(self) -> bool:
        cmd = self._get_command(Cmd_positionFeedbackOn, "cmd_positionFeedbackOn")
        return self.send_data(cmd)

    def remote_position_feedback_is_off(self) -> bool:
        cmd = self._get_command(Cmd_positionFeedbackOff, "cmd_positionFeedbackOff")
        return self.send_data(cmd)

    def get_servo_value(self) -> ServoPositionValue:
        return self._position

    def remote_get_value(self) -> bool:
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

    def get_data_values(self) -> List[ComponentValue]:
        val = super().get_data_values()
        # val.add(self._position)
        return val
