from typing import List, Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition

INDEX_SERVO = 0
INDEX_POSITION = 1


class Cmd_moveServoTo(RemoteCommand):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterServoPosition]]

    def __init__(self, id: int = LegControllerProtocol.CMD_SERVO_MOVE_TO):
        super().__init__(id, "cmd_moveServoTo", " move servo to position")

        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    def set_index(self, index):
        self._parameter_list[INDEX_SERVO].set_value(index)

    def set_position(self, position):
        self._parameter_list[INDEX_POSITION].set_position(position)

    @staticmethod
    def get_command(id, local_id, position):
        cmd = Cmd_moveServoTo(id)
        cmd.set_index(local_id)
        cmd.set_position(position)
        return cmd


"""		
package de.hska.lat.robot.component.actor.servo.protocol;

import de.hska.lat.comm.remote.RemoteCommand;

import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;






/**
 * command that ping a device, device returns ping response message  
 * @author Oktavian Gniot
 *
 */
public class Cmd_moveServoTo extends RemoteCommand
{
    
    
/**
     * 
     */
    private static final long serialVersionUID = 3564313371574431201L;

    
    
    private static final int INDEX_SERVO = 0;
    private static final int INDEX_POSITION = 1;
    

    protected static final String name = "moveServoTo";
    protected static final String description = "move servo to given position";
    
    
public Cmd_moveServoTo() 
{
    this.add(new RemoteParameterUint8("index","index of servo"));
    this.add(new RemoteParameterServoPosition("position","new servo position"));
}



public Cmd_moveServoTo(int command) 
{
    this();
    this.setId(command);
}


public void setData(int index, float position)
{
    (( RemoteParameterUint8) this.get(Cmd_moveServoTo.INDEX_SERVO)).setValue(index);
    (( RemoteParameterServoPosition) this.get(Cmd_moveServoTo.INDEX_POSITION)).setPosition(position);
}



public int getIndex()
{
    return((( RemoteParameterUint8) this.get(Cmd_moveServoTo.INDEX_SERVO)).getValue());
}

public float getPosition()
{
    return((( RemoteParameterServoPosition) this.get(Cmd_moveServoTo.INDEX_POSITION)).getPosition());
}


@Override
public String getName() 
{
    return(Cmd_moveServoTo.name);
}


@Override
public String getDescription() 
{
    return(Cmd_moveServoTo.description);
}



public static Cmd_moveServoTo getCommand(int command)
{
    Cmd_moveServoTo cmd;
    cmd = new Cmd_moveServoTo(command);
    
    return(cmd);
}

public static Cmd_moveServoTo getCommand(int command,int index, float position)
{
    Cmd_moveServoTo cmd;
    cmd = Cmd_moveServoTo.getCommand(command);
    cmd.setData(index, position);
    
    return(cmd);
}


}
"""
