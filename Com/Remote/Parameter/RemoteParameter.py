class RemoteParameter:
    def __init__(self, name, description, size):
        self._name = name
        self._descritption = description
        self._byte_size = size
        pass

    def get_name(self):
        return self._name

    def get_descritption(self):
        return self._descritption

    def get_byte_size(self):
        return self._byte_size

    def get_as_buffer(self):
        pass

    def put_data(self):
        pass

    def parse_from_buffer(self, data_buffer, index):
        pass

    def get_as_string(self):
        return "unknown"
