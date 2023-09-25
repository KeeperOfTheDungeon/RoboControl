from RoboControl.Robot.Component.Actor.servo.Servo import Servo
from RoboControl.Robot.Component.generic.currentSensor.CurrentSensor import CurrentSensor


class AnalogServo(Servo):
	_current_meter: CurrentSensor

	# AnalogServo(ComponentMetaData metaData, ServoProtocol protocol)
	def __init__(self, meta_data):
		super().__init__(meta_data)
		# self._position = ServoPosition(-90, 90)

	def remote_getValue(self) -> bool:
		raise ValueError("WIP: AnalogServo")
