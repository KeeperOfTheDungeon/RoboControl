from copy import deepcopy
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Component.Sensor.DistanceSensor import DistanceSensor, DistanceSensorSet
from RoboControl.Robot.Component.Sensor.LuxSensor import LuxSensor, LuxSensorSet





class Vcnl4000(RobotComponent):
    _max_range = 0
    _min_range = 0
    _beam_width = 0

    def __init__(self, meta_data):
        super().__init__(meta_data)

        self._lux_sensor = Vcnl4000LuxSensor(meta_data)
        self._distance_sensor = Vcnl4000DistanceSensor(meta_data)

    def get_lux_sensor(self):
        return self._lux_sensor

    def get_distance_sensor(self):
        return self._distance_sensor

    def set_transmitter(self, transmitter):
        super().set_transmitter(transmitter)
        self._lux_sensor.set_transmitter(transmitter)
        self._distance_sensor.set_transmitter(transmitter)



class Vcnl4000Set(ComponentSet):
    def __init__(self, components, protocol):

        lux_sensors = list()
        distance_sensors = list()
        vcnl_sensors = list()

        for component in components:
            sensor = Vcnl4000(component)
            vcnl_sensors.append(sensor)
            lux_sensors.append(sensor.get_lux_sensor())
            distance_sensors.append(sensor.get_distance_sensor())

        super().__init__(vcnl_sensors)

        protocol["cmd_getValue"] = protocol["cmd_getLux"]
        self._lux_sensor_set = Vcnl4000LuxSensorSet(lux_sensors, protocol)

        protocol["cmd_getValue"] = protocol["cmd_getDistance"]
        self._distance_sensor_set = Vcnl4000DistanceSensorSet(distance_sensors, protocol)

    def get_distance_sensor(self):
        return self._distance_sensor

    def get_lux_sensors(self):
        return self._lux_sensor_set

    def get_distance_sensors(self):
        return self._distance_sensor_set

    def get_command_processors(self):
        command_list = super().get_command_processors()
        command_list.extend(self._lux_sensor_set.get_command_processors())
        command_list.extend(self._distance_sensor_set.get_command_processors())

        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        msg_list.extend(self._lux_sensor_set.get_message_processors())
        msg_list.extend(self._distance_sensor_set.get_message_processors())

        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        stream_list.extend(self._lux_sensor_set.get_stream_processors())
        stream_list.extend(self._distance_sensor_set.get_stream_processors())

        return stream_list

    # noinspection PyTypeChecker
    def get_component_on_local_id(self, index: int) -> Vcnl4000:
        return super().get_component_on_local_id(index)

    def process_settings(self, remote_message) :
        index = remote_message.get_index()
        sensor = self.get_component_on_local_id(index)
        if sensor is None:
            return
        sensor.set_settigs(
            
        )



class Vcnl4000LuxSensor(LuxSensor):

    VCNL4000_MAX_RANGE = 16383.5
    VCNL4000_MIN_RANGE = 0.0

    def __init__(self, meta_data):
        meta_data["min_range"] = Vcnl4000LuxSensor.VCNL4000_MIN_RANGE
        meta_data["max_range"] = Vcnl4000LuxSensor.VCNL4000_MAX_RANGE
        meta_data["protocol"]['cmd_getValue'] = meta_data["protocol"]['cmd_getLux']
        super().__init__(meta_data)
        self._gain = 0


class Vcnl4000LuxSensorSet(LuxSensorSet):
    pass



class Vcnl4000DistanceSensor(DistanceSensor):
    
    DISTANCE_DATA_DEEPTH = 8

    VCNL4000_BEAM_WIDTH = 30.0

    VCNL4000_MAX_RANGE = 200.0
    VCNL4000_MIN_RANGE = 1.0
    VCNL4000_MAX_GRANULARITY = 10.0
    
    _setup_listener = list()

    def __init__(self, meta_data):
        meta_data["beam_width"] = Vcnl4000DistanceSensor.VCNL4000_BEAM_WIDTH
        meta_data["min_range"] = Vcnl4000DistanceSensor.VCNL4000_MIN_RANGE
        meta_data["max_range"] = Vcnl4000DistanceSensor.VCNL4000_MAX_RANGE
        meta_data["granularity"] = Vcnl4000DistanceSensor.VCNL4000_MAX_GRANULARITY
        meta_data["protocol"]['cmd_getValue'] = meta_data["protocol"]['cmd_getDistance']
        super().__init__(meta_data)

    #	self._proximityValue = 0
    #	self._distance_table = DistanceTable()

    #	def set_proximity_value(self, proximity_value):
    #		self._proximityValue = proximity_value

    #	def get_proximity_value(self):
    #		return self._proximityValue

    def set_distance_table(self, distance_table):
        self._distance_table = deepcopy.copy(distance_table)

        for listener in self._setup_listener:
            listener.distance_table_changed(self)

    def get_distance_table(self):
        return deepcopy.copy(self._distance_table)
    

class Vcnl4000DistanceSensorSet(DistanceSensorSet):
    pass


