from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Sensor.vcnl4000.protocol.RemoteParameterVcnl4000Settings import \
    RemoteParameterVcnl4000Settings

INDEX_SENSOR = 0
INDEX_PARAMETERS = 1


class Msg_vcnl4000Settings(RemoteMessage):
    _parameter_list: list[RemoteParameterUint8, RemoteParameterVcnl4000Settings]

    def __init__(self, id: int):
        super().__init__(id, "setVcnl4000Settings", "set settings for a Vcnl4000 Sensor")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        self._parameter_list.append(RemoteParameterVcnl4000Settings())

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            ir_current: "Vcnl4000IrCurrent" = None,
            averaging_mode: "Vcnl4000AveragingModes" = None,
            proximity_frequency: "Vcnl4000FrequencyModes" = None,
            auto_conversion: bool = None,
            auto_compensation: bool = None,
    ) -> "Msg_vcnl4000Settings":
        cmd = Msg_vcnl4000Settings(id)
        if None not in [ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation]:
            cmd.set_data(index, ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation)
        return cmd

    def set_data(
            self,
            index: int,
            ir_current: "Vcnl4000IrCurrent",
            averaging_mode: "Vcnl4000AveragingModes",
            proximity_frequency: "Vcnl4000FrequencyModes",
            auto_conversion: bool,
            auto_compensation: bool,
    ) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[INDEX_PARAMETERS].set_ir_current(ir_current)
        self._parameter_list[INDEX_PARAMETERS].set_averaging_mode(averaging_mode)
        self._parameter_list[INDEX_PARAMETERS].set_proximity_frequency(proximity_frequency)
        self._parameter_list[INDEX_PARAMETERS].set_auto_conversion(auto_conversion)
        self._parameter_list[INDEX_PARAMETERS].set_auto_compensation(auto_compensation)

    def get_ir_current(self) -> "Vcnl4000IrCurrent":
        return self._parameter_list[INDEX_PARAMETERS].get_ir_current()

    def get_averaging_mode(self) -> "Vcnl4000AveragingModes":
        return self._parameter_list[INDEX_PARAMETERS].get_averaging_mode()

    def get_proximity_frequency(self) -> "Vcnl4000FrequencyModes":
        return self._parameter_list[INDEX_PARAMETERS].get_proximity_frequency()

    def get_auto_conversion(self) -> bool:
        return self._parameter_list[INDEX_PARAMETERS].get_auto_conversion()

    def get_auto_compensation(self) -> bool:
        return self._parameter_list[INDEX_PARAMETERS].get_auto_compensation()

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
