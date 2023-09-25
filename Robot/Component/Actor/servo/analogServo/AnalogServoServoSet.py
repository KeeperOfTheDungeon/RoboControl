from typing import List

from RoboControl.Robot.Component.Actor.servo.ServoSet import ServoSet
from RoboControl.Robot.Component.Actor.servo.analogServo.AnalogServo import AnalogServo


# TODO why
class AnalogServoServoSet(ServoSet, List[AnalogServo]):
	pass
