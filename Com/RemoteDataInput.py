class RemoteDataInput:
    running = False

    _listener_list = list()

    def __init__(self):
        pass

    def run(self):
        pass

    def add_listener(self, listener):
        self._listener_list.append(listener)
        pass

    def remove_listener(self, liustener):
        pass

    def deliver_packet(self, remote_data):
        for listener in self._listener_list:
            listener.receive(remote_data)

    def is_runing(self):
        pass
