from RoboControl.Com.RemoteData import RemoteData, RemoteMessage, RemoteStream
from RoboControl.Com.Connection import RemoteDataOutput

from RoboControl.Robot.AbstractRobot.AbstractRobotDevice import AbstractRobotDevice
from RoboControl.Robot.AbstractRobot.ComponentConfig import ComponentConfig
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Device.DeviceProtocol import DeviceProtocol, Msg_nodeType
from RoboControl.Robot.Device.DeviceProtocol import Cmd_clearAllDataStreams, Cmd_clearComStatistics, \
    Cmd_clearCpuStatistics, Cmd_continueAllDataStreams
from RoboControl.Robot.Device.DeviceProtocol import Cmd_getErrorCount, Cmd_getNextError, Cmd_getNodeId, \
    Cmd_loadDataStreams, Cmd_pauseAllDataStreams
from RoboControl.Robot.Device.DeviceProtocol import Cmd_ping, Cmd_saveDataStreams, Cmd_startStreamData
from RoboControl.Robot.Device.DeviceProtocol import Cmd_stopStreamData, Msg_pingResponse, Stream_comStatistics, \
    Stream_cpuStatistics

from RoboControl.Robot.Device.control.DataAquisator import DataAquisator
from RoboControl.Robot.Device.control.DeviceAquisators import DeviceAquisators
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor


