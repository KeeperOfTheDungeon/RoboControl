from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent
from RoboControl.Robot.Component.protocol.Cmd_getComponentSettings import Cmd_getComponentSettings
from RoboControl.Robot.Component.protocol.Cmd_getComponentValue import Cmd_getComponentValue
from RoboControl.Robot.Component.protocol.Cmd_loadComponentDefaults import Cmd_loadComponentDefaults
from RoboControl.Robot.Component.protocol.Cmd_saveComponentDefaults import Cmd_saveComponentDefaults


class RobotComponent(AbstractComponent):

    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._sensor_listener = list()
        self._setup_listener = list()
        self._local_id = meta_data["local_id"]
        self._device_address = meta_data["protocol"]["device_id"]

        protocol = meta_data["protocol"]

        self._cmd_get_settings = protocol["cmd_getSettings"]
        self._cmd_save_defaults = protocol["cmd_saveDefaults"]
        self._cmd_load_defaults = protocol["cmd_loadDefaults"]
        self._cmd_get_value = protocol["cmd_getValue"]
        self._transmitter = None
        self._setup_listener = list()
        self._value_listener = list()

    def set_transmitter(self, transmitter):
        self._transmitter = transmitter

    def send_data(self, remote_data):
        remote_data.set_destination_addres(self._device_address)
        if (self._transmitter is not None):
            self._transmitter.transmitt(remote_data)
        return None

    def remote_load_defaults(self):
        return self.send_data(Cmd_loadComponentDefaults.get_command(self._cmd_save_defaults, self._local_id))

    def remote_save_defaults(self):
        return self.send_data(Cmd_saveComponentDefaults.get_command(self._cmd_load_defaults, self._local_id))

    def remote_get_settings(self):
        return self.send_data(Cmd_getComponentSettings.get_command(self._cmd_get_settings, self._local_id))

    def remote_get_component_value(self):
        return self.send_data(Cmd_getComponentValue.get_command(self._cmd_get_value, self._local_id))

    def on_connected(self):
        pass

    def on_disconnected(self):
        pass

    def get_local_id(self):
        return self._local_id

    def get_device_address(self):
        return self._device_address

    def actualize_now(self):
        return False

    def decode_command(self, remote_data):
        return False

    def decode_message(self, remote_data):
        return False

    def decode_stream(self, remote_data):
        return False

    def decode_exception(self, remote_data):
        return False

    def decode(self, remoteData):
        return False

    def notify_setup_changed(self):
        for listener in self._setup_listener:
            listener.settings_changed()

    def add_setup_listener(self, listener):
        self._setup_listener.append(listener)

    def remove_setup_listener(self, listener):
        self._setup_listener.remove(listener)

    def add_value_listener(self, listener):
        self._value_listener.append(listener)

    def remove_value_listener(self, listener):
        self._value_listener.remove(listener)

    def notify_value_changed(self):
        for listener in self._setup_listener:
            listener.value_changed()

    def get_values(self):
        values = list()

    def get_name(self):
        return (self._name)
