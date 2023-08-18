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

Byte: TypeAlias = int


class PicoOutput(RemoteDataOutput):

    def __init__(self):
        self._state_machine_tx = rp2.StateMachine(0, self.tx, freq=1000000, out_base=Pin(0), sideset_base=Pin(0))

        self._state_machine_tx.active(1)
        self._data_out_buffer = int(256)
        self.out_byte_pointer = 0

    def send_token(self, token: Byte) -> bool:
        if self._state_machine_tx is not None:
            self._data_out_buffer[self.out_byte_pointer] = token
            self.out_byte_pointer += 1
        return True

    def transmit(self, data_packet: RemoteDataPacket) -> bool:
        self.out_byte_pointer = 0
        if isinstance(data_packet, RemoteCommandDataPacket):
            self.send_token(DataPacketPico.COMMAND_START_TOKEN)
        elif isinstance(data_packet, RemoteMessageDataPacket):
            self.send_token(DataPacketPico.MESSAGE_START_TOKEN)
        elif isinstance(data_packet, RemoteStreamDataPacket):
            self.send_token(DataPacketPico.STREAM_START_TOKEN)
        else:
            raise ValueError("WIP: packet_types are not implemented")
        self.send_token(data_packet.get_destination_address())
        self.send_token(data_packet.get_source_address())
        self.send_token(data_packet.get_command())
        for index in range(0, len(data_packet.get_data())):
            self.send_token(data_packet.get_byte(index))
        self.send_token(DataPacketPico.END_TOKEN)

        try:
            for token in self._data_out_buffer:
                self._state_machine_tx.put(token)
        except Exception as e:
            traceback.print_exception(e)
        return False


    def stop(self):
        self._state_machine_rx.active(0)

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

