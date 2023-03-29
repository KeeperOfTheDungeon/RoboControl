class DeviceConfig:
    
    def __init__(self, id, name):
        self._name = name
        self._id = id


    def get_id(self):
        return self._id