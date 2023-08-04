from RoboControl.Com.Pico.PicoInput import PicoInput
from RoboControl.Com.Pico.PicoOutput import PicoOutput
from RoboControl.Com.Connection.Connection import Connection


class PicoConnection(Connection):
    connected: bool = False

    open_streams: Dict[str, Optional[Serial]] = {}

    def __init__(self):
        super().__init__()

        # clear programs form pio for clean restart
        rp2.PIO(0).remove_program()
        rp2.PIO(1).remove_program()

    def connect(self, data_packet_receiver: Listener) -> None:
        if not self.connected:
            self._data_output = PicoInput() # add data_output
            self._data_input = PicoOutput # add data_input
            super().connect(data_packet_receiver)

    def disconnect(self) -> None:
        self._data_input.stop()
        self._data_output.stop()
        super().disconnect()
