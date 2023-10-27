from typing import List


from RoboControl.Robot.Component.text.TextSet import TextSet
from RoboControl.Robot.Component.text.protocol.Msg_textFragment import Msg_textFragment
from RoboControl.Robot.Device.Generic.DataHub.DataHubAquisator import DataHubAquisator
from RoboControl.Robot.Device.Generic.DataHub.DataHubProtocol import DataHubProtocol, MSG_TEXT_FRAGMENT
from RoboControl.Robot.Device.RobotDevice import RobotDevice



class DataHub(RobotDevice):
    name = "DataHub"
    ROBOT_NAME = "name"
    ID = 0
    _texts: TextSet



    def build(self):
        self._protocol = DataHubProtocol(self)

        self._aquisators = DataHubAquisator.get_data_aquisators()

        self.add_texts([])  # WIP

        self.build_protocol()


    def build_protocol(self):
        super().build_protocol()
        self.add_message_processor(
            Msg_textFragment(MSG_TEXT_FRAGMENT),
            self
        )

    def get_texts(self) -> "TextSet":
        return self._texts

    def add_texts(self, texts):
        self._texts = TextSet(texts, self._protocol.get_text_protocol())
        self.add_component_set(self._texts)

    def load_setup(self):
        for text in self._texts:
            text.remote_get_text()
