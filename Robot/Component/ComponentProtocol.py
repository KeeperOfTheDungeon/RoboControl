from RoboControl.Robot.Component.protocol.Cmd_getComponentSettings import Cmd_getComponentSettings
from RoboControl.Robot.Component.protocol.Cmd_loadComponentDefaults import Cmd_loadComponentDefaults
from RoboControl.Robot.Component.protocol.Cmd_saveComponentDefaults import Cmd_saveComponentDefaults


class ComponentProtocol:
    def __init__(self, protocol):
        self._cmd_set_settings_id = protocol["cmd_set_settings"]
        self._cmd_get_settings_id = protocol["cmd_get_settings"]
        self._cmd_save_defaults_id = protocol["cmd_save_defaults"]
        self._cmd_load_defaults_id = protocol["cmd_load_defaults"]

        self._msg_settings_id = protocol["msg_settings"]

        self._device_id = protocol["device_id"]

    def get_command_processors(self, decoder):
        processors = list()

        processors.append(Cmd_getComponentSettings(self._cmd_get_settings_id), decoder)
        processors.append(Cmd_loadComponentDefaults(self._cmd_load_defaults_id), decoder)
        processors.append(Cmd_saveComponentDefaults(self._cmd_save_defaults_id), decoder)

        return processors

    def get_message_processors(self, decoder):
        processors = list()
        return processors

    def get_stream_processors(self, decoder):
        processors = list()
        return processors

    def get_exception_processors(self, decoder):
        processors = list()
        return processors
