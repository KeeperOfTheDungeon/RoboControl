#import threading
from time import sleep
from machine import Pin
import rp2



from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.Pico.DataPacketPico import DataPacketPico


class PicoInput(RemoteDataInput):

    def __init__(self):
        print("init - PicoInput")
        Pin(1, Pin.IN, Pin.PULL_UP)
        self._state_machine_rx = rp2.StateMachine(1, self.rx, freq=10000000, in_base=Pin(1), jmp_pin=Pin(1))

        self._state_machine_rx.irq(lambda x: {print('error: usart did not recieve end bit')})
        self._state_machine_rx.active(1)
        self.running = True
       # self.x = threading.Thread(target=self.run)
       # self.x.start()
        self.run()

    def run(self) -> None:
        print("x is running")

        data_packet = DataPacketPico()

        while self.running:
            print("alive")
            if self._state_machine_rx.rx_fifo() > 1:
                token = self._state_machine_rx.get()

                if data_packet.putToken(token):  # put token  into datapacket - if endsync detected function will return True
                    print("dp")
                    remote_data = data_packet.decode()
                    print(str(remote_data))

                    self.deliver_packet(remote_data)

                    data_packet = DataPacketPico()

            else:
                sleep(0.001)

            pass

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

