import math


class Radiant:

	
	def convert_radiant_to_degree(angle):
		degree = angle* (180.0/math.pi)
		return degree

	def convert_degree_to_radiant(angle):
		radiant = (angle*math.pi) / 180.0
		return radiant
