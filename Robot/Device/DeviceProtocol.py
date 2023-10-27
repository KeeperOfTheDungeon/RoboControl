from RoboControl.Com.RemoteParameter import RemoteParameterUint8, RemoteParameterUint32
from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream




class DeviceProtocol:

    CMD_PING = 0x03

    CMD_GET_NODE_ID = 0x05

    CMD_GET_COM_STATISTICS = 0x06
    CMD_CLEAR_COM_STATISTICS = 0x07

    CMD_GET_CPU_STATISTICS = 0x08
    CMD_CLEAR_CPU_STATISTICS = 0x09

    CMD_GET_NEXT_ERROR = 0x0A
    CMD_GET_ERROR_COUNT = 0x0B

    CMD_START_STREAM_DATA = 0x10
    CMD_STOP_STREAM_DATA = 0x11
    CMD_CLEAR_ALL_DATA_STREAMS = 0x12
    CMD_PAUSE_ALL_DATA_STREAMS = 0x13
    CMD_CONTINUE_ALL_DATA_STREAMS = 0x14
    CMD_SAVE_STREAMS = 0x15
    CMD_LOAD_STREAMS = 0x16

    MSG_PING_RESPONSE = 0x01

    MSG_COM_STATUS = 0x03
    MSG_CPU_STATUS = 0x04

    STREAM_COM_STATISTICS = 0x03
    STREAM_CPU_STATISTICS = 0x04

    def __init__(self, device):
        super().__init__()
        self._device_id = device.get_id()
        self._device = device

        self._message_list = []
        self._stream_list = []



class Cmd_ping(RemoteCommand):

    INDEX_TTL = 0

    def __init__(self, id: int):
        super().__init__(id, "ping", " send ping")
        self._parameter_list.append(RemoteParameterUint8("ttl", "time to live"))

    def set_ttl(self, ttl):
        self._parameter_list[Cmd_ping.INDEX_TTL].set_value(ttl)

    @staticmethod
    def get_command(id: int = DeviceProtocol.CMD_PING):
        cmd = Cmd_ping(id)
        cmd.set_ttl(10)
        return cmd



class Cmd_getNodeId(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "getNodeId", "get destinations node id")

    @staticmethod
    def get_command(id: int):
        cmd = Cmd_getNodeId(id)
        cmd.set_id(DeviceProtocol.CMD_GET_NODE_ID)
        return cmd
    


class Cmd_setDeviceState(RemoteCommand):
    _parameter_list = list()
    # FIXME false java file?

    INDEX_TYPE = 0

    def __init__(self, id: int):
        super().__init__(id, "setDeviceState", "set device state")
        self._parameter_list.append(RemoteParameterUint8("type", "type of data (device dependent)"))

    @staticmethod
    def get_command(id: int, index: int = None):
        cmd = Cmd_setDeviceState(id)
        if index:
            cmd.set_data(index)
        return cmd

    def set_data(self, index: int) -> None:
        self._parameter_list[Cmd_setDeviceState.INDEX_TYPE].set_value(index)

    def get_type(self) -> int:
        return self._parameter_list[Cmd_setDeviceState.INDEX_TYPE].get_value()
    

class Cmd_clearComStatistics(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_CLEAR_COM_STATISTICS):
        super().__init__(id, "clearComStatistics", "clear device comunication statistic")

    @staticmethod
    def get_command():
        return Cmd_clearComStatistics()
    

class Cmd_clearCpuStatistics(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_CLEAR_CPU_STATISTICS):
        super().__init__(id, "clearCpuStatistics", "clear device cpu statistic")

    @staticmethod
    def get_command():
        return Cmd_clearCpuStatistics()
    


class Cmd_clearAllDataStreams(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS):
        super().__init__(id, "clearAllStreams", "clear all data streams on device")

    @staticmethod
    def get_command():
        return Cmd_clearAllDataStreams()
    

class Cmd_continueAllDataStreams(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS):
        super().__init__(id, "continueAllStreams", "continue all active streams on device")

    @staticmethod
    def get_command():
        return Cmd_continueAllDataStreams()
    

class Cmd_loadDataStreams(RemoteCommand):
    def __init__(self, id: int = DeviceProtocol.CMD_LOAD_STREAMS):
        super().__init__(id, "loadDataStreams", "load saved device data Streams from nonvolatile memory")

    @staticmethod
    def get_command():
        return Cmd_loadDataStreams()
    

