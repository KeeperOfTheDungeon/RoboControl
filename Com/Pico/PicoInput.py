from machine import Pin
from _thread import allocate_lock
import rp2



from RoboControl.Com.RemoteDataInput import RemoteDataInput
from RoboControl.Com.Pico.DataPacketPico import DataPacketPico, END_TOKEN
from micropython import const
from array import array

TOKEN_BUFFER_SIZE = const(128)
token_buffer = array('h', [0 for i in range(TOKEN_BUFFER_SIZE)])
token_buffer_index = 0
token_buffer_read_index = 0
token = 0x000
isRead = False

class PicoInput(RemoteDataInput):
    def __init__(self, connection_counter, rxpin, clock_pin):
        self.led_onboard = Pin(5, Pin.OUT)
        print("init - PicoInput")
        Pin(rxpin, Pin.IN, Pin.PULL_UP)
        rx = rx_factory(clock_pin)
        self._state_machine_rx = rp2.StateMachine(connection_counter, rx, freq=10000000, in_base=Pin(rxpin), jmp_pin=Pin(rxpin))

        self._state_machine_rx.irq(self.interrupt_callback)

        """
        packet_one = DataPacketPico()
        packet_two = DataPacketPico()
        self._packet_list = [packet_one, packet_two]
        self._counter = 0
        self._active_packet = self._packet_list[self._counter]
        self._readable_packet = self._packet_list[self._counter]
        """
        
        self._data_packet = DataPacketPico()
        
        self._state_machine_rx.active(1)
        self.running = True

    def process(self):
        global token, token_buffer, token_buffer_index, token_buffer_read_index, isRead
        if isRead:
            #print('isRead')
            tz = token_buffer[token_buffer_read_index]
            if self._data_packet.putToken(tz) == DataPacketPico.PACKET_READY:  # put token  into datapacket - if endsync detected function will return True
                remote_data = self._data_packet.decode()
                #print('delivering package')
                self.deliver_packet(remote_data)
            token_buffer_read_index = (token_buffer_read_index + 1) % TOKEN_BUFFER_SIZE
            isRead = True if token_buffer_index > token_buffer_read_index else False

    def stop(self):
        self.running = False
        self._state_machine_rx.active(0)

    def sync_error(self):
        print('sync error: usart did not recieve end bit')
        #ToDo abfangen und rücksetzen
        

    def interrupt_callback(self, x):
        global token, token_buffer, token_buffer_index, isRead
        #print('in interrupt')
        while self._state_machine_rx.rx_fifo() > 0:
            token = self._state_machine_rx.get()
            #print(token)
            token_buffer[token_buffer_index] = token
            token_buffer_index = (token_buffer_index + 1) % TOKEN_BUFFER_SIZE
        isRead = True

def rx_factory(clock_pin):
    @rp2.asm_pio(in_shiftdir=rp2.PIO.SHIFT_RIGHT,
                fifo_join=rp2.PIO.JOIN_RX)
    def rx():
        wrap_target()

        # wait for start bit
        label('ready')
        wait(0, pins, clock_pin)		# warte auf 0 bei clock
        wait(1, pins, clock_pin)		# warte auf 1 bei clock
        jmp(pin, 'ready') 		# wenn pin High dann kein Startbit

        # accept message
        set(x, 8)				# setze counter auf 8 bits
        wait(0, pins, clock_pin)		# warte auf 0 bei clock 
            
        label('loop')
            
        wait(1, pins, clock_pin)		# warte auf 1 bei clock
        in_(pins, 1)			# holle aktuelles bit
        wait(0, pins, clock_pin)		# Warte auf 0 beiu clock
            
        jmp(x_dec, 'loop')		# nächsten bit hollen (solange n > 0)

        # wait for end bit
        wait(1, pins, clock_pin)		# warte auf 1 bei Clock
        jmp(pin, 'end_bit')		# springe zu ende 

        # exception as 10. LSB in word to main thread
        set(y, 1)
        in_(y, 23)
            
        jmp('end')				# ende

        # normal execution
        label('end_bit')	
        in_(null, 23)
            
        label('end')
        push()				# push data to RX FIFO
        irq(rel(0))

        wrap()
    return rx
