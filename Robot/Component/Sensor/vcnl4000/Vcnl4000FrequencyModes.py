class Vcnl4000FrequencyModes:
    def __init__(self, number: int, frequency: str):
        self._number = number
        self._frequency = frequency

    def get_number(self) -> int:
        return self._number

    def get_frequency(self) -> str:
        return self._frequency

    @staticmethod
    def get(index: int) -> "Vcnl4000FrequencyModes":
        for value in Vcnl4000FrequencyModesEnum.values():
            if value.get_number() == index:
                return value
        return Vcnl4000FrequencyModesEnum.MODE_3_125_MHZ

    @staticmethod
    def get_default() -> "Vcnl4000FrequencyModes":
        """ "get vcnl4000 default frequency mode. This mode is set on Sensor reset" """
        return Vcnl4000FrequencyModesEnum.MODE_781_25_KHZ

    def __str__(self) -> str:
        return f"{self._frequency}"


class Vcnl4000FrequencyModesEnum:
    MODE_3_125_MHZ = Vcnl4000FrequencyModes(0, "3.125 MHz")
    MODE_1_5625_MHZ = Vcnl4000FrequencyModes(1, "1.5625 MHz")
    MODE_781_25_KHZ = Vcnl4000FrequencyModes(2, "781.25 kHz")
    MODE_390_625_Khz = Vcnl4000FrequencyModes(3, "390.625 kHz")

    @staticmethod
    def values() -> list[Vcnl4000FrequencyModes]:
        return [f for f in dir(Vcnl4000FrequencyModesEnum) if isinstance(f, Vcnl4000FrequencyModes)]
