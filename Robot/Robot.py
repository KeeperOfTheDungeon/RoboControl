from typing import List

from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboControl.Robot.Device.Generic.DataHub.DataHub import DataHub

# from asyncio.windows_events import NULL
# from RoboView.Robot.Viewer.RobotSettings import RobotSettings


"""
An instance of this class represents a robot. It contains all robot devices
and provides connection for data transfer between this python robot representation and real robot.
    
@author Oktavian Gniot
"""


class Robot(AbstractRobot):

    def __init__(self, name: str):
        super().__init__()
        self._name = name

        self._morphologic_model: "MorphologicModel" = None
        self._appearance_model: "AppearanceModel" = None
        self._field_of_views: List["FieldOfView"] = []
        # self._perception_spheres: Vector[PerceptionSphere] = Vector()

        self._navigator: "Navigator" = None

        # TODO
        # self._destination = Destination()
        # self._navigation_path = NavigationPath()
        self._behavior: "RobotBehavior" = None

    def connect(self, connection: Connection) -> None:
        """ "connect to remote device over given connection" """
        connection.set_remote()
        super().connect(connection)

    def on_connected(self) -> None:
        """ "called when robot gets connected to remote device , load all setup data;" """
        super().on_connected()

        # AbstractRobotDevice<?,?> dataHub = this.deviceList.getDeviceOnId(DataHub.ID);
        # dataHub.remote_pingDevice();

        for device in self._device_list:
            device.set_transmitter(self._connection)
            device.on_connected()

    def on_disconnected(self) -> None:
        """ called when robot gets disconnected from remote device  """
        for _device in self._device_list:
            # _device.on_disconnected(self)
            pass  # FIXME DataHub has no .on_disconnected
        super().on_disconnected()

    def receive(self, remote_data: RemoteDataPacket) -> None:
        source = remote_data.get_source_address()
        device = self.get_device_on_id(source)

        if device is not None:
            device.receive(remote_data)
            data_packet = remote_data.get_data_packet()
            if data_packet is None:
                print("#" * 10)
                print(remote_data)
                print("#" * 10)
                raise Exception
            self._data_packet_logger.add_input_packet(data_packet)

    def get_panaromas(self) -> List["Panorama"]:
        raise ValueError("WIP: Panoramas not yet implemented")
        return self._panoramas

    def get_behavior(self) -> "RobotBehavior":
        raise ValueError("WIP: Behavior not yet implemented")
        return self._behavior

    def get_robot_name(self) -> str:
        # TODO why not just reuse get_name()
        return self._name

    def get_controls(self) -> List["BehaviorControl"]:
        raise ValueError("WIP: Behavior not yet implemented")
        return self.behavior.get_controls()

    def get_destination(self) -> "Destination":
        raise ValueError("WIP: Destination not yet implemented")

    def get_navigation_path(self) -> "NavigationPath":
        raise ValueError("WIP: NavigationPath not yet implemented")

    def get_field_of_view_on_name(self, name: str) -> "FieldOfView":
        raise ValueError("WIP: FieldOfView not yet implemented")
        for field_of_view in self._fields_of_views:
            if field_of_view.get_name() == name:
                return field_of_view
        return None

    def get_field_of_view_on_id(self, id: int) -> "FieldOfView":
        raise ValueError("WIP: FieldOfView not yet implemented")
        for field_of_view in self._fields_of_views:
            if field_of_view.has_id(id):
                return field_of_view
        return None

    def add_main_hub(self, name_meta_data: "ComponentMetaData") -> None:
        raise ValueError("WIP: ComponentMetaData not yet implemented")
        meta_data: List["ComponentMetaData"] = [name_meta_data]
        self._device_list.add(DataHub(meta_data))

    def add_field_of_view(self, field_of_view: "FieldOfView") -> None:
        raise ValueError("WIP: FieldOfView not yet implemented")
        self._fields_of_views.append(field_of_view)
