from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Actor.Actor import Actor
from RoboControl.Robot.Component.Actor.LedProtocol import Cmd_getLedBrightness, Cmd_setLedBrightness


from RoboControl.Robot.Value.BrightnessValue import BrightnessValue


class Led(Actor):
    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._brightness_value = BrightnessValue(meta_data)
        protocol = meta_data.get("protocol")
        self._cmd_setBrightness = protocol["cmd_setBrightness"]
        self._cmd_getValue = protocol["cmd_getValue"]

    def remote_set_brightness(self, brightness: float) -> bool:
        if self._component_protocol is None:
            return False
        cmd = Cmd_setLedBrightness.get_command(self._cmd_setBrightness, self._local_id, brightness )
        return self.send_data(cmd)

    def remote_get_value(self) -> bool:
        if self._component_protocol is None:
            return False
        cmd = Cmd_getLedBrightness.get_command(self._cmd_getValue, self._local_id)
        return self.send_data(cmd)


class LedSet(ComponentSet):
    def __init__(self, components, protocol):
        # TODO why typecast here?
        super().__init__(
            [Led(component) for component in components]
        )

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        return stream_list