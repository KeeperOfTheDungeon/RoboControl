class DeviceStatus:
	def __init__(self):
		self._listener = list()
		

	def add_listener (self, listener):
		self._listener.append(listener)

	def remove_listener(self, listener):
		self._listener.remove(listener)
