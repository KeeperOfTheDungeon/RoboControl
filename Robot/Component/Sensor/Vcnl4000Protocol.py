from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage
from RoboControl.Com.RemoteParameter import RemoteParameterUint16, RemoteParameterUint8
from RoboControl.Robot.Component.Sensor.RemoteParameterVcnl4000Settings import RemoteParameterVcnl4000Settings
from RoboControl.Robot.Component.Sensor.Vcnl4000 import Vcnl4000FrequencyModes, Vcnl4000DistanceSensor, DistanceTable, \
    Vcnl4000DistanceSensorSet

INDEX_SENSOR = 0


class Cmd_getVcnl4000DistanceTable(RemoteCommand):


    def __init__(self, id: int):
        super().__init__(id, "getVcnl4000DistanceTable", "get distance table for VCNL4000 sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))

    @staticmethod
    def get_command(id: int, index: int = None) -> "Cmd_getVcnl4000DistanceTable":
        cmd = Cmd_getVcnl4000DistanceTable(id)
        if index is not None:
            cmd.set_data(index)
        return cmd

    def set_data(self, index: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
    

class Cmd_getVcnl4000RawProximity(RemoteCommand):


    def __init__(self, id):
        # name = "setMpu9150Settings" # description = "set settings for a mpu9150Sensor"
        super().__init__(id, "getProximity", "get VCNL 4000 raw proximity value")
        # RemoteParameterUint8("index","mpu9150 sensor index")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))

    @staticmethod
    def get_command(id, index):
        cmd = Cmd_getVcnl4000RawProximity(id)
        if index is not None:
            cmd.set_data(index)
        return cmd

    def set_data(self, index: int):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
    


class Cmd_setVcnl4000DistanceTable(RemoteCommand):

    def __init__(self, id: int):
        super().__init__(id, "setVcnl4000DistanceTable", "entrys for a VCNL4000 Sensor distance table")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            self._parameter_list.append(RemoteParameterUint8(f"distance{i}", "distance point"))
            self._parameter_list.append(RemoteParameterUint16(f"value{i}", "proximity value"))

    @staticmethod
    def get_command(id: int, index: int = None, distances= None):
        cmd = Cmd_setVcnl4000DistanceTable(id)
        if None not in [index, distances]:
            cmd.set_data(index, distances)
        return cmd

    def set_data(self, index: int, distances) :
        self._parameter_list[INDEX_SENSOR].set_value(index)
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            offset = (i * 2)
            self._parameter_list[offset + 1].set_value(distances.get_Distance(index))
            self._parameter_list[offset + 2].set_value(distances.get_proximity_value(index))

    def get_distance_table(self):
        distances = DistanceTable()
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            offset = (i * 2)
            distance = self._parameter_list[offset + 1].get_value()
            proximity = self._parameter_list[offset + 2].get_value()
            distances.set_proximity_point(i, distance, proximity)
        return distances

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()


class Cmd_setVcnl4000Settings(RemoteCommand):
    INDEX_PARAMETERS = 1
    def __init__(self, id: int):
        # name = "setMpu9150Settings" # description = "set settings for a mpu9150Sensor"
        super().__init__(id, "setVcnl4000Settings", "set settings for a Vcnl4000 Sensor")
        # RemoteParameterUint8("index","mpu9150 sensor index")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        self._parameter_list.append(RemoteParameterVcnl4000Settings())

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            ir_current = None,
            averaging_mode = None,
            proximity_frequency = None,
            auto_conversion: bool = None,
            auto_compensation: bool = None,
    ):
        cmd = Cmd_setVcnl4000Settings(id)
        if None not in [ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation]:
            cmd.set_data(index, ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation)
        return cmd

    def set_data(
            self,
            index: int,
            ir_current,
            averaging_mode,
            proximity_frequency,
            auto_conversion: bool,
            auto_compensation: bool,
    ) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[Cmd_setVcnl4000Settings.INDEX_PARAMETERS].set_ir_current(ir_current)
        self._parameter_list[Cmd_setVcnl4000Settings.INDEX_PARAMETERS].set_averaging_mode(averaging_mode)
        self._parameter_list[Cmd_setVcnl4000Settings.INDEX_PARAMETERS].set_proximity_frequency(proximity_frequency)
        self._parameter_list[Cmd_setVcnl4000Settings.INDEX_PARAMETERS].set_auto_conversion(auto_conversion)
        self._parameter_list[Cmd_setVcnl4000Settings.INDEX_PARAMETERS].set_auto_compensation(auto_compensation)

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()
    


class Msg_vcnl4000DistanceTable(RemoteMessage):
  
    def __init__(self, id: int):
        super().__init__(id, "vcnl4000DistanceTable", "entrys for a VCNL4000 Sensor distance table")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            self._parameter_list.append(RemoteParameterUint8(f"distance{i}", "distance point"))
            self._parameter_list.append(RemoteParameterUint16(f"value{i}", "proximity value"))

    @staticmethod
    def get_command(id: int, index: int = None, distances = None) -> "Msg_vcnl4000DistanceTable":
        cmd = Msg_vcnl4000DistanceTable(id)
        if None not in [index, distances]:
            cmd.set_data(index, distances)
        return cmd

    def set_data(self, index: int, distances) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        for i in range(Vcnl4000DistanceSensor.DISTANCE_DATA_DEEPTH):
            offset = (i * 2)
            self._parameter_list[offset + 1].set_value(distances.get_Distance(index))
            self._parameter_list[offset + 2].set_value(distances.get_proximity_value(index))

    def get_distance_table(self):
        distances = DistanceTable()
        for i in range(Vcnl4000DistanceSensorSet.DISTANCE_DATA_DEEPTH):
            offset = (i * 2)
            distance = self._parameter_list[offset + 1].get_value()
            proximity = self._parameter_list[offset + 2].get_value()
            distances.set_proximity_point(i, distance, proximity)
        return distances

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()




class Msg_vcnl4000RawProximity(RemoteMessage):
    INDEX_PROXIMITY_VALUE = 1

    def __init__(self, id: int):
        super().__init__(id, "proximity", "VCNL 4000 raw proximity value")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        self._parameter_list.append(RemoteParameterUint16("proximity", "proximity value"))

    @staticmethod
    def get_command(id: int, index: int = None, value: int = None):
        cmd = Msg_vcnl4000RawProximity(id)
        if None not in [index, value]:
            cmd.set_data(index, value)
        return cmd

    def set_data(self, index: int, value: int) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[Msg_vcnl4000RawProximity.INDEX_PROXIMITY_VALUE].set_value(value)

    def get_proximity_value(self) -> int:
        return self._parameter_list[Msg_vcnl4000RawProximity.INDEX_PROXIMITY_VALUE].get_value()

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()



class Msg_vcnl4000Settings(RemoteMessage):
    INDEX_PARAMETERS = 1
    def __init__(self, id):
        super().__init__(id, "vcnl4000Settings", "settings for a Vcnl4000 Sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        self._parameter_list.append(RemoteParameterVcnl4000Settings())

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            ir_current = None,
            averaging_mode = None,
            proximity_frequency = None,
            auto_conversion: bool = None,
            auto_compensation: bool = None,
    ):
        cmd = Msg_vcnl4000Settings(id)
        if None not in [ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation]:
            cmd.set_data(index, ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation)
        return cmd

    def set_data(
            self,
            index: int,
            ir_current,
            averaging_mode,
            proximity_frequency: Vcnl4000FrequencyModes,
            auto_conversion: bool,
            auto_compensation: bool,
    ):
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].set_ir_current(ir_current)
        self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].set_averaging_mode(averaging_mode)
        self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].set_proximity_frequency(proximity_frequency)
        self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].set_auto_conversion(auto_conversion)
        self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].set_auto_compensation(auto_compensation)

    def get_ir_current(self):
        return self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].get_ir_current()

    def get_averaging_mode(self):
        return self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].get_averaging_mode()

    def get_proximity_frequency(self):
        return self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].get_proximity_frequency()

    def get_auto_conversion(self) -> bool:
        return self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].get_auto_conversion()

    def get_auto_compensation(self) -> bool:
        return self._parameter_list[Msg_vcnl4000Settings.INDEX_PARAMETERS].get_auto_compensation()

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
