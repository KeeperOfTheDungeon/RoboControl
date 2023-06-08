# noinspection PyShadowingBuiltins
class RemoteData:

    def __init__(self, id, name, description):
        self._source_addres = 0
        self._destination_addres = 0
        self._id = id

        self._name = name
        self._description = description
        self._parameter_list = list()
        self._payload = bytearray()

    def set_id(self, id):
        self._id = id

    def get_id(self):
        return self._id

    def get_payload_size(self):
        size = 0
        for parameter in self._parameter_list:
            size += parameter.get_byte_size()
        return size

    def has_id(self, id):
        return self._id == id

    def get_destination_addres(self):
        return self._destination_addres

    def set_destination_addres(self, destination):
        self._destination_addres = destination

    def get_source_addres(self):
        return self._source_addres

    def set_source_addres(self, source):
        self._source_addres = source

    def get_data_packet(self):
        pass

    def make_data_packet(self, data_packet):
        # data_packet.set_remote_data()
        pass

    def set_payload(self, payload):
        self._payload = payload

    def get_payload(self):
        return self._payload

    def parse_payload(self, payload):

        if self.get_payload_size() != len(payload):
            print("wrong payload")
        else:
            print("correct payload")
            index = 0
            print(payload)
            for parameter in self._parameter_list:
                index += parameter.parse_from_buffer(payload, index)

    def to_string(self):
        # WIP pick one
        _ = """
        print(self._name, "destination -", self._destination_addres, "| source -", self._source_addres, "| id -",
              self._id)

        for parameter in self._parameter_list:
            print(parameter.get_name(), parameter.get_value())
        """
        print(self._name, " : lenge - ", len(self._payload))
        for byte in self._payload:
            print(byte, end=", ")

    def get_name(self):
        return self._name

    def get_description(self):
        return self._description


"""package de.hska.lat.comm.remote;



    protected int id;

    
    protected int destination;
    protected int source;

    
public RemoteData()
{
}

"""

"""
protected RemoteDataPacket makeDataPacket(RemoteDataPacket dataPacket)
{
    

    dataPacket.setRemoteData(this);
    
    
    ByteBuffer messageData = ByteBuffer.allocate(this.getBufferSize());
    
    
    for (RemoteParameter<?> parameter : this)
    {
        parameter.putData(messageData);
    }
    
    dataPacket.setData(messageData.array());
    
    return(dataPacket);
}







public void parseDataPacket(RemoteDataPacket packet)
{
    this.source = packet.getSourceAddres();
    this.destination = packet.getDestinationAddres();
    
    this.parseDataPacketData(packet);
}





public void parseDataPacketData(RemoteDataPacket packet)
{
    int dataIndex;
    
    ByteBuffer dataBuffer;
    
    dataIndex=0;
    
    dataBuffer = packet.getDataBuffer();
    
    for (RemoteParameter<?> parameter : this)
    {
        dataIndex+=parameter.parseFromBuffer(dataBuffer, dataIndex);
    }

}

public String getName() 
{
    return (RemoteData.name);
}

public String getDescription() 
{
    return(RemoteData.description);
}


public String getTypeName()
{
    return ("generic");
}


public int getParameterCount()
{
    return(this.size());
}



public String getParametersAsString(boolean description)
{
    String parameters = new String();
    boolean first=true;
    
    for (RemoteParameter<?> parameter : this)
    {
        if (first!=true)
        {
            parameters +=  ", ";
        }
        parameters += parameter.getAsString(description);
        first=false;
    }

    
    return(parameters);
}

}
"""
