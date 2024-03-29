
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Value.ComponentValue import ComponentValue


class Actor(RobotComponent):
    _control_value: ComponentValue

    def __init__(self, meta_data):
        super().__init__(meta_data)

    def remote_get_value(self) -> bool:
        pass

    def get_control_value(self) -> ComponentValue:
        return self._control_value

    def get_control_values(self):
        return [self._control_value]
