class DataAquisator:
    """ "provides container for data aquisators. Data aquisators are used for periodic broadcast of device data." """

    def __init__(self, name: str, default_period: int, id: int):
        """ "generates a data aquisator with given name and id, id corresponds to device internal broadcast command" """
        self._name = name
        self._period = default_period
        self._id = id
        self._status = False

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def __str__(self):
        return self.get_name()

    def set_period(self, period: int) -> None:
        """ "set the refresh frequency"
        @:param period in 10 milliseconds steps
        """
        self._period = period

    def get_period(self) -> int:
        return self._period

    def is_on(self) -> bool:
        return self._status

    def set_on(self) -> None:
        self._status = True

    def set_off(self) -> None:
        self._status = False