class Vcnl4000AveragingModes:
    def __init__(self, number: int, averaging: int):
        self._number = number
        self._averaging = averaging

    def get_number(self) -> int:
        return self._number

    def get_averaging(self) -> int:
        return self._averaging

    @staticmethod
    def get(index: int):
        for value in Vcnl4000AveragingModesEnum.values():
            if value.get_number() == index:
                return value
        return Vcnl4000AveragingModesEnum.AVERAGING_32

    @staticmethod
    def get_default():
        """ "sensors default averaging mode (32 conversions). This mode is set automatic on sensors reset." """
        return Vcnl4000AveragingModesEnum.AVERAGING_32

    def __str__(self):
        return f"{self._averaging} samples"


class Vcnl4000AveragingModesEnum:
    AVERAGING_1 = Vcnl4000AveragingModes(0, 0)
    AVERAGING_2 = Vcnl4000AveragingModes(1, 12)
    AVERAGING_4 = Vcnl4000AveragingModes(2, 4)
    AVERAGING_8 = Vcnl4000AveragingModes(3, 8)
    AVERAGING_16 = Vcnl4000AveragingModes(4, 16)
    AVERAGING_32 = Vcnl4000AveragingModes(5, 32)
    AVERAGING_64 = Vcnl4000AveragingModes(6, 64)
    AVERAGING_128 = Vcnl4000AveragingModes(7, 128)

    @staticmethod
    def values() -> list[Vcnl4000AveragingModes]:
        return [f for f in dir(Vcnl4000AveragingModesEnum) if isinstance(f, Vcnl4000AveragingModes)]



class Vcnl4000FrequencyModes:
    def __init__(self, number, frequency):
        self._number = number
        self._frequency = frequency

    def get_number(self):
        return self._number

    def get_frequency(self):
        return self._frequency

    @staticmethod
    def get(index: int):
        for value in Vcnl4000FrequencyModesEnum.values():
            if value.get_number() == index:
                return value
        return Vcnl4000FrequencyModesEnum.MODE_3_125_MHZ

    @staticmethod
    def get_default():
        """ "get vcnl4000 default frequency mode. This mode is set on Sensor reset" """
        return Vcnl4000FrequencyModesEnum.MODE_781_25_KHZ

    def __str__(self):
        return f"{self._frequency}"



class Vcnl4000FrequencyModesEnum:
    MODE_3_125_MHZ = Vcnl4000FrequencyModes(0, "3.125 MHz")
    MODE_1_5625_MHZ = Vcnl4000FrequencyModes(1, "1.5625 MHz")
    MODE_781_25_KHZ = Vcnl4000FrequencyModes(2, "781.25 kHz")
    MODE_390_625_Khz = Vcnl4000FrequencyModes(3, "390.625 kHz")

    @staticmethod
    def values() -> list[Vcnl4000FrequencyModes]:
        return [f for f in dir(Vcnl4000FrequencyModesEnum) if isinstance(f, Vcnl4000FrequencyModes)]


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


class Vcnl4000IrCurrent:
    def __init__(self, number: int, current: int):
        self._number = number
        self._current = current

    def get_number(self) -> int:
        return self._number

    def get_current(self) -> int:
        return self._current

    @staticmethod
    def get(index: int):
        for value in Vcnl4000IrCurrentEnum.values():
            if value.get_number() == index:
                return value
        return Vcnl4000IrCurrentEnum.CURRENT_20MA

    @staticmethod
    def get_default():
        """ "get VCNL 4000 default IR LED current. This current is set on sensor reset." """
        return Vcnl4000IrCurrentEnum.CURRENT_20MA

    def __str__(self):
        return f"{self._current}ma"


class Vcnl4000IrCurrentEnum:
    CURRENT_0MA = Vcnl4000IrCurrent(0, 0)
    CURRENT_10MA = Vcnl4000IrCurrent(1, 10)
    CURRENT_20MA = Vcnl4000IrCurrent(2, 20)
    CURRENT_30MA = Vcnl4000IrCurrent(3, 30)
    CURRENT_40MA = Vcnl4000IrCurrent(4, 40)
    CURRENT_50MA = Vcnl4000IrCurrent(5, 50)
    CURRENT_60MA = Vcnl4000IrCurrent(6, 60)
    CURRENT_70MA = Vcnl4000IrCurrent(7, 70)
    CURRENT_80MA = Vcnl4000IrCurrent(8, 80)
    CURRENT_90MA = Vcnl4000IrCurrent(9, 90)
    CURRENT_100MA = Vcnl4000IrCurrent(10, 100)
    CURRENT_110MA = Vcnl4000IrCurrent(11, 110)
    CURRENT_120MA = Vcnl4000IrCurrent(12, 120)
    CURRENT_130MA = Vcnl4000IrCurrent(13, 130)
    CURRENT_140MA = Vcnl4000IrCurrent(14, 140)
    CURRENT_150MA = Vcnl4000IrCurrent(15, 150)
    CURRENT_160MA = Vcnl4000IrCurrent(16, 160)
    CURRENT_170MA = Vcnl4000IrCurrent(17, 170)
    CURRENT_180MA = Vcnl4000IrCurrent(18, 180)
    CURRENT_190MA = Vcnl4000IrCurrent(19, 190)
    CURRENT_200MA = Vcnl4000IrCurrent(20, 200)

    @staticmethod
    def values() -> list[Vcnl4000IrCurrent]:
        return [f for f in dir(Vcnl4000IrCurrentEnum) if isinstance(f, Vcnl4000IrCurrent)]
