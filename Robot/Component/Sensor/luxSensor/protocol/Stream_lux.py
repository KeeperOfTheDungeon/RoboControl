from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Sensor.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue

class Stream_lux(RemoteStream):

	def __init__(self, id):
		super().__init__(id, "luxValues", "actual lux Values measured by lux sensors")


	def get_command(id , size):
		cmd = Stream_lux(id)
		for index in range (0, size):
			cmd._parameter_list.append(RemoteParameterLuxValue("brightness ","value for sensor "+str(index)))
		return (cmd)	




	def get_lux_Value(self, index):
		value = 0

		if index < len(self._parameter_list):
			value = self._parameter_list[index].get_lux()

		return value


"""package de.hska.lat.robot.component.generic.luxSensor.protocol;

import java.nio.ByteBuffer;

import de.hska.lat.comm.remote.RemoteDataPacket;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.comm.remote.parameter.RemoteParameter;





/**
 * 
 * @author Oktavian Gniot
 *
 *command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor
 */

public class Stream_lux extends RemoteStream
{
	

	/**
	 * 
	 */
	private static final long serialVersionUID = 5103359306711895136L;
	protected static final String name = "measuredLuxValues";
	protected static final String description = "actual measured light in lux";


public Stream_lux() 
{
}
	
	
public Stream_lux(int command) 
{
	this();
	this.setId(command);
}


@Override
public String getName() 
{
	return(Stream_lux.name);
}


@Override
public String getDescription() 
{
	return(Stream_lux.description);
}



public void setData(float... values)
{
	int enumerator;
	RemoteParameterLuxValue parameter;
	
	enumerator = 0;
	
	for (float value : values)
	{
		parameter = new RemoteParameterLuxValue("lux ","measured lux value from sensor "+enumerator);
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
	enumerator = 0;
	

	
	for (dataIndex = 0; dataIndex<dataBuffer.capacity()-1;enumerator++)
	{
		parameter = new RemoteParameterLuxValue("lux ","measured lux value from sensor "+enumerator);
		dataIndex+=parameter.parseFromBuffer(dataBuffer, dataIndex);
		this.add(parameter);
	}
	

	
	
}


public float getLuxValue(int index)
{
	if (index < this.size())
	{
		return((( RemoteParameterLuxValue) this.get(index)).getValue());
	}
	
return(0);	
}




public static Stream_lux getCommand(int id)
{
	Stream_lux cmd;
	cmd = new Stream_lux(id);
	
	return(cmd);
}



public static Stream_lux getCommand(int command, float...valuess)
{
	Stream_lux cmd;
	cmd = Stream_lux.getCommand(command);
	cmd.setData(valuess);
	
	return(cmd);
}


}

"""