from RoboControl.Robot.Component.Actor.Actor import Actor
from RoboControl.Robot.Component.Actor.Led.protocol.Cmd_getLedBrightness import Cmd_getLedBrightness
from RoboControl.Robot.Component.Actor.Led.protocol.Cmd_setLedBrightness import Cmd_setLedBrightness
from RoboControl.Robot.Value.BrightnessValue import BrightnessValue


class Led(Actor):
	
	def __init__(self, meta_data):
		super().__init__(meta_data)
		self._brightness_value = BrightnessValue(meta_data)
		protocol = meta_data["protocol"]
		self._cmd_set_led_brightness  = protocol["cmd_setBrightness"]


	def remote_set_brightness(self, brightness):
		cmd = Cmd_setLedBrightness.get_command(self._cmd_set_led_brightness, self._local_id, brightness )
		self.send_data(cmd)

    """
	def remote_send_msg_brightness(self, brightness):
		cmd = Msg_setLedBrightness.get_command(self._cmd_set_led_brightness, self._local_id, brightness )
		self.send_data(cmd)
    """


	def remote_get_value(self):
		cmd = Cmd_getLedBrightness.get_command(self._componentProtocol.cmd_get_value_id,self._local_id)
		cmd.set_brightness
		self.send_data(cmd)
		
		
