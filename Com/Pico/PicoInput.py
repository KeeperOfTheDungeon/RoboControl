#import threading
from time import sleep
from machine import Pin
import rp2



from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.Pico.DataPacketPico import DataPacketPico



class PicoInput(RemoteDataInput):
    clock_pin = 2
    def __init__(self):
        clock_pin = 2
        self.led_onboard = Pin(5, Pin.OUT)
        print("init - PicoInput")
        Pin(1, Pin.IN, Pin.PULL_UP)
        self._state_machine_rx = rp2.StateMachine(1, self.rx, freq=10000000, in_base=Pin(1), jmp_pin=Pin(1))

        self._state_machine_rx.irq(lambda x: {print('error: usart did not recieve end bit')})
        #self._state_machine_rx.irq(self.sync_error())
        self._state_machine_rx.active(1)
        self.running = True
        self._data_packet = DataPacketPico()
        self.counter = 0



    def process(self):

       # if self._state_machine_rx.rx_fifo() > 1:
            token = self._state_machine_rx.get()
            print("t : ",token)
           # if self._data_packet.putToken(token):  # put token  into datapacket - if endsync detected function will return True
           #     print("dp")
           #     remote_data = self._data_packet.decode()
             

           #     self.deliver_packet(remote_data)

           #     self._data_packet = DataPacketPico()



    def run(self) -> None:
        print("x is running")

        data_packet = DataPacketPico()

        while self.running:
          #  print("alive : ",self.counter)
           # self.counter+=1
            #self.led_onboard.on()
            while self._state_machine_rx.rx_fifo() > 0:
                
                token = self._state_machine_rx.get()
                  
                if data_packet.putToken(token) == DataPacketPico.PACKET_READY:  # put token  into datapacket - if endsync detected function will return True
                    remote_data = data_packet.decode()
                    self.deliver_packet(remote_data)

                #    data_packet = DataPacketPico()
            else:
               # sleep(0.001)
                #sleep(1)
                pass
            #self.led_onboard.off()
            
#    with print & deliver 5 ms
            

    def stop(self):
        self.running = False
        self._state_machine_rx.active(0)

    def sync_error(self):
        print('sync error: usart did not recieve end bit')
        #ToDo abfangen und rücksetzen
    
    @rp2.asm_pio(in_shiftdir=rp2.PIO.SHIFT_RIGHT)
    def rx():
        wrap_target()

        # wait for start bit
        label('ready')
        wait(0, pins, 2)		# warte auf 0 bei clock
        wait(1, pins, 2)		# warte auf 1 bei clock
        jmp(pin, 'ready') 		# wenn pin High dann kein Startbit

        # accept message
        set(x, 8)				# setze counter auf 8 bits
        wait(0, pins, 2)		# warte auf 0 bei clock 
        
        label('loop')
        
        wait(1, pins, 2)		# warte auf 1 bei clock
        in_(pins, 1)			# holle aktuelles bit
        wait(0, pins, 2)		# Warte auf 0 beiu clock
        
        jmp(x_dec, 'loop')		# nächsten bit hollen (solange n > 0)

        # wait for end bit
        wait(1, pins, 2)		# warte auf 1 bei Clock
        jmp(pin, 'end_bit')		# springe zu ende 

        # exception thrown to main thread
        irq(block, rel(0))
        
        jmp('end')				# ende

        # normal execution
        label('end_bit')	
        in_(null, 23)
        #in_(null, 9)		
        push()				# push data to RX FIFO
      #  push()
        label('end')

        wrap()

