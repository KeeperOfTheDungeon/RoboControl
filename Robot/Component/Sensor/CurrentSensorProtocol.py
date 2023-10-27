from RoboControl.Com.RemoteParameter import RemoteParameterUint16, RemoteParameterUint32, RemoteParameterUint8
from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream

INDEX_SENSOR = 0


class Cmd_getActualCurrentDrain(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "Cmd_getActualCurrentDrain", " get the actual current drain measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id: int, local_id: int):
        cmd = Cmd_getActualCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
    

class Cmd_getMaximalCurrentDrain(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "Cmd_getMaximalCurrentDrain", " get the higest current drain ever measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_getMaximalCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
    
class Cmd_getTotalCurrentDrain(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "Cmd_getTotalCurrentDrain", " get the total current drain ever measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_getTotalCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
    

class Cmd_resetMaximalCurrentDrain(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "resetMaximalCurrentDrain",
                         "reset the highest current drain ever measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_resetMaximalCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
    
class Cmd_resetTotalCurrentDrain(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "Cmd_resetMaximalCurrentDrain", " reset the total current drain measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SENSOR].set_value(index)

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_resetTotalCurrentDrain(id)
        cmd.set_index(local_id)
        return cmd
    
    
class Cmd_setCurrentSettings(RemoteCommand):
	
	INDEX_WINDOW_SIZE	= 1
	INDEX_THRESHOLD 	= 2

	def __init__(self, id):
		super().__init__(id,"Cmd_setCurrentSettings","set settings for a Current Sensor")
		self._parameter_list.append(RemoteParameterUint8("index","sensor index"))
		self._parameter_list.append(RemoteParameterUint8("window size","current sensor data window size"))
		self._parameter_list.append(RemoteParameterUint16("threshold","current sensor threshold"))


	def set_index(self, index):
		self._parameter_list[INDEX_SENSOR].set_value(index)

	def set_window_size(self, window_size):
		self._parameter_list[Cmd_setCurrentSettings.INDEX_WINDOW_SIZE].set_value(window_size)

	def set_threshold(self, threshold):
		self._parameter_list[Cmd_setCurrentSettings.INDEX_THRESHOLD].set_value(threshold)


	def get_command(id, local_id, window_size, threshold):
		cmd = Cmd_setCurrentSettings(id)
		cmd.set_window_size(window_size)
		cmd.set_threshold(threshold)
		cmd.set_index(local_id)

		return (cmd)
     
     
class Msg_currentSettings(RemoteMessage):
    
    INDEX_WINDOW_SIZE = 1
    INDEX_THRESHOLD = 2

    def __init__(self, id):
        super().__init__(id,  "maximal current drain measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterUint8("window size", "current sensor data window size"))
        self._parameter_list.append(RemoteParameterUint16("threshold", "current sensor threshold"))

    @staticmethod
    def get_command(id):
        cmd = Msg_currentSettings(id)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_window_size(self) :
        return self._parameter_list[Msg_currentSettings.INDEX_WINDOW_SIZE].get_value()

    def get_threshold(self):
        return self._parameter_list[Msg_currentSettings.INDEX_THRESHOLD].get_value()
    


class Msg_maxCurrentDrain(RemoteMessage):

    SENSOR_CURRENT = 1

    def __init__(self, id):
        super().__init__(id,  "maximal current drain measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "current sensor index"))
        self._parameter_list.append(RemoteParameterUint16("drain", "maximal current drain measured by this sensor"))

    @staticmethod
    def get_command(id: int):
        cmd = Msg_maxCurrentDrain(id)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_max_current(self):
        return self._parameter_list[Msg_maxCurrentDrain.SENSOR_CURRENT].get_value()
    

class Msg_measuredCurrent(RemoteMessage):

    INDEX_DRAIN = 1

    def __init__(self, id):
        super().__init__(id, "measured current drain by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "current sensor index"))
        self._parameter_list.append(RemoteParameterUint16("drain", "measured current drain by this sensor"))

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            max_drain: int = None,
    ):
        cmd = Msg_measuredCurrent(id)
        if None not in [index, max_drain]:
            cmd.set_data(index, max_drain)
        return cmd

    def get_index(self):
        """ "get sensor index for sensor corresponding to this message" """
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_current(self):
        return self._parameter_list[Msg_measuredCurrent.INDEX_DRAIN].get_value()

    def get_drain(self):
        return self._parameter_list[Msg_measuredCurrent.INDEX_DRAIN].get_value()

    def set_data(self, index, max_drain):
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[Msg_measuredCurrent.INDEX_DRAIN].set_value(max_drain)



class Msg_totalCurrentDrain(RemoteMessage):
    
    SENSOR_CURRENT = 1

    def __init__(self, id):
        super().__init__(id, "total current amount measured by this sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "current sensor index"))
        self._parameter_list.append(RemoteParameterUint32("drain", "total current amount measured by this sensor"))

    @staticmethod
    def get_command(id: int):
        cmd = Msg_totalCurrentDrain(id)
        return cmd

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_total(self):
        return self._parameter_list[Msg_totalCurrentDrain.SENSOR_CURRENT].get_value()
    


class Stream_actualConsumption(RemoteStream):
    _parameter_list: list[RemoteParameterUint16]

    def __init__(self, id):
        super().__init__(
            id,
            "measured current values from device size, size/count is device dependent"
        )

    @staticmethod
    def get_command(id: int, values):
        cmd = Stream_actualConsumption(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def set_data(self, values):
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def get_actual_consumption(self, index):
        value = 0
        if index < len(self._parameter_list):
            value = self._parameter_list[index].get_value()
        return value

    def get_value(self, index):
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_value()

    def get_values_count(self):
        return len(self._parameter_list)

    def make_parameter(self, index: int):
        return RemoteParameterUint16(f"current {index}", f"measured current for sensor {index}")

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)



class Stream_maxConsumption(RemoteStream):
    
    def __init__(self, id):
        super().__init__(
            id,
            "measured max current values from device size, size/count is device dependent"
        )

    @staticmethod
    def get_command(id: int, values):
        cmd = Stream_maxConsumption(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def set_data(self, values) :
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def get_value(self, index):
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_value()

    def get_values_count(self):
        return len(self._parameter_list)

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)

    def get_max_consumption(self, index):
        value = 0
        if index < len(self._parameter_list):
            value = self._parameter_list[index].get_value()
        return value

    def make_parameter(self, index: int):
        return RemoteParameterUint32(f"current {index}", f"measured current for sensor {index}")


class Stream_totalConsumption(RemoteStream):
    
    def __init__(self, id):
        super().__init__(
            id,
            "measured total current values from device size, size/count is device dependent"
        )

    @staticmethod
    def get_command(id: int, values):
        cmd = Stream_totalConsumption(id)
        if values is not None:
            cmd.set_data(values)
        return cmd

    def set_data(self, values):
        for index, value in enumerate(values):
            parameter = self.make_parameter(index)
            parameter.set_value(value)
            self._parameter_list.append(parameter)

    def get_value(self, index: int):
        if index >= self.get_parameter_count():
            return 0
        return self._parameter_list[index].get_value()

    def get_values_count(self):
        return len(self._parameter_list)

    def parse_data_packet_data(self, data_packet):
        return self.parse_data_packet_data_dynamic(data_packet)

    def get_total_consumption(self, index):
        value = 0
        if index < len(self._parameter_list):
            value = self._parameter_list[index].get_value()
        return value

    def make_parameter(self, index: int):
        return RemoteParameterUint32(f"current {index}", f"measured current for sensor {index}")
