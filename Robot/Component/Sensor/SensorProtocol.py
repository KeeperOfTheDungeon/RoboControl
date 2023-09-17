from RoboControl.Robot.Component.ComponentProtocol import ComponentProtocol


class SensorProtocol(ComponentProtocol):

    def __init__(
            self, device_id,
            cmd_set_settings_id,
            cmd_get_settings_id,
            cmd_save_defaults_id,
            cmd_load_defaults_id,
            msg_settings_id,

            cmd_get_value_id,
            msg_value_id,
            stream_values_id
    ):
        super().__init__(
            self, device_id,
            cmd_set_settings_id,
            cmd_get_settings_id,
            cmd_save_defaults_id,
            cmd_load_defaults_id,
            msg_settings_id
        )

        self._cmd_get_value_id = cmd_get_value_id
        self._msg_value_id = msg_value_id
        self._stream_values_id = stream_values_id
