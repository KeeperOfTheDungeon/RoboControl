from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteStream import RemoteStream


COMMAND_START_TOKEN	= b'#'
COMMAND_START_TOKEN_STR = str(chr(ord(COMMAND_START_TOKEN)))

MESSAGE_START_TOKEN	= b'*'
MESSAGE_START_TOKEN_STR = str(chr(ord(MESSAGE_START_TOKEN)))

STREAM_START_TOKEN = b'$'
STREAM_START_TOKEN_STR = str(chr(ord(STREAM_START_TOKEN)))

EXCEPTION_START_TOKEN = b'^'
ALLERT_START_TOKEN = b'!'

OK_START_TOKEN			= b'O'
FAIL_START_TOKEN		= b'N'
END_TOKEN   = b';'

class DataPacketAscii(RemoteDataPacket):



    def __init__(self):
        self._token_counter = 0
        self._data_buffer = ""
        pass



    def decode(self):
  
        #print(self.data_buffer)
        index = 0

        message_type = self._data_buffer[index]

        if message_type == COMMAND_START_TOKEN_STR:
            print("Message sync")
            remote_data = RemoteCommand(0,"","")
            self.do_decode(remote_data)


        elif message_type == MESSAGE_START_TOKEN_STR:
            print("Message sync")
            remote_data = RemoteMessage(0, "","")
            self.do_decode(remote_data)

        elif message_type == STREAM_START_TOKEN_STR:
            print("Stream sync")
            remote_data = RemoteStream(0,"","")
            self.do_decode(remote_data)

        else:
            print("unsync")
            remote_data = RemoteData(0,"","")

        return remote_data    


    def do_decode(self,remote_data ):

            index = 1


            remote_data._destination_addres = int(self._data_buffer[index:index+2],16)   
            index += 2


            remote_data._source_addres = int(self._data_buffer[index:index+2],16)   
            index += 2


            remote_data._id = int(self._data_buffer[index:index+2],16)   
            index += 2

            # get payload

            data_size = len(self._data_buffer)
            data_size -= index+1
            data_size /=2
            #data_size = int((len(self._data_buffer) - (index+1)) /2)

            payload = bytearray(int(data_size))
            pindex = 0

            while index < (len(self._data_buffer)-1):
                value = int(self._data_buffer[index:index+2],16)   
                index += 2
                payload[pindex] = value
                pindex += 1
        
            remote_data.set_payload(payload)

          
  
            #error - exception

       # return remote_data



    def putToken(self, token):

        end_token  = False

      #  try:
        self._data_buffer += str(token,'utf-8')
        self._token_counter += 1



        if token == END_TOKEN:
            end_token = True
        
        return end_token  




    def code(self, data_packet):
        payload_size = data_packet.get_payload_size() * 2
        payload_size += 8

        self._data_buffer = bytearray(payload_size) 

        index = 0

        # command mark
        if isinstance(data_packet,RemoteCommand):
            self._data_buffer[index] = ord(COMMAND_START_TOKEN)
        elif isinstance(data_packet,RemoteMessage):
            self._data_buffer[index] = ord(MESSAGE_START_TOKEN)

        print(type(data_packet))
        index += 1


        destination = data_packet.get_destination_addres()
        self._data_buffer[index] = get_char(destination >> 4 )
        index += 1
        self._data_buffer[index] = get_char(destination & 0xf )
        index += 1


        source = data_packet.get_source_addres()
        self._data_buffer[index] = get_char(source >> 4 )
        index += 1
        self._data_buffer[index] = get_char(source & 0xf )
        index += 1


        command = data_packet.get_id()
        self._data_buffer[index] = get_char(command >> 4 )
        index += 1
        self._data_buffer[index] = get_char(command & 0xf )
        index += 1

        #send Data payload

        self._data_buffer[len(self._data_buffer)-1] = ord(END_TOKEN)
        
     
        for parameter in data_packet._parameter_list:

            buffer = parameter.get_as_buffer()
            for byte in buffer:
                self._data_buffer[index] = get_char(byte >> 4 )
                index+=1
                self._data_buffer[index] = get_char(byte & 0xf )
                index+=1



    def get_ascii_buffer(self):
        return self._data_buffer




def get_char(data_byte):

    if data_byte > 9:
        value =data_byte  + 0x37
    else:
        value = data_byte + 0x30
    
    return value



def hex_char_to_nibble(data_byte):
    if (data_byte>0x40) & (data_byte<0x47):
        data_byte-=0x37
    elif (data_byte > 0x60) & ( data_byte < 0x67):
        data_byte-=0x57

    elif (data_byte>0x2f) & (data_byte<0x3a):
        data_byte-=0x30

    else:
        pass
        #throw new ConversionException(databyte);

    return(data_byte)


