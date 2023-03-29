package de.hska.lat.robot.component.actor.servo.protocol;

import de.hska.lat.comm.remote.RemoteCommand;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;






/**
 * command that ping a device, device returns ping response message  
 * @author Oktavian Gniot
 *
 */
public class Cmd_getServoPosition extends RemoteCommand
{
	

	
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;


	private static final int INDEX_SERVO = 0;
	

	protected static final String name = "getServoPosition";
	protected static final String description = "getPosition of a servo";
	
	
public Cmd_getServoPosition() 
{
	this.add(new RemoteParameterUint8("index","index of servo"));
}



public Cmd_getServoPosition(int command) 
{
	this();
	this.setId(command);
}


public void setData(int index)
{
	(( RemoteParameterUint8) this.get(Cmd_getServoPosition.INDEX_SERVO)).setValue(index);
}



public int getIndex()
{
	return((( RemoteParameterUint8) this.get(Cmd_getServoPosition.INDEX_SERVO)).getValue());
}



@Override
public String getName() 
{
	return(Cmd_getServoPosition.name);
}


@Override
public String getDescription() 
{
	return(Cmd_getServoPosition.description);
}



public static Cmd_getServoPosition getCommand(int command)
{
	Cmd_getServoPosition cmd;
	cmd = new Cmd_getServoPosition(command);
	
	return(cmd);
}

public static Cmd_getServoPosition getCommand(int command,int index)
{
	Cmd_getServoPosition cmd;
	cmd = Cmd_getServoPosition.getCommand(command);
	cmd.setData(index);
	
	return(cmd);
}


}
