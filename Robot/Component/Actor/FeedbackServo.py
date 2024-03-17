from RoboControl.Robot.Component.Actor.Servo import Servo


class FeedbackServo(Servo):

	def __init__(self, meta_data):
		super().__init__(meta_data)

		self._is_calibrating = False

	def is_calibrating(self):
		return self._is_calibrating
