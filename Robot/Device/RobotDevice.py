from typing import List

from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput
from RoboControl.Robot.AbstractRobot.AbstractListener import DeviceEventNotifier
from RoboControl.Robot.AbstractRobot.AbstractRobotDevice import AbstractRobotDevice
from RoboControl.Robot.AbstractRobot.Config.ComponentConfig import ComponentConfig
from RoboControl.Robot.AbstractRobot.Config.DeviceConfig import DeviceConfig
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Device.Protocol import DeviceProtocol
from RoboControl.Robot.Device.Protocol.Cmd_clearAllDataStreams import Cmd_clearAllDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_clearComStatistics import Cmd_clearComStatistics
from RoboControl.Robot.Device.Protocol.Cmd_clearCpuStatistics import Cmd_clearCpuStatistics
from RoboControl.Robot.Device.Protocol.Cmd_continueAllDataStreams import Cmd_continueAllDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_getErrorCount import Cmd_getErrorCount
from RoboControl.Robot.Device.Protocol.Cmd_getNextError import Cmd_getNextError
from RoboControl.Robot.Device.Protocol.Cmd_getNodeId import Cmd_getNodeId

from RoboControl.Robot.Device.Protocol.Cmd_loadDataStreams import Cmd_loadDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_pauseAllDataStreams import Cmd_pauseAllDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_ping import Cmd_ping
from RoboControl.Robot.Device.Protocol.Cmd_saveDataStreams import Cmd_saveDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_startStreamData import Cmd_startStreamData
from RoboControl.Robot.Device.Protocol.Cmd_stopStreamData import Cmd_stopStreamData
from RoboControl.Robot.Device.Protocol.Msg_pingResponse import Msg_pingResponse
from RoboControl.Robot.Device.Protocol.Stream_comStatistics import Stream_comStatistics
from RoboControl.Robot.Device.Protocol.Stream_cpuStatistics import Stream_cpuStatistics
from RoboControl.Robot.Device.control.DataAquisator import DataAquisator
from RoboControl.Robot.Device.control.DeviceAquisators import DeviceAquisators


class RobotDevice(
    AbstractRobotDevice,  # ControlInterface
):
    def __init__(self, component_config: DeviceConfig):
        super().__init__(component_config)
        self._aquisators: List[DataAquisator] = DeviceAquisators.get_data_aquisators()
        self._event_listener: List[DeviceEventNotifier] = []
        self.build()

    def build(self):
        self.build_protocol()

    def build_protocol(self):
        self._add_ping_processors()
        self._add_node_id_processors()
        self._add_stream_control()
        self._add_statistics()

    def get_data_aquisators(self):
        return self._aquisators

    def add_event_listener(self, listener: DeviceEventNotifier) -> None:
        self._event_listener.append(listener)

    def remove_event_listener(self, listener: DeviceEventNotifier) -> None:
        self._event_listener.remove(listener)

    def set_transmitter(self, transmitter: RemoteDataOutput) -> None:
        super().set_transmitter(transmitter)
        for component_set in self._component_set_list:
            component_set.set_transmitter(transmitter)

    def get_device_name(self) -> str:
        return self.get_name()

    def add_component_set(self, component_set: ComponentSet) -> None:
        self._component_set_list.append(component_set)
        for component in component_set:
            self.add_component(component)

    def add_component(self, component: RobotComponent) -> None:
        self._component_list.append(component)

    def get_aquisators(self) -> list[DataAquisator]:
        return self._aquisators

    def send_data(self, data: RemoteData) -> bool:
        # print("ARD: send Data", data_packet)
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

    def process_ping_command(self, remote_command: Cmd_ping) -> None:
        # print("******************got ping command************************")
        msg = Msg_pingResponse.get_command(DeviceProtocol.MSG_PING_RESPONSE)
        self.send_data(msg)

    # noinspection PyMethodMayBeStatic
    def process_ping_response(self, remote_message: Msg_pingResponse) -> None:
        for listener in self._event_listener:
            listener.ping_received(self)

    def remote_start_stream(self, index: int, period: int) -> bool:
        cmd = Cmd_startStreamData.get_command(
            DeviceProtocol.CMD_START_STREAM_DATA,
            new_type=index, period=period
        )
        return self.send_data(cmd)

    def remote_stop_stream(self, index: int) -> bool:
        cmd = Cmd_stopStreamData.get_command(index)
        return self.send_data(cmd)

    def remote_clear_streams(self) -> bool:
        cmd = Cmd_clearAllDataStreams.get_command()
        return self.send_data(cmd)

    def remote_pause_streams(self) -> bool:
        cmd = Cmd_pauseAllDataStreams.get_command()
        return self.send_data(cmd)

    def remote_continue_streams(self) -> bool:
        cmd = Cmd_continueAllDataStreams.get_command()
        return self.send_data(cmd)

    def remote_save_streams(self) -> bool:
        cmd = Cmd_saveDataStreams.get_command()
        return self.send_data(cmd)

    def remote_load_streams(self) -> bool:
        cmd = Cmd_loadDataStreams.get_command()
        return self.send_data(cmd)

    def remote_ping_device(self) -> bool:
        cmd = Cmd_ping.get_command()
        return self.send_data(cmd)

    def remote_get_next_error(self) -> bool:
        cmd = Cmd_getNextError.get_command()
        return self.send_data(cmd)

    def remote_get_error_count(self) -> bool:
        cmd = Cmd_getErrorCount.get_command()
        return self.send_data(cmd)

    def remote_clear_com_statistics(self) -> bool:
        cmd = Cmd_clearComStatistics.get_command()
        return self.send_data(cmd)

    def remote_clear_cpu_statistics(self) -> bool:
        cmd = Cmd_clearCpuStatistics.get_command()
        return self.send_data(cmd)

    def decode_stream(self, remote_stream_data: RemoteStream) -> bool:
        if isinstance(remote_stream_data, Stream_cpuStatistics):
            self._cpu_status.process_cpu_status_message(remote_stream_data)
            return True
        elif isinstance(remote_stream_data, Stream_comStatistics):
            self._com_status.process_com_status_message(remote_stream_data)
            return True
        return False

    def decode_message(self, remote_message: RemoteMessage) -> bool:
        if isinstance(remote_message, Msg_pingResponse):
            self.process_ping_response(remote_message)
            return True
        return False

    # noinspection PyMethodMayBeStatic
    def process_node_id_command(self, command_data):
        print("******************got node Id command************************")

    def _add_ping_processors(self) -> None:
        self.add_command_processor(
            Cmd_ping(DeviceProtocol.CMD_PING),
            self,
        )
        self.add_message_processor(
            Msg_pingResponse(DeviceProtocol.MSG_PING_RESPONSE),
            self,
        )

    def _add_node_id_processors(self) -> None:
        self.add_command_processor(
            Cmd_getNodeId(DeviceProtocol.CMD_GET_NODE_ID),
            self,
        )

    def _add_stream_control(self) -> None:
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_START_STREAM_DATA), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_STOP_STREAM_DATA), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_SAVE_STREAMS), self)
        self.add_command_processor(Cmd_startStreamData(DeviceProtocol.CMD_LOAD_STREAMS), self)

    def _add_statistics(self) -> None:
        self.add_stream_processor(Stream_comStatistics(DeviceProtocol.STREAM_COM_STATISTICS), self)
        self.add_stream_processor(Stream_cpuStatistics(DeviceProtocol.STREAM_CPU_STATISTICS), self)
