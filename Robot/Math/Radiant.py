import math


class Radiant:
    @staticmethod
    def convert_radiant_to_degree(angle: float) -> float:
        degree = angle * (180.0 / math.pi)
        return degree

    @staticmethod
    def convert_degree_to_radiant(angle: float) -> float:
        radiant = (angle * math.pi) / 180.0
        return radiant
