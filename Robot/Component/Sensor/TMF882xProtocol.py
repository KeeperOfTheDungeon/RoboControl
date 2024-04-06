from RoboControl.Com.RemoteData import RemoteMessage
from RoboControl.Com.RemoteParameter import RemoteParameterUint8, RemoteParameterUint24, RemoteParameterInt, \
    RemoteParameterInt16

INDEX_SENSOR = 0


class Msg_distance(RemoteMessage):
    SENSOR_VALUE = 1
    CONFIDENCE_VALUE = 2

    def __init__(self, id: int):
        super().__init__(id, "actual distance measured by an distance sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterInt16("distance", "distance value in mm"))
        self._parameter_list.append(RemoteParameterInt16("confidence", "confidence of measured distance"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None, distance: int = None, confidence: int = None
    ):
        cmd = Msg_distance(id)
        if None not in [index, distance, confidence]:
            cmd.set_data(index, distance, confidence)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_distance(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def set_data(self, index: int, distance: int, confidence: int):
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[Msg_distance.SENSOR_VALUE].set_value(distance)
        self._parameter_list[Msg_distance.CONFIDENCE_VALUE].set_value(confidence)
