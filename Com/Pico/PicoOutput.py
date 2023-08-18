#import traceback
#from typing import TypeAlias

#from serial import Serial
from machine import Pin
#from time import sleep
import rp2

from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput
from RoboControl.Com.Pico import DataPacketPico
from RoboControl.Com.Remote.RemoteCommandDataPacket import RemoteCommandDataPacket
from RoboControl.Com.Remote.RemoteMessageDataPacket import RemoteMessageDataPacket
from RoboControl.Com.Remote.RemoteStreamDataPacket import RemoteStreamDataPacket


class PicoOutput(RemoteDataOutput):

    def __init__(self):
        self._state_machine_tx = rp2.StateMachine(0, self.tx, freq=1000000, out_base=Pin(0), sideset_base=Pin(0))
        self._state_machine_tx.active(1)

    def transmitt(self, data_packet: RemoteDataPacket) -> None:
        print("transmitt")
        data_packet.set_source_addres(1)
        pico_data = DataPacketPico()
        pico_data.code(data_packet)
        token_buffer = pico_data.get_buffer()
        
        for token in token_buffer:
            self._state_machine_tx.put(token)


    def stop(self):
        self._state_machine_tx.active(0)

    @rp2.asm_pio(out_init=rp2.PIO.OUT_HIGH,
             out_shiftdir=rp2.PIO.SHIFT_RIGHT,
             sideset_init=rp2.PIO.OUT_HIGH)
    def tx():
        wrap_target()

        #start bit
        pull()
        wait(0, pins, 2)
        set(x, 8)    .side(0)
        wait(1, pins, 2)

        # message
        label('loop')
        wait(0, pins, 2)
        out(pins, 1)
        wait(1, pins, 2)
        jmp(x_dec, 'loop')

        #end bit
        wait(0, pins, 2)
        mov(x,x)    .side(1)
        wait(1, pins, 2)
        
        
        wait(0, pins, 2)
        mov(x,x)    .side(1)
        wait(1, pins, 2)

        wrap()

