# import copy
from typing import Optional

from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput
from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent
from RoboControl.Robot.AbstractRobot.AbstractListener import DataPacketReceiver, CpuStatusListener, ComStatusListener
from RoboControl.Robot.AbstractRobot.Config.DeviceConfig import DeviceConfig
from RoboControl.Robot.AbstractRobot.RemotePacketHandler import RemotePacketHandler
from RoboControl.Robot.AbstractRobot.Config.ComponentConfig import ComponentConfig
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Component.statistic.ComStatus import ComStatus
from RoboControl.Robot.Component.statistic.CpuStatus import CpuStatus
from RoboControl.Robot.Device.remoteProcessor.RemoteDecoder import RemoteDecoder
from RoboControl.Robot.Value.ComponentValue import ComponentValue


class AbstractRobotDevice(
    AbstractComponent, DataPacketReceiver, RemoteDecoder, RemotePacketHandler
):
    _name = "AbstractRobotDevice"
    _type_name = "?"
    _transmitter: RemoteDataOutput  # RemoteDataTransmitter

    def __init__(self, component_config: DeviceConfig):
        AbstractComponent.__init__(self, {
            "name": component_config.get_name(),
            "global_id": component_config.get_id()  # FIXME is this right?
        })
        RemotePacketHandler.__init__(self)
        self._id: int = component_config.get_id()

        self._component_list: list[RobotComponent] = []
        self._component_set_list: list[ComponentSet] = []

        self._com_status = ComStatus()
        self._cpu_status = CpuStatus()

    def set_transmitter(self, transmitter: RemoteDataOutput) -> None:
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

    def get_component(self, index: int) -> Optional[RobotComponent]:
        if index >= self.get_component_count():
            return None
        return self._component_list[index]

    def find_component_on_name(self, name: str) -> Optional[RobotComponent]:
        for component in self._component_list:
            if component.get_component_name() == name:
                return component
        return None

    def find_component_on_global_id(self, global_id: int) -> Optional[RobotComponent]:
        for component in self._component_list:
            if component.get_global_id() == global_id:
                return component
        return None

    def add_cpu_status_listener(self, listener: CpuStatusListener) -> None:
        self._cpu_status.add_status_listener(listener)

    def remove_cpu_status_listener(self, listener: CpuStatusListener) -> None:
        self._cpu_status.remove_status_listener(listener)

    def get_cpu_status(self) -> CpuStatus:
        return self._cpu_status

    def add_com_status_listener(self, listener: ComStatusListener) -> None:
        self._com_status.add_status_listener(listener)

    def remove_com_status_listener(self, listener: ComStatusListener) -> None:
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
