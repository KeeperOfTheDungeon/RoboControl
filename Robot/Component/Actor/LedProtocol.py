from RoboControl.Com.RemoteData import RemoteCommand
from RoboControl.Com.RemoteParameter import RemoteParameterUint8

from RoboControl.Robot.Component.Actor.ActorProtocol import ActorProtocol
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor


class LedProtocol(ActorProtocol):
    def get_command_processors(self, remote_decoder):
        """ "get led command processors"
        @:param "remoteDecoder barometric sensor set"
        @:return "commands processors for barometric sensor"
        """
        print("get command processor in protocol")
        commands = super().get_command_processors(remote_decoder)
        for cmd in [
            RemoteProcessor(Cmd_setLedBrightness(self._cmd_set_value_id), remote_decoder),
            RemoteProcessor(Cmd_getLedBrightness(self._cmd_get_value_id), remote_decoder),
        ]:
            commands.append(cmd)
        return commands

    def get_stream_processors(self, remote_decoder):
        """ "get led stream processors"
        @:param "remoteDecoder led set"
        @:return "stream processors for led"
        """
        commands = super().get_stream_processors(remote_decoder)
        # commands.append( Stream_barometricPressures(self.streamValuesId, sensor) )
        return commands

    def get_message_processors(self, remote_decoder):
        """ "get led message processors"
        @:param "remoteDecoder led set"
        @:return "message processors for led"
        """
        commands = super().get_message_processors(remote_decoder)
        # commands.append( Msg_ledBrightness(self.msgValueId, sensorSet) )
        return commands



class Cmd_getLedBrightness(RemoteCommand):
    _parameter_list =list()
    _index = 0

    def __init__(self, id):
        super().__init__(id, "get brightness of a LED")
        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))

    def set_index(self, index):
        self._parameter_list[self._index].set_value(index)

    def get_index(self):
        return self._parameter_list[self._index].get_value()

    @staticmethod
    def get_command(id, index):
        cmd = Cmd_getLedBrightness()
        cmd.set_id(id)
        cmd.set_index(index)
        return cmd
    


class Cmd_setLedBrightness(RemoteCommand):

    LED_INDEX = 0
    BRIGHTNESS_INDEX = 1

    _parameter_list = list()

    def __init__(self, id):
        super().__init__(id, "set brightness of a LED")
        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))
        self._parameter_list.append(RemoteParameterUint8("brightness", "LED brightness"))

    def set_index(self, index):
        self._parameter_list[Cmd_setLedBrightness.LED_INDEX].set_value(index)

    def get_index(self):
        return self._parameter_list[Cmd_setLedBrightness.LED_INDEX].get_value()

    def set_brightness(self, brightness):
        brightness = int(brightness * 255)
        self._parameter_list[Cmd_setLedBrightness.BRIGHTNESS_INDEX].set_value(brightness)

    def get_brightness(self):
        value = self._parameter_list[Cmd_setLedBrightness.BRIGHTNESS_INDEX].get_value()
        return value / 255

    @staticmethod
    def get_command(id, index, brightness):
        cmd = Cmd_setLedBrightness(id)
        if index:
            cmd.set_index(index)
        if brightness:
            cmd.set_brightness(brightness)
        return cmd


class Cmd_setLedColor(RemoteCommand):

    INDEX_LED = 0
    INDEX_COLOR = 1

    _parameter_list = list()

    def __init__(self, id):
        super().__init__(id,  "set color of an RGB LED")
        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))
   #     self._parameter_list.append(RemoteParameterHsvColor("color", "LED color"))

    def set_index(self, index):
        self._parameter_list[Cmd_setLedColor.INDEX_LED].set_value(index)
        

    def get_index(self):
        return self._parameter_list[Cmd_setLedColor.INDEX_LED].get_value()

    def set_data(self, index: int, color):
        self._parameter_list[Cmd_setLedColor.INDEX_LED].set_value(index)
        self._parameter_list[Cmd_setLedColor.INDEX_COLOR].set_value(color)

    def get_color(self):
        return self._parameter_list[Cmd_setLedColor.INDEX_COLOR].get_color()

    @staticmethod
    def get_command(id, index = None, color=  None):
        cmd = Cmd_setLedColor(id)
        if None not in [index, color]:
            cmd.set_data(index, color)
        return cmd
    
