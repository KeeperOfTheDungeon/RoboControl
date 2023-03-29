from time import sleep
from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii
import threading


class AsciiInput(RemoteDataInput):
  
    def __init__(self, serial_input):
        self._serial_input = serial_input

        self.running = True
        x = threading.Thread(target=self.run)
        x.start()
        

    def run(self):
        print("x is running")

        data_packet = DataPacketAscii()

        while self.running == True:
       


            if self._serial_input.in_waiting > 1:
                token = self._serial_input.read(1)
                
                if data_packet.putToken(token) == True:
                    print("dp")
                    #check
                    remote_data = data_packet.decode()
                    remote_data.to_string()
                   
                    self.deliver_packet(remote_data)
                    #deliver !
                    #super().deliver_packet(data_packet)
                    #clear packet
                    
                    data_packet = DataPacketAscii()
                
            else:
                sleep(0.001)




            pass


