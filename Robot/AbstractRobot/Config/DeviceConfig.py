from typing import TypeAlias


class DeviceConfig:

    def __init__(self, id: int, name: str):
        self._name = name
        self._id = id

    def get_id(self) -> int:
        return self._id

    def get_name(self) -> str:
        return self._name

    def get_device_metadata(self) -> "DeviceMetaData":
        return DeviceMetaData(self._id, self._name)


DeviceMetaData: TypeAlias = DeviceConfig
