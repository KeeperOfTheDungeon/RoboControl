class DeviceStatus:
    def __init__(self):
        self._listener = list()

    def add_listener(self, listener):
        self._listener.append(listener)

    def remove_listener(self, listener):
        self._listener.remove(listener)


class ComStatus(DeviceStatus):
    _status_listener = list()

    def __init__(self):
        super().__init__()
        self._recived_messages = 0
        self._transfered_messages = 0
        self._lost_messages = 0
        self._invalid_messages = 0
        self._status_listener = list()

    def get_recived_messages(self):
        return self._recived_messages

    def get_transfered_messages(self):
        return self._transfered_messages

    def get_lost_messages(self):
        return self._lost_messages

    def get_invalid_messages(self):
        return self._invalid_messages

    def add_status_listener(self, listener):
        self._status_listener.append(listener)

    def remove_status_listener(self, listener):
        self._status_listener.remove(listener)

    def process_com_status_message(self, remote_data):
        self._transfered_messages = remote_data.get_transmitted_messages_count()
        self._recived_messages = remote_data.get_received_messages_count()
        self._lost_messages = remote_data.get_invalid_messages_count()
        self._invalid_messages = remote_data.get_lost_messages_count()

        for listener in self._status_listener:
            listener.com_status_changed(self)


class CpuStatus(DeviceStatus):
    _SYSTEM_STATE_NAMES = ["init", "running", "stopped", "selftest", "standby"]
    _status_listener = list()

    def __init__(self):
        super().__init__()
        self._min_load = 0
        self._max_load = 0
        self._last_load = 0
        self._status_listener = list()
        self._system_state = CpuStatus._SYSTEM_STATE_NAMES.index("running")

    def get_min_load(self):
        return self._min_load

    def get_max_load(self):
        return self._max_load

    def get_last_load(self):
        return self._last_load

    def add_status_listener(self, listener):
        self._status_listener.append(listener)

    def remove_status_listener(self, listener):
        self._status_listener.remove(listener)

    def process_cpu_status_message(self, remote_data):
        self._min_load = remote_data.get_min_load()
        self._max_load = remote_data.get_max_load()
        self._last_load = remote_data.get_last_load()

        for listener in self._status_listener:
            listener.cpu_status_changed(self)

    def get_system_state(self):
        return self._system_state

    def get_system_state_as_string(self):
        return CpuStatus._SYSTEM_STATE_NAMES[self._system_state]