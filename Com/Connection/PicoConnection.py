from RoboControl.Com.Pico.PicoInput import PicoInput
from RoboControl.Com.Pico.PicoOutput import PicoOutput
from RoboControl.Com.Connection.Connection import Connection
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
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

    def connect(self, listener) -> None:
        super().connect(listener)
        if not self.connected:
            self._data_output = PicoOutput() # add data_output
            self._data_input = PicoInput() # add data_input
            self._data_input.run()

            
    def disconnect(self) -> None:
        self._data_input.stop()
        self._data_output.stop()
        super().disconnect()

            


