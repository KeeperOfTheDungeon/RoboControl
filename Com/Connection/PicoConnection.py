from RoboControl.Com.Pico.PicoInput import PicoInput
from RoboControl.Com.Pico.PicoOutput import PicoOutput
from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
import rp2
import utime
import _thread

class PicoConnection(Connection):
    connected: bool = False

    def __init__(self, meta_data):
        super().__init__()
        print("PicoConnection - init")
        self._rxpin = meta_data["rx_pin"]		#extract receiver pin from settings
        self._txpin = meta_data["tx_pin"]		#extract transmitter pin from settings
        self._clock_pin = meta_data["clock_pin"]#extract clock pin from settings
        
        # clear programs form pio for clean restart
        rp2.PIO(0).remove_program()
        rp2.PIO(1).remove_program()



    def connect(self, listener) -> None:
        super().connect(listener)
        if not self.connected:
            self._data_output = PicoOutput(self._txpin, self._clock_pin) # add data_output
            self._data_input = PicoInput(self._rxpin, self._clock_pin) # add data_input
        
        _thread.start_new_thread(self.connection_thread, ())
            
    def disconnect(self) -> None:
        self._data_input.stop()
        self._data_output.stop()
        super().disconnect()


        
    def connection_thread(self):
        while True:
            self._data_input.process()
            self._data_output.process()


