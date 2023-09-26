from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

LED_INDEX = 0
BRIGHTNESS_INDEX = 1


class Cmd_setLedBrightness(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "setLedBrightness", "set brightness of a LED")

        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))
        self._parameter_list.append(RemoteParameterUint8("brightness", "LED brightness"))

        pass

    def set_index(self, index):
        self._parameter_list[LED_INDEX].set_value(index)

    def get_index(self):
        return self._parameter_list[LED_INDEX].get_value()

    def set_brightness(self, brightness):
        brightness = int(brightness * 255)
        self._parameter_list[BRIGHTNESS_INDEX].set_value(brightness)

    def get_brightness(self):
        value = self.get(self._led_brightness).get_value()
        value /= 255
        return value

    def get_command(id, index, brightness):
        cmd = Cmd_setLedBrightness(id)
        cmd.set_index(index)
        cmd.set_brightness(brightness)

        return (cmd)
