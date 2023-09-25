from RoboControl.Com.Remote.RemoteMessageDataPacket import RemoteMessageDataPacket
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket

# WIP for debugging
ALL_MESSAGES = {
    "HeadSensorsProtocol": {
        0x20: "MLX90614_SETTINGS",
        0x21: "MLX90614_AMBIENT_TEMPERATURE",
        0x22: "MLX90614_OBJECT_TEMPERATURE",
        0x23: "VCNL4020_SETTINGS",
        0x24: "VCNL4020_DISTANCE",
        0x25: "VCNL4020_DISTANCE_TABLE",
        0x26: "VCNL4020_LUX",
        0x27: "VCNL4020_RAW_PROXIMITY",
        0x28: "BMP085_SETTINGS",
        0x29: "BMP085_TEMPERATURE",
        0x2A: "BMP085_PRESURE",
    },
    "LegControllerProtocol": {
        0x20: "SERVO_SETTINGS",
        0x21: "SERVO_POSITION",
        0x22: "SERVO_SPEED",
        0x23: "SERVO_STATUS",
        0x30: "CURRENT_VALUE",
        0x32: "CURRENT_MAX_VALUE",
        0x34: "CURRENT_TOTAL_CONSUMPTION",
        0x36: "CURRENT_SETTINGS",
        0x3a: "TEMPERATURE_VALUE",
        0x3b: "TEMPERATURE_SETTINGS",
    },
    "LegSensorsProtocol": {
        0x25: " LED_BRIGHTNES",
        0x20: " VCNL4020_SETTINGS",
        0x21: " VCNL4020_DISTANCE",
        0x22: " VCNL4020_DISTANCE_TABLE",
        0x23: " VCNL4020_LUX",
        0x24: " VCNL4020_RAW_PROXIMITY",
    },
    "DataHubProtocol": {
        0x02: "MSG_NODE_TYPE",
        0x20: "MSG_TEXT_FRAGMENT",
    },
    "DeviceProtocol": {
        0x01: "MSG_PING_RESPONSE",
        0x03: "MSG_COM_STATUS",
        0x04: "MSG_CPU_STATUS",
    }
}


class RemoteMessage(RemoteData):
    _type_name: str = "message"

    def get_data_packet(self) -> RemoteMessageDataPacket:
        data_packet = RemoteMessageDataPacket(self.get_destination_address(), self.get_source_address(), self.get_id())
        return self.make_data_packet(data_packet)

    # WIP for debugging, sorry
    @staticmethod
    def guess_command_name(command_id: int) -> str:
        command_id = int(command_id)
        return (
            ALL_MESSAGES["DeviceProtocol"].get(command_id)
            or ALL_MESSAGES["DataHubProtocol"].get(command_id)
            or ALL_MESSAGES["LegSensorsProtocol"].get(command_id)
            or ALL_MESSAGES["LegControllerProtocol"].get(command_id)
            or ALL_MESSAGES["HeadSensorsProtocol"].get(command_id)
        )
