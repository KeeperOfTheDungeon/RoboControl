from RoboControl.Robot.Component.statistic.DeviceStatus import DeviceStatus


class CpuStatus(DeviceStatus):
    _SYSTEM_STATE_NAMES = ["init", "running", "stopped", "selftest", "standby"]

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
