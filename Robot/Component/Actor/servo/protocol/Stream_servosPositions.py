from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition


class Stream_servosPositions(RemoteStream):

	def __init__(self, id):
		super().__init__(id, "Stream_servoPositions", "actual servo positions")


	def get_command(id , size):
		cmd = Stream_servosPositions(id)
		for index in range (0, size):
			cmd._parameter_list.append(RemoteParameterServoPosition("position ", "position for servo "+str(index)))
		return (cmd)	




	def get_position(self, index):
		value = 0

		if index < len(self._parameter_list):
			value = self._parameter_list[index].get_position()

		return value
"""
package de.hska.lat.robot.component.actor.servo.protocol;

import java.nio.ByteBuffer;

import de.hska.lat.comm.remote.RemoteDataPacket;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.comm.remote.parameter.RemoteParameter;


public class Stream_servosPositions extends RemoteStream
{


	
	/**
	 * 
	 */
	private static final long serialVersionUID = 4452549041406810297L;
	
	
	protected static final String name = "servoPositions";
	protected static final String description = "actual servo positions ";
	
	
	
	
	
	
public Stream_servosPositions()
{
}


public Stream_servosPositions(int command)
{
	this();
	this.setId(command);
}


public String getName() 
{
	return (Stream_servosPositions.name);
}



public String getDescription() 
{
	return(Stream_servosPositions.description);
}


public void setData(float... positions)
{
	int enumerator;
	RemoteParameterServoPosition parameter;
	
	enumerator = 0;
	
	for (float position : positions)
	{
		parameter = new RemoteParameterServoPosition("position "+enumerator,"position for servo "+enumerator);
		parameter.setPosition(position);
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
		parameter = new RemoteParameterServoPosition("position "+enumerator,"position for servo "+enumerator);
		dataIndex+=parameter.parseFromBuffer(dataBuffer, dataIndex);
		this.add(parameter);
	}
}



public int getPositionsCount()
{
	return(this.size());	
}



public float getPosition(int index)
{
	if (index < this.size())
	{
		return((( RemoteParameterServoPosition) this.get(index)).getPosition());
	}
	
	
	
return(0);	
}





public static Stream_servosPositions getCommand(int command)
{
	Stream_servosPositions cmd;
	cmd = new Stream_servosPositions(command);
	
	return(cmd);
}





public static Stream_servosPositions getCommand(int command, float...positions)
{
	Stream_servosPositions cmd;
	cmd = Stream_servosPositions.getCommand(command);
	cmd.setData(positions);
	
	return(cmd);
}



}
"""