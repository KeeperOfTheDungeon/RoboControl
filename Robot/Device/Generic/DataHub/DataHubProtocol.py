from RoboControl.Com.Connection import Connection
# from RoboControl.Robot.Component.text.protocol.Msg_textFragment import Msg_textFragment
# from RoboControl.Robot.Device.Generic.DataHub.DataHub import DataHub
from RoboControl.Robot.Device.Protocol.DeviceProtocol import DeviceProtocol
from RoboControl.Robot.Device.Protocol.Msg_nodeType import Msg_nodeType
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor

MSG_NODE_TYPE = 0x2
CMD_GET_NODE_TYPE = 0x5
MSG_TEXT_FRAGMENT = 0x20
CMD_GET_TEXT = 0x20


class DataHubProtocol(DeviceProtocol):
    def __init__(self, device: "DataHub"):
        super().__init__(device)
        # self._message_list.append(
        #     RemoteProcessor(
        #         Msg_textFragment(MSG_TEXT_FRAGMENT),
        #         device.get_texts
        #     ),
        # )

    def get_text_protocol(self, device_id: int) -> "TextProtocol":
        raise ValueError("WIP: TextProtocol")
        return TextProtocol(
            0,
            0,  # cmdSetSettingsId,
            0,  # cmdGetSettingsId
            0,  # cmdSaveDefaultsId
            0,  # cmdLoadDefaultsId
            0,  # msgSettingsId
            CMD_GET_TEXT,  # cmdGetText
            0  # msgTextFragment
        )

    @staticmethod
    def msg_node_type() -> Msg_nodeType:
        cmd = Msg_nodeType(MSG_NODE_TYPE)
        cmd.set_data(Connection.REMOTE_CHANEL_ID)
        return cmd