class Cmd_saveDataStreams(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_SAVE_STREAMS):
        super().__init__(id, "saveDataStreams", "save device actuals data Streams to non volatile memory")

    @staticmethod
    def get_command(id: int = DeviceProtocol.CMD_SAVE_STREAMS):
        return Cmd_saveDataStreams(id)
    

class Cmd_startStreamData(RemoteCommand):
    _parameter_list = list()

    def __init__(self, id: int = DeviceProtocol.CMD_START_STREAM_DATA):
        super().__init__(id, "startStreamData", "start streaming data")
        self._type_index = 0
        self._period_index = 1
        self._parameter_list.append(RemoteParameterUint8("type", "type of data (device dependent)"))
        self._parameter_list.append(RemoteParameterUint8("period", "period of in 10 ms steps"))

    def set_type(self, new_type):
        self._parameter_list[self._type_index].set_value(new_type)

    def set_period(self, new_period):
        self._parameter_list[self._period_index].set_value(new_period)

    def get_type(self) -> int:
        return self._parameter_list[self._type_index].get_value()

    def get_period(self) -> int:
        return self._parameter_list[self._period_index].get_value()

    @staticmethod
    def get_command(id: int, new_type: int = None, period: int = None):
        cmd = Cmd_startStreamData(id)
        if new_type:
            cmd.set_type(new_type)
        if period:
            cmd.set_period(period)
        return cmd
    


class Cmd_stopStreamData(RemoteCommand):

    def __init__(self):
        super().__init__(DeviceProtocol.CMD_STOP_STREAM_DATA, "stopStreamData", "stop streaming data")
        self._type_index = 0
        self._parameter_list.append(RemoteParameterUint8("index", "stream index"))

    def set_type(self, new_type):
        self._parameter_list[self._type_index].set_value(new_type)

    @staticmethod
    def get_command(new_type):
        cmd = Cmd_stopStreamData()
        cmd.set_type(new_type)
        return cmd
    

class Cmd_pauseAllDataStreams(RemoteCommand):
    def __init__(self, id: int = DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS):
        super().__init__(id, "pauseAllStreams", "pause all active streams on device")

    @staticmethod
    def get_command():
        return Cmd_pauseAllDataStreams()
    


class Cmd_getErrorCount(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_GET_ERROR_COUNT):
        super().__init__(id, "getErrorCounts", "get count of errors on device")

    @staticmethod
    def get_command():
        cmd = Cmd_getErrorCount()
        cmd.set_id(DeviceProtocol.CMD_GET_ERROR_COUNT)
        return cmd

class Cmd_getNextError(RemoteCommand):

    def __init__(self, id: int = DeviceProtocol.CMD_GET_NEXT_ERROR):
        super().__init__(id, "getNextError", "get next error from error queue")

    @staticmethod
    def get_command():
        return Cmd_getNextError()
    

class Msg_pingResponse(RemoteMessage):

    INDEX_TTL = 0

    _parameter_list = list()

    def __init__(self, id: int = DeviceProtocol.MSG_PING_RESPONSE):
        super().__init__(id, "pingResponse", "response to a ping command")
        self._parameter_list.append(RemoteParameterUint8("ttl", "time to live"))

    @staticmethod
    def get_command(id: int, ttl: int = None) -> "Msg_pingResponse":
        res = Msg_pingResponse(id)
        if ttl is not None:
            res.set_data(ttl)
        return res

    def get_ttl(self):
        return self._parameter_list[Msg_pingResponse.INDEX_TTL].get_value()

    def set_data(self, node_type: int) -> None:
        self._parameter_list[Msg_pingResponse.INDEX_TTL].set_value(node_type)



class Msg_nodeType(RemoteMessage):

    NODE_TYPE = 0

    _parameter_list = list()

    def __init__(self, id: int = DeviceProtocol.MSG_PING_RESPONSE):
        super().__init__(id, "nodeType", "type of a node")
        self._parameter_list.append(RemoteParameterUint8("type", "type of a node"))

    @staticmethod
    def get_command(id: int, node_type: int = None) -> "Msg_nodeType":
        res = Msg_nodeType(id)
        if node_type is not None:
            res.set_data(node_type)
        return res

    def get_node_type(self):
        return self._parameter_list[Msg_nodeType.NODE_TYPE].get_value()

    def set_data(self, node_type: int) -> None:
        self._parameter_list[Msg_nodeType.NODE_TYPE].set_value(node_type)


