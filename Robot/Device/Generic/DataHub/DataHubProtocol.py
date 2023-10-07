from RoboControl.Com.Connection import Connection
from RoboControl.Robot.Device.Protocol.DeviceProtocol import DeviceProtocol
from RoboControl.Robot.Device.Protocol.Msg_nodeType import Msg_nodeType
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor

MSG_NODE_TYPE = 0x2
CMD_GET_NODE_TYPE = 0x5
MSG_TEXT_FRAGMENT = 0x20
CMD_GET_TEXT = 0x20


class DataHubProtocol(DeviceProtocol):
    _device: "DataHub"

    def get_text_protocol(self):  # TextProtocol
        protocol = {
            "device_id": self._device_id,
            "cmd_getText": CMD_GET_TEXT,
            "msg_textFragment": MSG_TEXT_FRAGMENT,
        }
        return protocol

    @staticmethod
    def msg_node_type() -> Msg_nodeType:
        cmd = Msg_nodeType(MSG_NODE_TYPE)
        cmd.set_data(Connection.REMOTE_CHANEL_ID)
        return cmd
