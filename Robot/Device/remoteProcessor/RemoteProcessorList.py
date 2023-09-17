class RemoteProcessorList(list):
    def find_on_id(self, id):
        # print("RPL : looking for id - ",id)
        for processor in self:
            # print("RPL : ",processor, " id : ", processor.get_remote_id())
            if processor.has_remote_id(id):
                return processor
        return None