class Stream_comStatistics(RemoteStream):
    _parameter_list = list()

    INDEX_TRANSMITTED_MESSAGES = 0
    INDEX_RECEIVED_MESSAGES = 1
    INDEX_INVALID_MESSAGES = 2
    INDEX_LOST_MESSAGES = 3
    INDEX_LOST_UNDELIVERABLE = 4
    INDEX_COM_STATUS = 5


    def __init__(self, id):
        super().__init__(id, "comStatus", "status of the com system")

        self._parameter_list.append(RemoteParameterUint32("transmitted", "number of transmitted messages"))
        self._parameter_list.append(RemoteParameterUint32("received", "number of recived messages thrue this device"))
        self._parameter_list.append(
            RemoteParameterUint32("invalid", "number of invalid messages received thrue this device"))
        self._parameter_list.append(RemoteParameterUint32("lost", "number of lost mesages"))
        self._parameter_list.append(RemoteParameterUint32("undeliverable", "number of undeliverable mesages"))
        self._parameter_list.append(RemoteParameterUint8("status", "actual status of the device com system"))

    def get_transmitted_messages_count(self):
        return self._parameter_list[Stream_comStatistics.INDEX_TRANSMITTED_MESSAGES].get_value()

    def get_received_messages_count(self):
        return self._parameter_list[Stream_comStatistics.INDEX_RECEIVED_MESSAGES].get_value()

    def get_invalid_messages_count(self):
        return self._parameter_list[Stream_comStatistics.INDEX_INVALID_MESSAGES].get_value()

    def get_lost_messages_count(self):
        return self._parameter_list[Stream_comStatistics.INDEX_LOST_MESSAGES].get_value()

    def set_data(
            self, transmitted: int, received: int, invalid: int, lost: int, status: int, undeliverable: int
    ) -> None:
        self._parameter_list[Stream_comStatistics.INDEX_TRANSMITTED_MESSAGES].set_value(transmitted)
        self._parameter_list[Stream_comStatistics.INDEX_RECEIVED_MESSAGES].set_value(received)
        self._parameter_list[Stream_comStatistics.INDEX_INVALID_MESSAGES].set_value(invalid)
        self._parameter_list[Stream_comStatistics.INDEX_LOST_MESSAGES].set_value(lost)
        self._parameter_list[Stream_comStatistics.INDEX_LOST_UNDELIVERABLE].set_value(undeliverable)
        self._parameter_list[Stream_comStatistics.INDEX_COM_STATUS].set_value(status)

    @staticmethod
    def get_command(
            id: int,
            transmitted: int = None, received: int = None, invalid: int = None, lost: int = None, status: int = None, undeliverable: int = None
    ):
        cmd = Stream_comStatistics(id)
        if transmitted and received and invalid and lost and status and undeliverable:
            cmd.set_data(transmitted, received, invalid, lost, status, undeliverable)
        return cmd
    

class Stream_cpuStatistics(RemoteStream):
   
    INDEX_MIN_CPU_LOAD = 0
    INDEX_ACTUAL_CPU_LOAD = 1
    INDEX_MAX_CPU_LOAD = 2
    INDEX_CPU_STATUS = 3

    _parameter_list = list()

    def __init__(self, id: int):
        super().__init__(id, "cpuStatus", "status of the cpu containing values for min max and last cycle duration")

        self._parameter_list.append(RemoteParameterUint8("min", "min load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("max", "max load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("actual", "actual load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("status", "actual status of the device cpu"))

        self.set_id(id)

    def get_last_load(self):
        return self._parameter_list[Stream_cpuStatistics.INDEX_ACTUAL_CPU_LOAD].get_value()

    def get_min_load(self):
        return self._parameter_list[Stream_cpuStatistics.INDEX_MIN_CPU_LOAD].get_value()

    def get_max_load(self):
        return self._parameter_list[Stream_cpuStatistics.INDEX_MAX_CPU_LOAD].get_value()

    def set_data(self, min_load: int, max_load: int, current_load: int, status: int) -> None:
        self._parameter_list[Stream_cpuStatistics.INDEX_MIN_CPU_LOAD].set_value(min_load)
        self._parameter_list[Stream_cpuStatistics.INDEX_MAX_CPU_LOAD].set_value(max_load)
        self._parameter_list[Stream_cpuStatistics.INDEX_ACTUAL_CPU_LOAD].set_value(current_load)
        self._parameter_list[Stream_cpuStatistics.INDEX_CPU_STATUS].set_value(status)

    @staticmethod
    def get_command(
            id: int,
            min_load: int = None, max_load: int = None, current_load: int = None, status: int = None
    ):
        cmd = Stream_cpuStatistics(id)
        if min_load and max_load and current_load and status:
            cmd.set_data(min_load, max_load, current_load, status)
        return