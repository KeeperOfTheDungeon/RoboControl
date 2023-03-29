from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput


REMOTE_CHANEL_ID = 1
REMOTE_NODE_ID = 1  

class Connection:

    _data_output = RemoteDataOutput()
    _data_input = RemoteDataInput()
    
    def __init__(self):
        self.device_id = REMOTE_CHANEL_ID
        self.connection_name = ""
        self.connection_partner = ""
        
    
    def connect(self, data_packet_receiver):
        self._data_input.add_listener(data_packet_receiver)
        pass
    
    def disconnect(self):
        pass

    def set_remote(self):
        self._data_output.set_remote()
        pass

    def transmitt(self, data_packet):
        self._data_output.transmitt(data_packet)
    