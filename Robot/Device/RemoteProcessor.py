from RoboControl.Com.RemoteData import RemoteCommand, RemoteMessage, RemoteStream, RemoteException


# WIP check if this merged right

class RemoteProcessor:

    def __init__(self, remote_data, remote_processor):
        self._remote_data = remote_data
        self._remote_processor = remote_processor

    def has_remote_id(self, id):
        if self._remote_data.get_id() == id:
            return True
        return False

    def get_remote_data(self):
        return self._remote_data

    def get_remote_id(self):
        return self._remote_data.get_id()

    def execute(self, remote_data):

        remote_dict = remote_data.__dict__
        print(remote_dict)
        for parameter in remote_dict["_parameter_list"]:
            print(parameter.get_as_string(True))

        if self._remote_processor is None:
            return
        if callable(self._remote_processor):
            return self._remote_processor(remote_data)
        # vorsortierung um sp#tzer ifs zu sparen
        if isinstance(remote_data, RemoteCommand):
            self._remote_processor.decode_command(remote_data)
        elif isinstance(remote_data, RemoteMessage):

            self._remote_processor.decode_message(remote_data)
        elif isinstance(remote_data, RemoteStream):
            self._remote_processor.decode_stream(remote_data)
        elif isinstance(remote_data, RemoteException):
            self._remote_processor.decode_exception(remote_data)
        # elif isinstance(remote_data, RemoteAlert):
        #     self._remote_processor.decode_exception(remote_data)


class RemoteProcessorList(list):
    def find_on_id(self, id):
        #print("RPL : looking for id - ", id)
        for processor in self:
            #print("RPL : ", processor, " id : ", processor.get_remote_id())
            if processor.has_remote_id(id):
                return processor
        return None
