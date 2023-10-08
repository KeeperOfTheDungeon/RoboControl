# import copy

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteException import RemoteException
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Component.statistic.ComStatus import ComStatus
from RoboControl.Robot.Component.statistic.CpuStatus import CpuStatus
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessorList import RemoteProcessorList

from RoboControl.Robot.Device.Protocol import DeviceProtocol

from RoboControl.Robot.Device.Protocol.Stream_comStatistics import Stream_comStatistics
from RoboControl.Robot.Device.Protocol.Stream_cpuStatistics import Stream_cpuStatistics
from RoboControl.Robot.Device.Protocol.Cmd_ping import Cmd_ping
from RoboControl.Robot.Device.Protocol.Cmd_getNodeId import Cmd_getNodeId
from RoboControl.Robot.Device.Protocol.Msg_pingResponse import Msg_pingResponse


class AbstractRobotDevice:
    _name = "AbstractRobotDevice"
    _transmitter: RemoteDataOutput

    def __init__(self, component_config):
        self._name = component_config.get_name()
        self._id = component_config.get_id()

        self._remote_command_processor_list = RemoteProcessorList()
        self._remote_message_processor_list = RemoteProcessorList()
        self._remote_stream_processor_list = RemoteProcessorList()
        self._remote_exception_processor_list = RemoteProcessorList()

        self._component_list = list()
        self._cpu_status_listener = list()
        self._com_status_listener = list()

        self._com_status = ComStatus()
        self._cpu_status = CpuStatus()

    def build_protocol(self):
        stream = Stream_comStatistics(DeviceProtocol.STREAM_COM_STATISTICS)
        handler = self._com_status.process_com_status_message
        processor = RemoteProcessor(stream, handler)
        self._remote_stream_processor_list.append(processor)

        stream = Stream_cpuStatistics(DeviceProtocol.STREAM_CPU_STATISTICS)
        handler = self._cpu_status.process_cpu_status_message
        processor = RemoteProcessor(stream, handler)
        self._remote_stream_processor_list.append(processor)

        command = Cmd_ping(DeviceProtocol.CMD_PING)
        handler = self.process_ping_command
        processor = RemoteProcessor(command, handler)
        self._remote_command_processor_list.append(processor)

        command = Cmd_getNodeId(DeviceProtocol.CMD_GET_NODE_ID)
        handler = self.process_node_id_command
        processor = RemoteProcessor(command, handler)
        self._remote_command_processor_list.append(processor)

        message = Msg_pingResponse(DeviceProtocol.MSG_PING_RESPONSE)
        handler = self.process_ping_response
        processor = RemoteProcessor(message, handler)
        self._remote_message_processor_list.append(processor)

    def set_transmitter(self, transmitter):
        self._transmitter = transmitter
        for component in self._component_list:
            component.set_transmitter(transmitter)

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id

    def has_id(self, query_id):
        if self._id == query_id:
            return True
        return False

    def add_components(self, components):
        for component in components:
            self._component_list.append(component)

    def get_component(self, index: int) -> RobotComponent:
        return self._component_list[index]

    def find_component_on_name(self, name):
        pass

    def find_copmonent_on_global_is(self, query_id):
        pass

    def get_component_count(self):
        return len(self._component_list)

    def add_cpu_status_listener(self, listener):
        self._cpu_status_listener.append(listener)
        self._cpu_status.add_status_listener(listener)

    def remove_cpu_status_listener(self, listener):
        self._cpu_status_listener.remove(listener)
        self._cpu_status.remove_status_listener(listener)

    def add_com_status_listener(self, listener):
        self._com_status.add_status_listener(listener)

    def remove_com_status_listener(self, listener):
        self._com_status.remove_status_listener(listener)

    def receive(self, data_packet: RemoteData):
        self.parse_data_packet(data_packet)

    def send_data(self, data_packet: RemoteData) -> bool:
        # print("ARD: send Data", data_packet)
        data_packet.set_destination_address(self.get_id())
        if self._transmitter is None:
            return False
        return self._transmitter.transmitt(data_packet)

    def load_setup(self) -> None:
        for component in self._component_list:
            component.remote_loadDefaults()
            component.remote_getSettings()

    def on_connected(self):
        """ "called when connection to remote robot succeeded" """
        # self.load_setup()
        for component in self._component_list:
            component.on_connected()

    def on_disconnected(self):
        """ "called when disconnecting grom remote robot" """
        # self.load_setup()
        for component in self._component_list:
            component.on_disconnected()

    def get_device_name(self) -> str:
        return self._name

    def parse_data_packet(self, data_packet):

        query_id = data_packet.get_id()
        processor = None
        # print ("ARD : ParseDataPAcket", query_id, data_packet)

        if isinstance(data_packet, RemoteCommand):
            processor = self._remote_command_processor_list.find_on_id(query_id)
            # print ("ARD : Command Prozessor", processor)

        elif isinstance(data_packet, RemoteMessage):
            processor = self._remote_message_processor_list.find_on_id(query_id)

        elif isinstance(data_packet, RemoteStream):
            processor = self._remote_stream_processor_list.find_on_id(query_id)

        elif isinstance(data_packet, RemoteException):
            processor = self._remote_exception_processor_list.find_on_id(query_id)

        if processor is not None:
            remote_data = processor.get_remote_data()
            # remote_stream = copy.copy(remote_data)
            # remote_stream.parse_payload(data_packet.get_payload())
            remote_data.parse_payload(data_packet.get_payload())
            processor.execute(remote_data)

    # device remote functions

    def remote_ping_device(self):
        cmd = Cmd_ping.get_command(DeviceProtocol.CMD_PING)
        self.send_data(cmd)

    # Remote Prozessors

    # noinspection PyMethodMayBeStatic
    def process_ping_response(self, message_data):
        print("******************got ping response************************")

    # noinspection PyMethodMayBeStatic
    def process_ping_command(self, command_data):
        msg = Msg_pingResponse.get_command(DeviceProtocol.MSG_PING_RESPONSE)
        self.send_data(msg)
        print("******************got ping command************************")

    # noinspection PyMethodMayBeStatic
    def process_node_id_command(self, command_data):
        print("******************got node Id command************************")
