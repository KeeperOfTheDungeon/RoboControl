from RoboControl.Robot.Value.ComponentValue import ComponentValue


class LuxValue(ComponentValue):

    def __init__(self, meta_data):
        meta_data["type_name"] = "lux"
        meta_data["description"] = "lux"
        super().__init__(meta_data)
