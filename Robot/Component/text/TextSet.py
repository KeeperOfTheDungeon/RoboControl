from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.text.Text import Text
from RoboControl.Robot.Component.text.protocol.Msg_textFragment import Msg_textFragment


class TextSet(ComponentSet, list[Text]):
	""" "Super class for TSL 2561 Sensor sets." """

	def __init__(self, components: list[dict], protocol: dict):
		super().__init__([Text(meta_data) for meta_data in components])
		self._cmd_get_text = protocol["cmd_getText"]
		self._msg_text_fragment = protocol["msg_textFragment"]

	def process_text_fragment(self, remote_data: Msg_textFragment):
		# remote_data.get_parameter_count()
		pass

	def decode_message(self, remote_data: RemoteMessage) -> bool:
		if isinstance(remote_data, Msg_textFragment):
			self.process_text_fragment(remote_data)
		return False
