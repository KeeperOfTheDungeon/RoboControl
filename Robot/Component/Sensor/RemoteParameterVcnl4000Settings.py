from RoboControl.Com.RemoteParameter import RemoteParameter


BYTE_SIZE = 2

IC_CURRENT_INDEX = 0
IC_CURRENT_MASK = 0x3f

FREQUENCY_MODE_INDEX = 6
FREQUENCY_MODE_MASK = 0x2

AVERAGING_MODE_INDEX = 8
AVERAGING_MODE_MASK = 0x7

CONVERSION_MODE_INDEX = 11
AUTO_OFFSET_INDEX = 12


class RemoteParameterVcnl4000Settings(RemoteParameter):

    def __init__(self):
        super().__init__("Vcnl4000 parameters", "Vcnl4000 parameters", BYTE_SIZE)

    def get_ir_current(self):
        return self._ir_current

    def set_ir_current(self, ir_currentt):
        self._ir_current = ir_current

    def get_averaging_mode(self):
        return self._averaging_mode

    def set_averaging_mode(self, averaging_mode):
        self._averaging_mode = averaging_mode

    def get_proximity_frequency(self):
        return self._proximity_frequency

    def set_proximity_frequency(self, proximity_frequency):
        self._proximity_frequency = proximity_frequency

    def get_auto_conversion(self) -> bool:
        return self._auto_conversion

    def set_auto_conversion(self, auto_conversion: bool):
        self._auto_conversion = auto_conversion

    def get_auto_compensation(self) -> bool:
        return self._auto_compensation

    def set_auto_compensation(self, auto_compensation: bool):
        self._auto_compensation = auto_compensation

    def put_data(self, data_buffer) -> None:

        data_value = 0
        data_value |= (self._ir_current.get_number() << IC_CURRENT_INDEX)
        data_value |= (self._proximity_frequency.get_number() << FREQUENCY_MODE_INDEX)
        data_value |= (self._averaging_mode.get_number() << AVERAGING_MODE_INDEX)

        if self._auto_conversion:
            data_value |= (1 << CONVERSION_MODE_INDEX)
        if self._auto_compensation:
            data_value |= (1 << AUTO_OFFSET_INDEX)
        data_value &= 0xffff
        data_buffer.put_char(data_value)

    def parse_from_buffer(self, data_buffer, index):
        data_value = data_buffer.get_char(index)
        value = data_value >> IC_CURRENT_INDEX
        masked_value = value & IC_CURRENT_MASK
        self._ir_current = Vcnl4000IrCurrent.get(masked_value)

        value = data_value >> FREQUENCY_MODE_INDEX
        masked_value = value & FREQUENCY_MODE_MASK
        self._proximity_frequency = Vcnl4000FrequencyModes.get(masked_value)

        mask = 1 << CONVERSION_MODE_INDEX
        masked_value = data_value & mask
        if masked_value:
            self._auto_conversion = True
        else:
            self._auto_conversion = False

        mask = 1 << AUTO_OFFSET_INDEX
        masked_value = data_value & mask
        if masked_value:
            self._auto_compensation = True
        else:
            self._auto_compensation = False

        # this.dlpf = Mpu9150Dlpf.get((dataValue>>RemoteParameterVcnl4000Settings.DLPF_INDEX) & 0x7);

        return self.get_byte_size()

    def get_as_string(self, description):
        infos = []
        if description:
            infos.append(self._name)
            infos.append(f"IR LED current={self._ir_current}")
            infos.append(f"frequency mode={self._proximity_frequency}")
            infos.append(f"averaging mode={self._averaging_mode}")
            infos.append(f"conversion mode={self._auto_conversion}")
            infos.append(f"auto compensation={self._auto_compensation}")
        else:
            infos.append(f"{self._ir_current}")
            infos.append(f"{self._proximity_frequency}")
            infos.append(f"{self._averaging_mode}")
            infos.append(f"{self._auto_conversion}")
            infos.append(f"{self._auto_compensation}")
        return ", ".join(infos)


