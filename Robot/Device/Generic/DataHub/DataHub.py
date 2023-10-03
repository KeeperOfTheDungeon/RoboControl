from typing import List

from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Device.Generic.DataHub.DataHubAquisator import DataHubAquisator
from RoboControl.Robot.Device.Generic.DataHub.DataHubProtocol import DataHubProtocol
from RoboControl.Robot.Device.Protocol.DeviceProtocol import DeviceProtocol
from RoboControl.Robot.Device.Protocol.Msg_pingResponse import Msg_pingResponse
from RoboControl.Robot.Device.RobotDevice import RobotDevice


class DataHub(RobotDevice):
    name = "DataHub"
    ROBOT_NAME = "name"
    ID = 0

    def __init__(self, component_config):
        super().__init__(component_config)  # super(DataHub.NAME, DataHub.ID)
        self._aquisators = DataHubAquisator.get_data_aquisators()
        # self.add_texts(component_config)

    def build(self):
        self._protocol = DeviceProtocol(self)  # WIP DataHubProtocol
        self.build_protocol()

    def get_texts(self) -> "TextSet":
        return self._texts

    def add_texts(self, texts: List["ComponentMetaData"]) -> None:
        self._texts = TextSet(texts, DataHubProtocol.get_text_protocol(self.get_id()))
        self.add_components(self._texts)

    def load_setup(self) -> None:
        for text in self._texts:
            text.remote_get_text()
