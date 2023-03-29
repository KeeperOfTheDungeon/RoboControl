from RoboControl.Com.Remote.Parameter import RemoteParameterUint32
from RoboControl.Com.Remote.Parameter.RemoteParameterUint32 import RemoteParameterUint32
from RoboControl.Com.Remote.RemoteStream import RemoteStream


class Stream_totalConsumption(RemoteStream):
	def __init__(self, id):
		super().__init__(id, "stream_maxConsumption", "measured total current values from device size, size/count is device dependent")

	
	def get_command(id , size):
		cmd = Stream_totalConsumption(id)
		for index in range (0, size):
			cmd._parameter_list.append(RemoteParameterUint32("current","measured current for sensor"+str(index)))
		return (cmd)	



	def get_total_consumption(self, index):
		value = 0

		if index < len(self._parameter_list):
			value = self._parameter_list[index].get_value()

		return value
		
		

"""package de.hska.lat.robot.component.currentSensor.protocol;

import java.nio.ByteBuffer;

import de.hska.lat.comm.remote.RemoteDataPacket;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.comm.remote.parameter.RemoteParameter;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint32;


public class Stream_totalConsumption extends RemoteStream
{


	
	
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 3175880214514883228L;
	/**
	 * 
	 */
	
	
	
	protected static final String name = "totalConsumption";
	protected static final String description = "measured current values from device size, size/count is device dependent";
	
	
	
	
	
	
public Stream_totalConsumption()
{
}


public Stream_totalConsumption(int command)
{
	this();
	this.setId(command);
}




@Override
public String getName() 
{
	return(Stream_totalConsumption.name);
}


@Override
public String getDescription() 
{
	return(Stream_totalConsumption.description);
}


public void setData(int... values)
{
	int enumerator;
	RemoteParameterUint32 parameter;
	
	enumerator = 0;
	
	for (int value : values)
	{
		parameter = new RemoteParameterUint32("current","measured current for sensor "+enumerator);
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
		parameter = new RemoteParameterUint32("current","measured current for sensor "+enumerator);
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
		return((( RemoteParameterUint32) this.get(index)).getValue());
	}
	
return(0);	
}





public static Stream_totalConsumption getCommand(int command)
{
	Stream_totalConsumption cmd;
	cmd = new Stream_totalConsumption(command);
	
	return(cmd);
}





public static Stream_totalConsumption getCommand(int command, int...values)
{
	Stream_totalConsumption cmd;
	cmd = Stream_totalConsumption.getCommand(command);
	cmd.setData(values);
	
	return(cmd);
}



}
"""