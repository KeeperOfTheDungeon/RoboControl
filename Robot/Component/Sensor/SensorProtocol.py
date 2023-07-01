from RoboControl.Robot.Component.ComponentProtocol import ComponentProtocol


class SensorProtocol(ComponentProtocol):
    def __init__(self, protocol):
        super().__init__(protocol)
        self._cmd_get_value_id = protocol["cmd_get_value_id"]
        self._msg_value_id = protocol["msg_value_id"]
        self._stream_values_id = protocol["stream_values_id"]
