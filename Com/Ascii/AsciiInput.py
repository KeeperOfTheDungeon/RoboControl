import threading
from time import sleep

from serial import Serial

from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii


class AsciiInput(RemoteDataInput):

    def __init__(self, serial_input: Serial):
        self._serial_input = serial_input

        self.running = True
        x = threading.Thread(target=self.run)
        x.start()

    def run(self) -> None:
        print("x is running")

        data_packet = DataPacketAscii()

        while self.running:

            if self._serial_input.in_waiting > 1:
                token = self._serial_input.read(1)

                if data_packet.putToken(token):
                    # print("dp")
                    # check
                    remote_data = data_packet.decode()
                    # print(str(remote_data))

                    self.deliver_packet(remote_data)
                    # deliver !
                    # super().deliver_packet(data_packet)
                    # clear packet

                    data_packet = DataPacketAscii()

            else:
                sleep(0.001)

            pass
