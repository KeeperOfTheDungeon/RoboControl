#import threading
from time import sleep
from machine import Pin
import rp2
import _thread


from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.Pico.DataPacketPico import DataPacketPico


class PicoInput(RemoteDataInput):

    def __init__(self):
        print("init - PicoInput")
        Pin(1, Pin.IN, Pin.PULL_UP)
        self._state_machine_rx = rp2.StateMachine(1, self.rx, freq=10000000, in_base=Pin(1), jmp_pin=Pin(1))

        self._state_machine_rx.irq(lambda x: {print('error: usart did not recieve end bit')})
        self._state_machine_rx.active(1)
        self._running = True
        self._data_packet = DataPacketPico()

    def run(self) -> None:
        _thread.start_new_thread(self.process, ())
                
    def process(self) -> None:
        while self._running:
            token = self._state_machine_rx.get()
            print('Recieved token: ' + str(token))

            if self._data_packet.putToken(token):  # put token  into datapacket - if endsync detected function will return True
                print("data packet recieved")
                remote_data = self._data_packet.decode()
                print(str(remote_data))

                self.deliver_packet(remote_data)

                self._data_packet = DataPacketPico()
            

    def stop(self):
        self.running = False
        self._state_machine_rx.active(0)

    
    @rp2.asm_pio(in_shiftdir=rp2.PIO.SHIFT_RIGHT)
    def rx():
        wrap_target()

        # wait for start bit
        label('ready')
        wait(0, pins, 2)
        wait(1, pins, 2)
        jmp(pin, 'ready')

        # accept message
        set(x, 8)
        wait(0, pins, 2)
        
        label('loop')
        
        wait(1, pins, 2)
        in_(pins, 1)
        wait(0, pins, 2)
        
        jmp(x_dec, 'loop')

        # wait for end bit
        wait(1, pins, 2)
        jmp(pin, 'end_bit')

        # exception thrown to main thread
        irq(block, rel(0))
        
        jmp('end')

        # normal execution
        label('end_bit')
        in_(null, 23)
        push()
        
        label('end')

        wrap()



