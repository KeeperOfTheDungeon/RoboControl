from RoboControl.Robot.Component.statistic.DeviceStatus import DeviceStatus


class CpuStatus(DeviceStatus):

	_SYSTEM_STATE_NAMES  = {"init","running","stopped","selftest","standby"}

#	private SystemState_e systemState=SystemState_e.RUNNING;


	def __init__(self):
		super().__init__()
		self._min_load = 0
		self._max_load = 0
		self._last_load = 0
		self._status_listener = list()

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


"""

public SystemState_e getSystemState()
{
	return(this.systemState);
}


/**
 * gets name of actual system state
 * @return system state
 */

public String getSystemStateAsString()
{
	return(SYSTEM_STATE_NAMES[this.systemState.ordinal()]);
}

	
}
"""