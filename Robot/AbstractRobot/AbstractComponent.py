from RoboControl.Robot.Value.ComponentValue import ComponentValue

class AbstractComponent:
    def __init__(self, meta_data):
        self._global_id = meta_data["global_id"]
        self._name = meta_data["name"]
        self._transmitter = None
      

    def get_name(self):
        return self._name

    get_component_name = get_name

    def set_component_name(self, name: str) -> None:
        self._name = name

    def get_global_id(self) -> int:
        """ "gets component global id this is the unique id for this component in a Robot" """
        return self._global_id

    def set_transmitter(self, transmitter):
        """ set transmitter for this component. All data will be sent thru this transmitter """
        self._transmitter = transmitter

    def get_data_values(self):
        return []

    def get_control_values(self):
        return []

  
class AbstractComponentList(list):
    def get_component_on_name(self, name):
        """ "search for a component in device with given name" """
        for component in self:
            if component.get_component_name() == name:
                return component
        return None

    def get_component_on_global_id(self, id):
        """ "search for a component in device with given globalId" """
        for component in self:
            if component.get_global_id() == id:
                return component
        return None

    def get_data_values(self) -> list[ComponentValue]:
        values = []
        for component in self:
            values += component.get_data_values()
        return values

    def get_control_values(self) -> list[ComponentValue]:
        values = []
        for component in self:
            values += component.get_control_values()
        return values