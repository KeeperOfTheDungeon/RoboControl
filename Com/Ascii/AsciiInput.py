import threading
from time import sleep

from serial import Serial

from RoboControl.Com.ComStatistic import ComStatistic
from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii

from logger import getLogger

logger = getLogger(__name__)


class AsciiInput(RemoteDataInput):

    def __init__(self, serial_input: Serial, statistic: ComStatistic):
        super().__init__(statistic)
        self._serial_input = serial_input

    def run_threaded(self):
        self.running = True
        x = threading.Thread(target=self.run)
        x.start()

    def run(self) -> None:
        print("x is running")

        receiving_packet = False
        ascii_data_packet = DataPacketAscii()

        while self.running:
            # try
            while (
                    self.running and self._serial_input
                    and self._serial_input.is_open
                    and self._serial_input.in_waiting < 1
            ):
                sleep(0.001)
            if not self.running:
                break

            self.statistic.count_up_recived_chars()

            token = self._serial_input.read(1)

            if DataPacketAscii.is_start_token(token):
                if receiving_packet:
                    self.statistic.count_up_error_packets()
                receiving_packet = True
                ascii_data_packet = DataPacketAscii()

            ascii_data_packet.put_token(token)

            if DataPacketAscii.is_end_token(token):
                if not receiving_packet:
                    self.statistic.count_up_error_packets()
                    continue
                logger.debug(ascii_data_packet.get_ascii_buffer())
                remote_data = ascii_data_packet.decode()
                # data_packet_buffer = copy(data_packet._data_buffer)
                # data_packet = DataPacketAscii.parse_ascii(data_packet_buffer)

                # self.deliver_packet(remote_data)
                data_packet = remote_data.get_data_packet()
                self.deliver_packet(data_packet)

                self.statistic.count_up_recived_packets()
                receiving_packet = False
                ascii_data_packet = DataPacketAscii()

            # } catch (IOException e) { e.printStackTrace();
            # } catch (InterruptedException e) { e.printStackTrace();
            # } catch(Exception e) { System.out.println("kill that bloody BUG !!! :"); e.printStackTrace();}
