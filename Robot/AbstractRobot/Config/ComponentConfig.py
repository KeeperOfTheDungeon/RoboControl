class ComponentConfig:
    def __init__(self, name, local_id, global_id):
        self._name = name
        self._global_id = global_id
        self._local_id = local_id
        

    def get_local_id(self):
         return(self._local_id)

    def get_global_id(self):
         return(self._global_id)

    def get_name(self):
        return(self._name)