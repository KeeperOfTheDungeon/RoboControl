from typing import List

from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.AbstractRobot.AbstractRobotDevice import AbstractRobotDevice
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

from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor


# from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
# from RoboControl.Com.Remote.RemoteMessage import RemoteMessage


class RobotDevice(AbstractRobotDevice):

    def __init__(self, component_config):
        super().__init__(component_config)
        self._aquisators: List[DataAquisator] = DeviceAquisators.get_data_aquisators()
        self._event_listener = []
        self._set_list = []
        self.build()

    # self.build_protocol()

    def get_data_aquisators(self):
        return self._aquisators

    def build_protocol(self):
        super().build_protocol()
        """
        this.commandList.add(new RemoteCommandProcessor(new Cmd_startStreamData(DeviceProtocol.CMD_START_STREAM_DATA),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_stopStreamData(DeviceProtocol.CMD_STOP_STREAM_DATA),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_clearAllDataStreams(DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_pauseAllDataStreams(DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS),device));	
        this.commandList.add(new RemoteCommandProcessor(new Cmd_continueAllDataStreams(DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_saveDataStreams(DeviceProtocol.CMD_SAVE_STREAMS),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_loadDataStreams(DeviceProtocol.CMD_LOAD_STREAMS),device));
        """

    # remote commands

    def remote_ping_device(self):
        cmd = Cmd_ping.get_command(DeviceProtocol.CMD_PING)
        self.send_data(cmd)

    def remote_continue_streams(self):
        cmd = Cmd_continueAllDataStreams.get_command()
        self.send_data(cmd)

    def remote_pause_streams(self):
        cmd = Cmd_pauseAllDataStreams.get_command()
        self.send_data(cmd)

    def remote_clear_streams(self):
        cmd = Cmd_clearAllDataStreams.get_command()
        self.send_data(cmd)

    def remote_save_streams(self):
        cmd = Cmd_saveDataStreams.get_command(DeviceProtocol.CMD_SAVE_STREAMS)
        self.send_data(cmd)

    def remote_load_streams(self):
        cmd = Cmd_loadDataStreams.get_command()
        self.send_data(cmd)

    def remote_start_stream(self, index, period):
        cmd = Cmd_startStreamData.get_command(
            DeviceProtocol.CMD_START_STREAM_DATA,
            new_type=index, period=period
        )
        self.send_data(cmd)

    def remote_stop_stream(self, index):
        cmd = Cmd_stopStreamData.get_command(index)
        self.send_data(cmd)

    def remote_clear_cpu_statistics(self):
        cmd = Cmd_clearCpuStatistics.get_command()
        self.send_data(cmd)

    def remote_clear_com_statistics(self):
        cmd = Cmd_clearComStatistics.get_command()
        self.send_data(cmd)

    def decode_stream(self, remote_stream_data: RemoteStream) -> bool:
        if isinstance(remote_stream_data, Stream_cpuStatistics):
            self._cpu_status.process_cpu_status_message(remote_stream_data)
            return True
        elif isinstance(remote_stream_data, Stream_comStatistics):
            self._com_status.process_com_status_message(remote_stream_data)
            return True
        return False

    def add_event_listener(self, listener) -> None:
        self._event_listener.append(listener)

    def remove_event_listener(self, listener) -> None:
        self._event_listener.remove(listener)

    def add_component_set(self, component_set: List) -> None:
        self._set_list.append(component_set)
        for component in component_set:
            self._component_list.append(component)

    def get_aquisators(self):
        return self._aquisators

    def remote_getNextError(self) -> bool:
        cmd = Cmd_getNextError.get_command()
        return self.send_data(cmd)

    def remote_getErrorCount(self) -> bool:
        cmd = Cmd_getErrorCount.get_command()
        return self.send_data(cmd)

    def decode_message(self, remote_message: RemoteMessage) -> bool:
        if isinstance(remote_message, Msg_pingResponse):
            self.process_ping_response(remote_message)
            return True
        return False
