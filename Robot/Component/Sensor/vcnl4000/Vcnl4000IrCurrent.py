class Vcnl4000IrCurrent:
    def __init__(self, number: int, current: int):
        self._number = number
        self._current = current

    def get_number(self) -> int:
        return self._number

    def get_current(self) -> int:
        return self._current

    @staticmethod
    def get(index: int) -> "Vcnl4000IrCurrent":
        for value in Vcnl4000IrCurrentEnum.values():
            if value.get_number() == index:
                return value
        return Vcnl4000IrCurrentEnum.CURRENT_20MA

    @staticmethod
    def get_default() -> "Vcnl4000IrCurrent":
        """ "get VCNL 4000 default IR LED current. This current is set on sensor reset." """
        return Vcnl4000IrCurrentEnum.CURRENT_20MA

    def __str__(self) -> str:
        return f"{self._current}ma"


class Vcnl4000IrCurrentEnum:
    CURRENT_0MA = Vcnl4000IrCurrent(0, 0)
    CURRENT_10MA = Vcnl4000IrCurrent(1, 10)
    CURRENT_20MA = Vcnl4000IrCurrent(2, 20)
    CURRENT_30MA = Vcnl4000IrCurrent(3, 30)
    CURRENT_40MA = Vcnl4000IrCurrent(4, 40)
    CURRENT_50MA = Vcnl4000IrCurrent(5, 50)
    CURRENT_60MA = Vcnl4000IrCurrent(6, 60)
    CURRENT_70MA = Vcnl4000IrCurrent(7, 70)
    CURRENT_80MA = Vcnl4000IrCurrent(8, 80)
    CURRENT_90MA = Vcnl4000IrCurrent(9, 90)
    CURRENT_100MA = Vcnl4000IrCurrent(10, 100)
    CURRENT_110MA = Vcnl4000IrCurrent(11, 110)
    CURRENT_120MA = Vcnl4000IrCurrent(12, 120)
    CURRENT_130MA = Vcnl4000IrCurrent(13, 130)
    CURRENT_140MA = Vcnl4000IrCurrent(14, 140)
    CURRENT_150MA = Vcnl4000IrCurrent(15, 150)
    CURRENT_160MA = Vcnl4000IrCurrent(16, 160)
    CURRENT_170MA = Vcnl4000IrCurrent(17, 170)
    CURRENT_180MA = Vcnl4000IrCurrent(18, 180)
    CURRENT_190MA = Vcnl4000IrCurrent(19, 190)
    CURRENT_200MA = Vcnl4000IrCurrent(20, 200)

    @staticmethod
    def values() -> list[Vcnl4000IrCurrent]:
        return [f for f in dir(Vcnl4000IrCurrentEnum) if isinstance(f, Vcnl4000IrCurrent)]
