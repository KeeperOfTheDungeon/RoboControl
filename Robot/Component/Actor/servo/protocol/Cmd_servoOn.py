from typing import List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8

INDEX_SERVO = 0


class Cmd_servoOn(RemoteCommand):
    _parameter_list: List[RemoteParameterUint8]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_ON):
        super().__init__(id, "cmd_servoOn", " switch servo on")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    @staticmethod
    def get_command(id, local_id):
        cmd = Cmd_servoOn(id)
        cmd.set_index(local_id)
        return cmd


"""package de.hska.lat.robot.component.actor.servo.protocol;

import de.hska.lat.comm.remote.RemoteCommand;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;






/**
 * command that ping a device, device returns ping response message  
 * @author Oktavian Gniot
 *
 */
public class Cmd_servoOn extends RemoteCommand
{
    
    

    
    /**
     * 
     */
    private static final long serialVersionUID = 3163146365421080717L;


    private static final int INDEX_SERVO = 0;
    

    protected static final String name = "servoOn";
    protected static final String description = "switch servo on";
    
    
public Cmd_servoOn() 
{
    this.add(new RemoteParameterUint8("index","index of servo"));
}



public Cmd_servoOn(int command) 
{
    this();
    this.setId(command);
}


public void setData(int index)
{
    (( RemoteParameterUint8) this.get(Cmd_servoOn.INDEX_SERVO)).setValue(index);
}



public int getIndex()
{
    return((( RemoteParameterUint8) this.get(Cmd_servoOn.INDEX_SERVO)).getValue());
}



@Override
public String getName() 
{
    return(Cmd_servoOn.name);
}


@Override
public String getDescription() 
{
    return(Cmd_servoOn.description);
}



public static Cmd_servoOn getCommand(int command)
{
    Cmd_servoOn cmd;
    cmd = new Cmd_servoOn(command);
    
    return(cmd);
}

public static Cmd_servoOn getCommand(int command,int index)
{
    Cmd_servoOn cmd;
    cmd = Cmd_servoOn.getCommand(command);
    cmd.setData(1<<index);
    
    return(cmd);
}


}
"""
