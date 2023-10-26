from typing import List

from RoboControl.Robot.Component.protocol.ComponentProtocol import Cmd_loadComponentDefaults, Cmd_getComponentSettings, Cmd_loadComponentDefaults, Cmd_saveComponentDefaults
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor


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
        for cmd in [
            Cmd_getComponentSettings(self._cmd_get_settings_id),
            Cmd_loadComponentDefaults(self._cmd_load_defaults_id),
            Cmd_saveComponentDefaults(self._cmd_save_defaults_id)
        ]:
            processor = RemoteProcessor(cmd, decoder)
            processors.append(processor)
        return processors

    def get_message_processors(self, _decoder) -> List[RemoteProcessor]:
        return []

    def get_stream_processors(self, _decoder) -> List[RemoteProcessor]:
        return []

    def get_exception_processors(self, _decoder) -> List[RemoteProcessor]:
        return []
