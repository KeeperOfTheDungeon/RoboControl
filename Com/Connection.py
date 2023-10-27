#from RoboControl.Com.PacketLogger.DataPacketLogger import DataPacketLogger
from RoboControl.Com.RemoteData import RemoteData
from RoboControl.Com.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.ComStatistic import ComStatistic


REMOTE_CHANEL_ID: int = 1
REMOTE_NODE_ID: int = 1


class RemoteDataInput:
    _listener_list  = list()

    def __init__(self, statistic):
        self.statistic = statistic
        self.running = False
        # self.set_daemon(True)

    def run(self) -> None:
        pass

    def add_listener(self, listener):
        """
        "ad a listener to the distribution list so this listener will become every incoming data packets received thru this input"
        :param listener:
        :return:
        """
        # print(" RDI : add_listener", self._listener_list)
        self._listener_list.append(listener)

    def remove_listener(self, listener):
        """
        remove a listener from the distribution list, so this listener will not become any mor packets
        :param listener: to be removed from distribution list
        :return:
        """
        self._listener_list.remove(listener)

    def deliver_packet(self, data_packet: RemoteDataPacket):
        """ "Deliver a new received data packet to all members of the distribution list (listeners)" """
        # print(self._listener_list)
        if data_packet is not None:
            for listener in self._listener_list:
                listener.receive(data_packet)

    def is_running(self) -> bool:
        return self.running    
    

class RemoteDataOutput:
    _packet_queue = list()
    _listener_list = list()
    _is_remote = False
    _is_running = False

    def __init__(self, statistic):
        self.statistic = statistic

    def run(self):
        pass

    def add_listener(self, listener):
        pass

    def remove_listener(self, liustener):
        pass

    def is_running(self):
        return self._is_running

    def set_remote(self):
        self._is_remote = True

    def get_remote(self):
        return self._is_remote

    def transmitt(self, data_packet: RemoteDataPacket):
        print ("RDO : default Transmitter")
        return False

    def send_byte(self, token):
        return False




class Connection:  # ConnectionControlInterface, RemoteDataTransmitter
    _data_packet_logger = None #: DataPacketLogger

    def __init__(self, name: str = ""):
        self.device_id = REMOTE_CHANEL_ID
        self.connection_name: str = name
        self.connection_partner: str = ""

        self.statistic = ComStatistic()
        self._data_output: RemoteDataOutput = RemoteDataOutput(self.statistic)
        self._data_input: RemoteDataInput = RemoteDataInput(self.statistic)

    def connect(self, data_packet_receiver):
        self._data_input.add_listener(data_packet_receiver)

    def disconnect(self):
        self._data_input.running = False

   # def is_remote(self):
  #      return self._data_output.get_remote()

  #  def set_remote(self):
  #      self._data_output.set_remote()

    def transmitt(self, remote_data: RemoteData):
        # print("c : Transmitt")
        if self._data_output is None:
            print("Can't transmit as _data_output isn't set.")
            return False
      #  if self.is_remote():
      #      remote_data.set_source_address(self.device_id)
      #  else:
      #      remote_data.set_destination_address(self.device_id)
  
        data_packet= remote_data.get_data_packet()
        
        if data_packet is None:
            raise ValueError(f"Incompatible remote_data type ({type(remote_data)}): {remote_data}")
        data_packet.set_remote_data(remote_data)
        # TODO find a solution for Pico
        if self._data_packet_logger is not None:
            self._data_packet_logger.add_output_packet(data_packet)
        print("c : Transmitting")
        # print(self._data_output)
        self._data_output.transmitt(data_packet)
        
        return True

    def set_data_packet_logger(self, data_packet_logger):
        self._data_packet_logger = data_packet_logger

    def get_data_packet_logger(self):
        return self._data_packet_logger

    def get_connection_name(self):
        return self.connection_name

    def get_partner_name(self):
        return self.connection_partner

    def get_statistic(self):
        return self.statistic
    
