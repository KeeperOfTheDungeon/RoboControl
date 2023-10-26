from RoboControl.Robot.Value.ComponentValue import ComponentValue
#from RoboView.Robot.Viewer.RobotSettings import RobotSettings

class AbstractComponent:
    def __init__(self, meta_data):
        self._global_id = meta_data["global_id"]
        self._name = meta_data["name"]
        self._transmitter: RemoteDataTransmitter = None
        self._instance_key: str = f"{self.__class__.__name__}.{self._global_id}"
        self._settings: RobotSettings = None

    def get_name(self):
        return self._name

    get_component_name = get_name

    def set_component_name(self, name: str) -> None:
        self._name = name

    def get_global_id(self) -> int:
        """ "gets component global id this is the unique id for this component in a Robot" """
        return self._global_id

    def set_transmitter(self, transmitter: RemoteDataTransmitter):
        """ set transmitter for this component. All data will be sent thru this transmitter """
        self._transmitter = transmitter

    def get_data_values(self) -> List[ComponentValue]:
        return []

    def get_control_values(self) -> List[ComponentValue]:
        return []

    def get_control_clients(self) -> List[ComponentValue]:
        return []

    def recover_string(self, key: str, value: str) -> str:
        """ "recover a String value from active settings. This property key will be generated from instance key + local key" """
        return self._settings.recover_string(self._instance_key + key, value)

    def recover_int(self, key: str, value: int) -> str:
        """ "recover a integer value from active settings. This property key will be generated from instance key + local key" """
        return self._settings.recover_int(self._instance_key + key, value)

    def recover_boolean(self, key: str, value: bool) -> str:
        """ "recover a boolean value from active settings. This property key will be generated from instance key + local key" """
        return self._settings.recover_boolean(self._instance_key + key, value)

    def save_string(self, key: str, value: str) -> str:
        """ "save a string value in active settings. This property key will be generated from instance key + local key" """
        return self._settings.save_string(self._instance_key + key, value)

    def save_int(self, key: str, value: int) -> str:
        """ "save a integer value in active settings. This property key will be generated from instance key + local key" """
        return self._settings.save_int(self._instance_key + key, value)

    def save_boolean(self, key: str, value: int) -> str:
        """ "save a boolean value in active settings. This property key will be generated from instance key + local key" """
        return self._settings.save_boolean(self._instance_key + key, value)

    def on_save_settings(self) -> None:
        raise ValueError("WIP AbstractComponent.on_save_settings")

    def on_load_settings(self) -> None:
        raise ValueError("WIP AbstractComponent.on_load_settings")
