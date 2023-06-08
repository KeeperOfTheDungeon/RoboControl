class RemoteDataPacket:

    # _source_addres = 0
    # destination_addres = 0
    # command  = 0
    # reply  = 0

    def __init__(self, type_name):
        self._type_name = type_name
        self.data = None

    # FIXME not used?
    # noinspection PyAttributeOutsideInit
    def a(self, destination_addres, source_addres, command):
        self._source_addres = source_addres
        self._destination_addres = destination_addres
        self._command = command
        # this.timestamp=new Date();

    def get_source_address(self):
        return self._source_address

    def get_destination_address(self):
        return self._destination_address

    def alocate(self, size):
        self.data = bytearray(size)

    def decode(self, data_buffer):
        pass

    def code(self):
        pass

    def set_byte(self, position, value):
        """ set a byte in payload array
        version :1.0
        date : 2022.02.01
        author dungeon keeper
        """
        self.data[position] = value

    def get_byte(self, position):
        """ get a byte from payload array
        version :1.0
        date : 2022.02.01
        author dungeon keeper
        """

        return self.data[position]

    def set_int_16(self, position, value):
        self.data[position] = value >> 8
        self.data[position + 1] = value & 0xff

    def get_int_16(self, position):
        value = (self.data[position] << 8) & 0xff00
        value |= self.data[position + 1] & 0xff
        return value

    def set_int_24(self, position, value):
        self.data[position] = (value >> 16) & 0xff
        self.data[position + 1] = (value >> 8) & 0xff
        self.data[position + 2] = value & 0xff

    def get_int_24(self, position):
        value = (self.data[position] << 16) & 0xff0000
        value |= (self.data[position + 1] << 8) & 0xff00
        value |= self.data[position + 2] & 0xff
        return value

    def set_int_32(self, position, value):
        self.data[position] = (value >> 24) & 0xff
        self.data[position + 1] = (value >> 16) & 0xff
        self.data[position + 2] = (value >> 8) & 0xff
        self.data[position + 3] = value & 0xff

    def get_int_32(self, position):
        value = (self.data[position] << 24) & 0xff000000
        value |= (self.data[position + 1] << 16) & 0xff0000
        value |= (self.data[position + 2] << 8) & 0xff00
        value |= self.data[position + 3] & 0xff
        return value

    def get_type_name(self):
        return self._type_name
