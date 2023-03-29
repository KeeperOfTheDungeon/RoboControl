
from RoboControl.Com.Remote.Parameter.RemoteParameterUint24 import RemoteParameterUint24
from RoboControl.Com.Remote.RemoteStream import RemoteStream


class Stream_distances(RemoteStream):
	def __init__(self, id):
		super().__init__(id, "distances", "actual distances measured by distance sensors")

	def get_command(id , size):
		cmd = Stream_distances(id)
		for index in range (0, size):
			cmd._parameter_list.append(RemoteParameterUint24("distance ","distance for sensor "+str(index)))
		return (cmd)	



	def get_distance(self, index):
		value = 0

		if index < len(self._parameter_list):
			value = self._parameter_list[index].get_value()

		return value


"""
package de.hska.lat.robot.component.generic.distance.protocol;

import java.nio.ByteBuffer;

import de.hska.lat.comm.remote.RemoteDataPacket;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.comm.remote.parameter.RemoteParameter;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint24;




/**
 * 
 * @author Oktavian Gniot
 *
 *command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor
 */

public class Stream_distances extends RemoteStream
{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 2638694167468005642L;



	protected static final String name = "distances";
	protected static final String description = "actual distances measured by distance sensors";


public Stream_distances() 
{
}
	
	
public Stream_distances(int command) 
{
	this();
	this.setId(command);
}


@Override
public String getName() 
{
	return(Stream_distances.name);
}


@Override
public String getDescription() 
{
	return(Stream_distances.description);
}



public void setData(int... values)
{
	int enumerator;
	RemoteParameterUint24 parameter;
	
	enumerator = 0;
	
	for (int value : values)
	{
		parameter = new RemoteParameterUint24("distance ","distance for sensor "+enumerator);
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
		parameter = new RemoteParameterUint24("distance ","distance for sensor "+enumerator);
		dataIndex+=parameter.parseFromBuffer(dataBuffer, dataIndex);
		this.add(parameter);
	}
	

	
	
}


public int getDistance(int index)
{
	if (index < this.size())
	{
		return((( RemoteParameterUint24) this.get(index)).getValue());
	}
	
return(0);	
}




public static Stream_distances getCommand(int id)
{
	Stream_distances cmd;
	cmd = new Stream_distances(id);
	
	return(cmd);
}



public static Stream_distances getCommand(int command, int...distances)
{
	Stream_distances cmd;
	cmd = Stream_distances.getCommand(command);
	cmd.setData(distances);
	
	return(cmd);
}


}

"""