from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteStream import RemoteStream


class Stream_maxConsumption(RemoteStream):
	def __init__(self, id):
		super().__init__(id, "stream_maxConsumption", "measured max current values from device size, size/count is device dependent")

	
	def get_command(id , size):
		cmd = Stream_maxConsumption(id)
		for index in range (0, size):
			cmd._parameter_list.append(RemoteParameterUint16("current","measured current for sensor"+str(index)))
		return (cmd)	



	def get_max_consumption(self, index):
		value = 0

		if index < len(self._parameter_list):
			value = self._parameter_list[index].get_value()

		return value
		
		
	"""package de.hska.lat.robot.component.currentSensor.protocol;

import java.nio.ByteBuffer;

import de.hska.lat.comm.remote.RemoteDataPacket;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.comm.remote.parameter.RemoteParameter;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint16;


public class Stream_maxConsumption extends RemoteStream
{


	
	
	
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 8877204081092268546L;
	
	
	protected static final String name = "maxConsumptions";
	protected static final String description = "measured current values from device size, size/count is device dependent";
	
	
	
	
	
	
public Stream_maxConsumption()
{
}


public Stream_maxConsumption(int command)
{
	this();
	this.setId(command);
}




@Override
public String getName() 
{
	return(Stream_maxConsumption.name);
}


@Override
public String getDescription() 
{
	return(Stream_maxConsumption.description);
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





public static Stream_maxConsumption getCommand(int command)
{
	Stream_maxConsumption cmd;
	cmd = new Stream_maxConsumption(command);
	
	return(cmd);
}





public static Stream_maxConsumption getCommand(int command, int...values)
{
	Stream_maxConsumption cmd;
	cmd = Stream_maxConsumption.getCommand(command);
	cmd.setData(values);
	
	return(cmd);
}



}
"""