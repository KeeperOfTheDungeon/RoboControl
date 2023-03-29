from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class AbstractRobot:
        
        def __init__(self):
            self._device_list = list()
            self._name = "generic"
            self._type_name = "generic"
            self._connection_listener = list()
        #connection = Connection()
        #settings
        #connection listener
            
        #dataPacket logger

            self._connection = Connection

        def get_name(self):
            return self._name


        def connect(self, connection):
            print ("connect")
            self._connection = connection
            self._connection.connect(self)
            self.on_connected()

        
        def disconnect(self, connection):    
            #this.deviceList.setTransmitter(null);
        #this.onDisconnected();
            pass

        def receive(self, data_packet):

            source = data_packet.get_source()

            for device in self.device_list:
                if device.sget_id() == source:
                    device.deliver_packet(data_packet)
                #data logger log data packet

        def get_connection(self):
            return self._connection

        def add_connection_listener(self, listener):
                self._connection_listener.appennd(listener)

        def remove_connection_listener(self, listener):
                pass

        def get_device_on_name(self, device_name):
                pass


        def get_device_on_id(self, device_id):
            for device in self._device_list:
                if device.has_id(device_id):
                    return device

            return None

        def get_component_on_global_id(self, device_id):
                pass

  

        def  get_device_list(self):
            pass

        def  get_device_count(self):
            return len(self.device_list)

        def on_connected(self):
               for listener in self._connection_listener:
                   listener.connect(self)

        def on_disconnected(self):
               for listener in self._connection_listener:
                   listener.disconnect(self)
        