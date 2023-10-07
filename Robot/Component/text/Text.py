from RoboControl.Robot.Component.RobotComponent import RobotComponent


class Text(RobotComponent):
	def remote_set_settings(self, user_defined: int) -> bool:
		raise ValueError("WIP: Cmd_setTemplateSettings")
		if self.component_protocol is None:
			return False
		cmd = Cmd_setTemplateSettings.getCommand(
			self.component_protocol.__cmd_set_settings_id, self._local_id, user_defined
		)
		return self.send_data(cmd)

	def remote_get_text(self) -> bool:
		raise ValueError("WIP: Cmd_getText")
		if self.component_protocol is None:
			return False
		cmd = Cmd_getText.getCommand(self.component_protocol._cmd_get_text, self._local_id)
		return self.send_data(cmd)
