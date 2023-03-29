from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.RemoteDataOutput import RemoteDataOutput
from RoboControl.Com.Ascii.DataPacketAscii import DataPacketAscii
from RoboControl.Com.Remote.RemoteCommandDataPacket import RemoteCommandDataPacket
from RoboControl.Com.Remote.RemoteMessageDataPacket import RemoteMessageDataPacket
from RoboControl.Com.Remote.RemoteStreamDataPacket import RemoteStreamDataPacket


import serial.tools.list_ports

class AsciiOutput(RemoteDataOutput):
	
	def __init__(self, serial_output):
		self._serial_output = serial_output

	def transmitt(self, data_packet):
		print("transmitt")
		data_packet.set_source_addres(1)
		self._packet_queue.append(data_packet)

		self.transmitt_packet(data_packet)
		pass


	def transmitt_packet(self, data_packet):    
		ascii_data = DataPacketAscii()
		ascii_data.code(data_packet)
		self.send(ascii_data)



	def send(self,ascii_data):
		
		self._serial_output.write(ascii_data.get_ascii_buffer())
