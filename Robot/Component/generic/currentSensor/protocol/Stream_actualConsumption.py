from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteStream import RemoteStream


class Stream_actualConsumption(RemoteStream):
	def __init__(self, id):
		super().__init__(id, "stream_actualConsumption", "measured current values from device size, size/count is device dependent")

	
	def get_command(id , size):
		cmd = Stream_actualConsumption(id)
		for index in range (0, size):
			cmd._parameter_list.append(RemoteParameterUint16("current","measured current for sensor"+str(index)))
		return (cmd)	



	def get_actual_consumption(self, index):
		value = 0

		if index < len(self._parameter_list):
			value = self._parameter_list[index].get_value()

		return value


"""package de.hska.lat.robot.component.currentSensor.protocol;

	
	
	
public Stream_actualConsumption()
{
}


public Stream_actualConsumption(int command)
{
	this();
	this.setId(command);
}




@Override
public String getName() 
{
	return(Stream_actualConsumption.name);
}


@Override
public String getDescription() 
{
	return(Stream_actualConsumption.description);
}


public void setData(int... values)
{
	int enumerator;
	RemoteParameterUint16 parameter;
	
	enumerator = 0;
	
	for (int value : values)
	{
		parameter = new RemoteParameterUint16("current","measured current for sensor "+enumerator);
		parameter.setValue(value);
		this.add(parameter);
	}
}


@Override
public void parseDataPacketData(RemoteDataPacket packet)
{
	int dataIndex;
	int enumerator;
	ByteBuffer dataBuffer;
	RemoteParameter<?> parameter;
	
	dataIndex=0;
	
	dataBuffer = packet.getDataBuffer();
	enumerator =0;
	

	
	for (dataIndex = 0; dataIndex<dataBuffer.capacity();enumerator++)
	{
		parameter = new RemoteParameterUint16("current","measured current for sensor "+enumerator);
		dataIndex+=parameter.parseFromBuffer(dataBuffer, dataIndex);
		this.add(parameter);
	}
	

	
	
}



public int getValuesCount()
{
	return(this.size());	
}



public int getValue(int index)
{
	if (index < this.size())
	{
		return((( RemoteParameterUint16) this.get(index)).getValue());
	}
	
return(0);	
}





public static Stream_actualConsumption getCommand(int command)
{
	Stream_actualConsumption cmd;
	cmd = new Stream_actualConsumption(command);
	
	return(cmd);
}





public static Stream_actualConsumption getCommand(int command, int...values)
{
	Stream_actualConsumption cmd;
	cmd = Stream_actualConsumption.getCommand(command);
	cmd.setData(values);
	
	return(cmd);
}



}
"""