from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Actor.Actor import Actor
from RoboControl.Robot.Component.Actor.LedProtocol import Cmd_getLedBrightness, Cmd_setLedBrightness


from RoboControl.Robot.Value.ComponentValue import BrightnessValue
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor

class Led(Actor):
    def __init__(self, meta_data):
        super().__init__(meta_data)
        print("Add a led")
        self._brightness_value = BrightnessValue(meta_data)
        protocol = meta_data.get("protocol")
        self._cmd_setBrightness = protocol["cmd_setBrightness"]
        self._cmd_getBrightness = protocol["cmd_getBrightness"]



    def remote_set_brightness(self, brightness: float) -> bool:
        cmd = Cmd_setLedBrightness.get_command(self._cmd_setBrightness, self._local_id, brightness )
        return self.send_data(cmd)


    def remote_get_brightness(self) -> bool:
        cmd = Cmd_getLedBrightness.get_command(self._cmd_getValue, self._cmd_getBrightness)
        return self.send_data(cmd)


class LedSet(ComponentSet):
    def __init__(self, components, protocol):
        # TODO why typecast here?
        super().__init__(
            [Led(component) for component in components]
        )
        self._cmd_setBrightness = protocol["cmd_setBrightness"]
        self._cmd_getBrightness = protocol["cmd_getBrightness"]


    

    def get_command_processors(self):
        command_list = super().get_command_processors()
        command_list.append(RemoteProcessor(Cmd_setLedBrightness(self._cmd_setBrightness), self))
        command_list.append(RemoteProcessor(Cmd_getLedBrightness(self._cmd_getBrightness), self))
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        return stream_list

    def decode_command(self, remote_command):
        if isinstance(remote_command, Cmd_setLedBrightness):
            print("got brightness") #self.process_ping_command(remote_command)
            return True
        if isinstance(remote_command, Cmd_getLedBrightness):
            print("get Valuuueee") #self.process_ping_command(remote_command)
            return True

