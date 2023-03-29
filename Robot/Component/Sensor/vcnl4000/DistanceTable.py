class DistanceTable:
	def __init__(self):
		self._table = [[0 for x in range(8)] for y in range(2)] 
		pass


	
	def get_Distance(self, index):
		if index < len(self._table):
			return self._table[index] [0]
		return 0

	def set_distance(self, index, distance):
		if index < len(self._table):
			self._table[index] [0] = distance

	def get_proximity_value(self, index):
		if index < len(self._table):
			return self._table[index] [1]
		return 0

	def set_proximity_value(self, index, proximity_value):
		if index < len(self._table):
			self._table[index] [1] = proximity_value


	def set_proximity_point(self, index, distance, proximity_value):
		if index < len(self._table):
			self._table[index] [1] = proximity_value
			self._table[index] [0] = distance
