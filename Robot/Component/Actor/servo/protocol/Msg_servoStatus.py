# disabled for micropython  # from typing import Union, List

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoStatus import RemoteParameterServoStatus
# from RoboControl.Robot.Component.generic.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue

SENSOR_INDEX = 0
INDEX_STATUS = 1


class Msg_servoStatus(RemoteMessage):
    _parameter_list: "List[Union[RemoteParameterUint8, RemoteParameterServoStatus]]"

    def __init__(self, id: int = LegControllerProtocol.MSG_SERVO_STATUS):
        super().__init__(id, "msg_servoStatus", "actual servo status")
        self._servo_index = 0
        self._servo_position = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoStatus("speed", "servo status"))

    @staticmethod
    def get_command(id):
        return Msg_servoStatus(id)

    def get_index(self):
        return self._parameter_list[SENSOR_INDEX].get_value()

    def get_speed(self):
        return self._parameter_list[INDEX_STATUS].get_value()


"""package de.hska.lat.robot.component.actor.servo.protocol;

import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint16;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;



/**
 * 
 * @author Oktavian Gniot
 *
 *command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor
 */

public class Msg_servoStatus extends RemoteMessage
{
    
    /**
     * 
     */
    private static final long serialVersionUID = 2638694167468005642L;



    protected static final String name = "servoSpeed";
    protected static final String description = "actual servo speed";


    private static final int INDEX_SERVO = 0;
    private static final int INDEX_SPEED = 1;
    

public Msg_servoStatus() 
{
    this.add(new RemoteParameterUint8("index","servo index"));
    this.add(new RemoteParameterServoStatus());
}
    
    
public Msg_servoStatus(int command) 
{
    this();
    this.setId(command);
}


@Override
public String getName() 
{
    return(Msg_servoStatus.name);
}


@Override
public String getDescription() 
{
    return(Msg_servoStatus.description);
}



public void setData(int index, boolean isActive, boolean isOn, boolean isReverse, boolean isAtMin, boolean isAtMax, boolean isStalling)
{
    (( RemoteParameterUint8) this.get(Msg_servoStatus.INDEX_SERVO)).setValue(index);
    //(( RemoteParameterServoStatus) this.get(Msg_servoStatus.INDEX_SPEED)).setValue(position);
}


/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */
public int getIndex()
{
    return((( RemoteParameterUint8) this.get(Msg_servoStatus.INDEX_SERVO)).getValue());
}


/**
 * get gradient
 * @return gradient 
 */
public int getSpeed()
{
    return((( RemoteParameterUint16) this.get(Msg_servoStatus.INDEX_SPEED)).getValue());
}





public static Msg_servoStatus getCommand(int id)
{
    Msg_servoStatus cmd;
    cmd = new Msg_servoStatus(id);
    
    return(cmd);
}



public static Msg_servoStatus getCommand(int command, int index,
        boolean isActive, boolean isOn, boolean isReverse, boolean isAtMin, boolean isAtMax, boolean isStalling)
{

    Msg_servoStatus cmd;
    cmd = Msg_servoStatus.getCommand(command);
    cmd.setData(index, isActive,  isOn,  isReverse,  isAtMin,  isAtMax, isStalling);
    
    return(cmd);
}


}

"""
