from RoboControl.Robot.AbstractRobot.AbstractProtocol import AbstractProtocol

CMD_PING = 0x03

CMD_GET_NODE_ID = 0x05

CMD_GET_COM_STATISTICS = 0x06
CMD_CLEAR_COM_STATISTICS = 0x07

CMD_GET_CPU_STATISTICS = 0x08
CMD_CLEAR_CPU_STATISTICS = 0x09

CMD_GET_NEXT_ERROR = 0x0A
CMD_GET_ERROR_COUNT = 0x0B

CMD_START_STREAM_DATA = 0x10
CMD_STOP_STREAM_DATA = 0x11
CMD_CLEAR_ALL_DATA_STREAMS = 0x12
CMD_PAUSE_ALL_DATA_STREAMS = 0x13
CMD_CONTINUE_ALL_DATA_STREAMS = 0x14
CMD_SAVE_STREAMS = 0x15
CMD_LOAD_STREAMS = 0x16

MSG_PING_RESPONSE = 0x01

MSG_COM_STATUS = 0x03
MSG_CPU_STATUS = 0x04

STREAM_COM_STATISTICS = 0x03
STREAM_CPU_STATISTICS = 0x04


class DeviceProtocol(AbstractProtocol):
    def __init__(self, device):
        super().__init__()
        self._device_id = device.get_id()
        self._device = device

        self._message_list = []
        self._stream_list = []
