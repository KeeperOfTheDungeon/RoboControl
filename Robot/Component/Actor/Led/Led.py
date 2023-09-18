from RoboControl.Robot.Component.Actor.Actor import Actor
from RoboControl.Robot.Component.Actor.Led.protocol.Cmd_getLedBrightness import Cmd_getLedBrightness
from RoboControl.Robot.Component.Actor.Led.protocol.Cmd_setLedBrightness import Cmd_setLedBrightness
from RoboControl.Robot.Value.BrightnessValue import BrightnessValue


class Led(Actor):
    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._brightness_value = BrightnessValue(meta_data)
        self._component_protocol = meta_data.get("protocol")

    def remote_set_brightness(self, brightness: float) -> bool:
        if self._component_protocol is None:
            return False
        cmd = Cmd_setLedBrightness.get_command(self._component_protocol["cmd_setBrightness"], self._local_id, brightness )
        return self.send_data(cmd)

    def remote_get_value(self) -> bool:
        if self._component_protocol is None:
            return False
        cmd = Cmd_getLedBrightness.get_command(self._component_protocol["cmd_getValue"], self._local_id)
        return self.send_data(cmd)
