from RoboControl.Com.RemoteData import RemoteMessage, RemoteStream
from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent
from RoboControl.Robot.Component.RobotComponent import RobotComponent


class ComponentSet(list):
    """ "Basis class for a list of device components of same type" """

    _transmitter = None

    def __init__(self, components):
        super().__init__(components)

    def get_component_on_global_id(self, id: int) -> Optional[AbstractComponent]:
        """ "search for an component with given id" """
        for component in self:
            if component.get_global_id() == id:
                return component
        return None

    def get_component_on_local_id(self, id: int) -> Optional[RobotComponent]:
        """ "find component with given id in this set" """
        for component in self:
            if component.get_local_id() == id:
                return component
        return None

    def get_data_values(self):
        return [c.get_values() for c in self]

    def get_command_processors(self):
        return list()

    def get_message_processors(self):
        return list()

    def get_stream_processors(self):
        return list()

    def get_ids(self) -> List[int]:
        ids = []
        for index, component in enumerate(self):
            ids[index] = component.get_global_id()
        return ids

    def load_settings(self):
        for sensor in self:
            sensor.remote_load_defaults()
            sensor.remote_get_settings()

    def get_components(self) -> list:
        """ "returns an array list with all components of this set" """
        return list(self)

    def set_transmitter(self, transmitter):
        self._transmitter = transmitter
        for component in self:
            component.set_transmitter(self._transmitter)

    def decode_message(self, remote_data):
        return False

    def decode_stream(self, remote_data) :
        return False
