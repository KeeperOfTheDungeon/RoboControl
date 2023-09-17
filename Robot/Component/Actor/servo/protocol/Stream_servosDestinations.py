from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition


class Stream_servosDestinations(RemoteStream):

    def __init__(self, id):
        super().__init__(id, "Stream_servoDestinations", "actual servo destinations")

    def get_command(id, size):
        cmd = Stream_servosDestinations(id)
        for index in range(0, size):
            cmd._parameter_list.append(
                RemoteParameterServoPosition("destination ", "destination for servo " + str(index)))
        return (cmd)

    def get_destination(self, index):
        value = 0

        if index < len(self._parameter_list):
            value = self._parameter_list[index].get_position()

        return value


"""package de.hska.lat.robot.component.actor.servo.protocol;

import java.nio.ByteBuffer;

import de.hska.lat.comm.remote.RemoteDataPacket;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.comm.remote.parameter.RemoteParameter;


public class Stream_servosDestinations extends RemoteStream
{


    
    
    
    /**
     * 
     */
    private static final long serialVersionUID = 3949845149294356524L;
    protected static final String name = "servoDestinations";
    protected static final String description = " servo destinations";
    
    
    
    
public Stream_servosDestinations()
{
}


public Stream_servosDestinations(int command)
{
    this();
    this.setId(command);
}


public String getName() 
{
    return (Stream_servosDestinations.name);
}



public String getDescription() 
{
    return(Stream_servosDestinations.description);
}



public void setData(float... destinations)
{
    int enumerator;
    RemoteParameterServoPosition parameter;
    
    enumerator = 0;
    
    for (float position : destinations)
    {
        parameter = new RemoteParameterServoPosition("destination "+enumerator,"destination for servo "+enumerator);
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
        parameter = new RemoteParameterServoPosition("destination "+enumerator,"destination for servo "+enumerator);
        dataIndex+=parameter.parseFromBuffer(dataBuffer, dataIndex);
        this.add(parameter);
    }
}



public int getPositionsCount()
{
    return(this.size());	
}



public float getDestination(int index)
{
    if (index < this.size())
    {
        return((( RemoteParameterServoPosition) this.get(index)).getPosition());
    }
    
    
    
return(0);	
}





public static Stream_servosDestinations getCommand(int command)
{
    Stream_servosDestinations cmd;
    cmd = new Stream_servosDestinations(command);
    
    return(cmd);
}





public static Stream_servosDestinations getCommand(int command, float...destination)
{
    Stream_servosDestinations cmd;
    cmd = Stream_servosDestinations.getCommand(command);
    cmd.setData(destination);
    
    return(cmd);
}



}
"""