class RobotDevice(AbstractRobotDevice):

    def __init__(self, device_meta_data):
        super().__init__(device_meta_data)
        self._aquisators = DeviceAquisators.get_data_aquisators()
        self._event_listener = list()
        self.build()

    def build(self):
        self.build_protocol()

    def build_protocol(self):
        super().build_protocol()
        self.add_commands()
        self.add_messages()
        self.add_streams()

    def get_data_aquisators(self):
        return self._aquisators

    def add_event_listener(self, listener):
        self._event_listener.append(listener)

    def remove_event_listener(self, listener):
        self._event_listener.remove(listener)

    def set_transmitter(self, transmitter: RemoteDataOutput):
        super().set_transmitter(transmitter)
        for component_set in self._component_set_list:
            component_set.set_transmitter(transmitter)

    def get_device_name(self) -> str:
        return self.get_name()

    def add_component_set(self, component_set: ComponentSet):
        self._component_set_list.append(component_set)
        for component in component_set:
            self.add_component(component)

    def add_component(self, component: RobotComponent):
        self._component_list.append(component)

    def get_aquisators(self) -> list[DataAquisator]:
        return self._aquisators

    REMOTE_CHANEL_ID: int = 1

    def send_data(self, data: RemoteData) -> bool:

        # if remote send wit remote id
        data.set_source_address(RobotDevice.REMOTE_CHANEL_ID)
        data.set_destination_address(self.get_id())
        if self._transmitter is None:
            return False
        return self._transmitter.transmitt(data)

    def load_setup(self) -> None:
        for component in self._component_list:
            component.remote_load_defaults()
            component.remote_get_settings()

    def on_connected(self) -> None:
        """ "called when connection to remote robot succeeded" """
        self.load_setup()
        for component in self._component_list:
            component.on_connected()

    def on_disconnected(self) -> None:
        """ "called when disconnecting to remote robot succeeded" """
        self.load_setup()
        for component in self._component_list:
            component.on_disconnected()

    def process_ping_command(self, remote_command):
        print("******************got ping command************************")
        msg = Msg_pingResponse.get_command(DeviceProtocol.MSG_PING_RESPONSE)
        self.send_data(msg)

    def process_get_nodeId_command(self, remote_command):
        print("******************got get Node ID command************************")
        msg = Msg_nodeType.get_command(DeviceProtocol.MSG_NODE_TYPE)
        self.send_data(msg)

    # noinspection PyMethodMayBeStatic
    def process_ping_response(self, Msg_pingResponse):
        print("got ping")
        for listener in self._event_listener:
            listener.ping_received(self)

    def remote_start_stream(self, index: int, period: int):
        cmd = Cmd_startStreamData.get_command(
            DeviceProtocol.CMD_START_STREAM_DATA,
            new_type=index, period=period
        )
        return self.send_data(cmd)

    def remote_stop_stream(self, index: int):
        cmd = Cmd_stopStreamData.get_command(index)
        return self.send_data(cmd)

    def remote_clear_streams(self):
        cmd = Cmd_clearAllDataStreams.get_command()
        return self.send_data(cmd)

    def remote_pause_streams(self):
        cmd = Cmd_pauseAllDataStreams.get_command()
        return self.send_data(cmd)

    def remote_continue_streams(self):
        cmd = Cmd_continueAllDataStreams.get_command()
        return self.send_data(cmd)

    def remote_save_streams(self):
        cmd = Cmd_saveDataStreams.get_command()
        return self.send_data(cmd)

    def remote_load_streams(self):
        cmd = Cmd_loadDataStreams.get_command()
        return self.send_data(cmd)

    def remote_ping_device(self):
        cmd = Cmd_ping.get_command()
        return self.send_data(cmd)

    def remote_get_next_error(self):
        cmd = Cmd_getNextError.get_command()
        return self.send_data(cmd)

    def remote_get_error_count(self):
        cmd = Cmd_getErrorCount.get_command()
        return self.send_data(cmd)

    def remote_clear_com_statistics(self):
        cmd = Cmd_clearComStatistics.get_command()
        return self.send_data(cmd)

    def remote_clear_cpu_statistics(self):
        cmd = Cmd_clearCpuStatistics.get_command()
        return self.send_data(cmd)

    def decode_command(self, remote_command):
        if isinstance(remote_command, Cmd_ping):
            self.process_ping_command(remote_command)
            return True
        if isinstance(remote_command, Cmd_getNodeId):
            self.process_get_nodeId_command(remote_command)
            return True

    def decode_message(self, remote_message: RemoteMessage) -> bool:
        if isinstance(remote_message, Msg_pingResponse):
            self.process_ping_response(remote_message)
            return True
        return False

    def decode_stream(self, remote_stream_data):
        if isinstance(remote_stream_data, Stream_cpuStatistics):
            self._cpu_status.process_cpu_status_message(remote_stream_data)
            return True
        elif isinstance(remote_stream_data, Stream_comStatistics):
            self._com_status.process_com_status_message(remote_stream_data)
            return True
        return False

    def add_command_processor(self, command, handler):
        processor = RemoteProcessor(command, handler)
        self._command_processor_list.append(processor)
        return self

    def add_command_processor_list(self, processor_list):
        self._command_processor_list.extend(processor_list)
        return self

    def add_message_processor(self, message, handler):
        processor = RemoteProcessor(message, handler)
        self._message_processor_list.append(processor)
        return self

    def add_message_processor_list(self, processor_list):
        self._message_processor_list.extend(processor_list)
        return self

    def add_stream_processor(self, stream, handler):
        processor = RemoteProcessor(stream, handler)
        self._stream_processor_list.append(processor)
        return self

    def add_stream_processor_list(self, processor_list):
        self._stream_processor_list.extend(processor_list)
        return self

    # noinspection PyMethodMayBeStatic
    def process_node_id_command(self, command_data):
        print("******************got node Id command************************")

    def add_commands(self):
        self.add_command_processor(Cmd_ping(DeviceProtocol.CMD_PING), self)
        self.add_command_processor(Cmd_ping(DeviceProtocol.Cmd_getNodeId), self)
        self.add_stream_control()

    def add_stream_control(self):
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_START_STREAM_DATA), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_STOP_STREAM_DATA), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_SAVE_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_LOAD_STREAMS), self)

    def add_commands(self):
        self.add_command_processor(Cmd_ping(DeviceProtocol.CMD_PING), self)

    def add_messages(self):
        self.add_message_processor(Msg_pingResponse(DeviceProtocol.MSG_PING_RESPONSE), self)
        self.add_message_processor(Cmd_getNodeId(DeviceProtocol.CMD_GET_NODE_ID), self)

    def add_streams(self) -> None:
        self.add_stream_processor(Stream_comStatistics(DeviceProtocol.STREAM_COM_STATISTICS), self)
        self.add_stream_processor(Stream_cpuStatistics(DeviceProtocol.STREAM_CPU_STATISTICS), self)
