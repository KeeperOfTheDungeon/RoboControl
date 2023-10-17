class Vcnl4000AveragingModes:
    def __init__(self, number: int, averaging: int):
        self._number = number
        self._averaging = averaging

    def get_number(self) -> int:
        return self._number

    def get_averaging(self) -> int:
        return self._averaging

    @staticmethod
    def get(index: int) -> "Vcnl4000AveragingModes":
        for value in Vcnl4000AveragingModesEnum.values():
            if value.get_number() == index:
                return value
        return Vcnl4000AveragingModesEnum.AVERAGING_32

    @staticmethod
    def get_default() -> "Vcnl4000AveragingModes":
        """ "sensors default averaging mode (32 conversions). This mode is set automatic on sensors reset." """
        return Vcnl4000AveragingModesEnum.AVERAGING_32

    def __str__(self) -> str:
        return f"{self._averaging} samples"


class Vcnl4000AveragingModesEnum:
    AVERAGING_1 = Vcnl4000AveragingModes(0, 0)
    AVERAGING_2 = Vcnl4000AveragingModes(1, 12)
    AVERAGING_4 = Vcnl4000AveragingModes(2, 4)
    AVERAGING_8 = Vcnl4000AveragingModes(3, 8)
    AVERAGING_16 = Vcnl4000AveragingModes(4, 16)
    AVERAGING_32 = Vcnl4000AveragingModes(5, 32)
    AVERAGING_64 = Vcnl4000AveragingModes(6, 64)
    AVERAGING_128 = Vcnl4000AveragingModes(7, 128)

    @staticmethod
    def values() -> list[Vcnl4000AveragingModes]:
        return [f for f in dir(Vcnl4000AveragingModesEnum) if isinstance(f, Vcnl4000AveragingModes)]
