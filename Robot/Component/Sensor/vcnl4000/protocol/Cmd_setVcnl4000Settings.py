from typing import Union

from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000AveragingModes import Vcnl4000AveragingModes
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000FrequencyModes import Vcnl4000FrequencyModes
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000IrCurrent import Vcnl4000IrCurrent
from RoboControl.Robot.Component.Sensor.vcnl4000.protocol.RemoteParameterVcnl4000Settings import \
    RemoteParameterVcnl4000Settings

INDEX_SENSOR = 0
INDEX_PARAMETERS = 1


class Cmd_setVcnl4000Settings(RemoteCommand):
    _parameter_list: list[Union[RemoteParameterUint8, RemoteParameterVcnl4000Settings]]

    def __init__(self, id: int):
        # name = "setMpu9150Settings" # description = "set settings for a mpu9150Sensor"
        super().__init__(id, "setVcnl4000Settings", "set settings for a Vcnl4000 Sensor")
        # RemoteParameterUint8("index","mpu9150 sensor index")
        self._parameter_list.append(RemoteParameterUint8("index", "VCNL4000 sensor index"))
        self._parameter_list.append(RemoteParameterVcnl4000Settings())

    @staticmethod
    def get_command(
            id: int,
            index: int = None,
            ir_current: Vcnl4000IrCurrent = None,
            averaging_mode: Vcnl4000AveragingModes = None,
            proximity_frequency: Vcnl4000FrequencyModes = None,
            auto_conversion: bool = None,
            auto_compensation: bool = None,
    ) -> "Cmd_setVcnl4000Settings":
        cmd = Cmd_setVcnl4000Settings(id)
        if None not in [ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation]:
            cmd.set_data(index, ir_current, averaging_mode, proximity_frequency, auto_conversion, auto_compensation)
        return cmd

    def set_data(
            self,
            index: int,
            ir_current: Vcnl4000IrCurrent,
            averaging_mode: Vcnl4000AveragingModes,
            proximity_frequency: Vcnl4000FrequencyModes,
            auto_conversion: bool,
            auto_compensation: bool,
    ) -> None:
        self._parameter_list[INDEX_SENSOR].set_value(index)
        self._parameter_list[INDEX_PARAMETERS].set_ir_current(ir_current)
        self._parameter_list[INDEX_PARAMETERS].set_averaging_mode(averaging_mode)
        self._parameter_list[INDEX_PARAMETERS].set_proximity_frequency(proximity_frequency)
        self._parameter_list[INDEX_PARAMETERS].set_auto_conversion(auto_conversion)
        self._parameter_list[INDEX_PARAMETERS].set_auto_compensation(auto_compensation)

    def get_index(self) -> int:
        return self._parameter_list[INDEX_SENSOR].get_value()
