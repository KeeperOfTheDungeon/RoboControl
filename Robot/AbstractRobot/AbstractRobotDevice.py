# import copy


from RoboControl.Com.RemoteData import RemoteData
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.AbstractRobot import DeviceConfig

from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent, AbstractComponentList


from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Device.DeviceStartus import ComStatus, CpuStatus
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessorList
from RoboControl.Robot.Value.ComponentValue import ComponentValue

from RoboControl.Com.RemoteDataPacket import RemoteCommandDataPacket, RemoteExceptionDataPacket, RemoteMessageDataPacket, RemoteStreamDataPacket

class AbstractRobotDevice():
    _name = "AbstractRobotDevice"
    _type_name = "?"
    _transmitter = None  # RemoteDataTransmitter

    def __init__(self, component_config: DeviceConfig):
        AbstractComponent.__init__(self, {
            "name": component_config.get_name(),
            "global_id": component_config.get_id()  # FIXME is this right?
        })
     
        self._id: int = component_config.get_id()

        self._command_processor_list = RemoteProcessorList()
        self._message_processor_list = RemoteProcessorList()
        self._stream_processor_list = RemoteProcessorList()

        self._component_list = AbstractComponentList()
        self._component_set_list: list[ComponentSet] = []

        self._com_status = ComStatus()
        self._cpu_status = CpuStatus()



    def set_transmitter(self, transmitter):
        self._transmitter = transmitter
        for component in self._component_list:
            if component is not None:
                component.set_transmitter(self._transmitter)

    def get_name(self) -> str:
        return self._name

    def get_id(self) -> int:
        """ "Get id of this device. Id is the address of corresponding device in real robot" """
        return self._id

    def get_component_count(self):
        return len(self._component_list)

    def get_component(self, index):
        if index >= self.get_component_count():
            return None
        return self._component_list[index]

    def find_component_on_name(self, name: str):
        for component in self._component_list:
            if component.get_component_name() == name:
                return component
        return None

    def find_component_on_global_id(self, global_id):
        for component in self._component_list:
            if component.get_global_id() == global_id:
                return component
        return None

    def add_cpu_status_listener(self, listener) -> None:
        self._cpu_status.add_status_listener(listener)

    def remove_cpu_status_listener(self, listener) -> None:
        self._cpu_status.remove_status_listener(listener)

    def get_cpu_status(self) -> CpuStatus:
        return self._cpu_status

    def add_com_status_listener(self, listener) -> None:
        self._com_status.add_status_listener(listener)

    def remove_com_status_listener(self, listener) -> None:
        self._com_status.remove_status_listener(listener)

    def get_com_status(self) -> ComStatus:
        return self._com_status

    def get_data_values(self) -> list[ComponentValue]:
        res = []
        for component in self._component_list:
            res += component.get_data_values()
        return res

    def get_control_values(self) -> list[ComponentValue]:
        res = []
        for component in self._component_list:
            res += component.get_control_values()
        return res

    def get_control_clients(self) -> "list[ControlClient]":
        res = []
        for component in self._component_list:
            res += component.get_control_clients()
        return res

    def on_load_settings(self) -> None:
        for component in self._component_list:
            component.on_load_settings()

    def on_save_settings(self) -> None:
        for component in self._component_list:
            component.on_save_settings()

    def decode(self, remote_data: RemoteData) -> bool:
        return False

    decode_command = decode
    decode_message = decode
    decode_stream = decode
    decode_exception = decode

    def has_id(self, query_id):
        if self._id == query_id:
            return True
        return False

    def receive(self, data_packet: RemoteDataPacket) -> None:
        return self.parse_data_packet(data_packet)



    def _find_processor(self, data_packet, remote_id: int):
        if isinstance(data_packet, RemoteCommandDataPacket):
            # print ("ARD : Command Prozessor", processor)
            return self._command_processor_list.find_on_id(remote_id)
        elif isinstance(data_packet, RemoteMessageDataPacket):
            return self._message_processor_list.find_on_id(remote_id)
        elif isinstance(data_packet, RemoteStreamDataPacket):
            return self._stream_processor_list.find_on_id(remote_id)
        elif isinstance(data_packet, RemoteExceptionDataPacket):
            return self._exception_processor_list.find_on_id(remote_id)
        print("unsuported data packet type")
        return None

    def parse_data_packet(self, data_packet):
        remote_id = data_packet.get_command()
        processor = self._find_processor(data_packet, remote_id)
        if processor is not None:
            remote_data = processor.get_remote_data()
            remote_data.parse_data_packet(data_packet)
            data_packet.set_remote_data(remote_data)
            processor.execute(remote_data)
            return remote_data

        return None
    
    def build_protocol(self):
        pass