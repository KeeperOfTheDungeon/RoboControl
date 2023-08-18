from RoboControl.Com.Pico.PicoInput import PicoInput
from RoboControl.Com.Pico.PicoOutput import PicoOutput
from RoboControl.Com.Connection.Connection import Connection
import rp2
import utime
import _thread

class PicoConnection(Connection):
    connected: bool = False

    def __init__(self):
        super().__init__()
        print("PicoConnection - init")
        # clear programs form pio for clean restart
        rp2.PIO(0).remove_program()
        rp2.PIO(1).remove_program()

    def connect(self, data_packet_receiver: Listener) -> None:
        if not self.connected:
            
            self._data_output = PicoOutput() # add data_output
            self._data_input = PicoInput() # add data_input
            _thread.start_new_thread(self.connection_thread, ())
            #super().connect(data_packet_receiver)

    def disconnect(self) -> None:
        self._data_input.stop()
        self._data_output.stop()
        super().disconnect()

    def connection_thread(self):
        while True:
          #  print("Hello, I'm here in the second thread writting every second")
            utime.sleep(1)
            self._data_input.process()
            
