# disabled for micropython  # from typing import List, Union

from Devices.LegController import LegControllerProtocol
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoStatus import RemoteParameterServoStatus
# from RoboControl.Robot.Component.generic.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue

SENSOR_INDEX = 0
INDEX_SPEED = 1
INDEX_MIN_RANGE = 1
INDEX_MAX_RANGE = 2
INDEX_OFFSET = 3
INDEX_SCALE = 4
INDEX_FLAGS = 5


class Msg_servoSettings(RemoteMessage):
    _parameter_list: "List[Union[RemoteParameterUint8, RemoteParameterUint16, RemoteParameterServoPosition, RemoteParameterServoStatus]]"

    def __init__(self, id: int = LegControllerProtocol.MSG_SERVO_SETTINGS):
        super().__init__(id, "servoSettings", "actual servo settings")
        # self._servo_index = 0
        # self._servo_position = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("min range", "servo min range"))
        self._parameter_list.append(RemoteParameterServoPosition("max range", "servo max range"))
        self._parameter_list.append(RemoteParameterUint16("offset", "servo offset"))
        self._parameter_list.append(RemoteParameterUint16("scale", "servo scale"))
        self._parameter_list.append(RemoteParameterServoStatus("scale", "servo scale"))

    @staticmethod
    def get_command(id):
        return Msg_servoSettings(id)

    def get_index(self):
        return self._parameter_list[SENSOR_INDEX].get_value()

    def get_speed(self):
        return self._parameter_list[INDEX_SPEED].get_value()


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

public class Msg_servoSettings extends RemoteMessage
{
    
    /**
     * 
     */
    private static final long serialVersionUID = 2638694167468005642L;



    protected static final String name = "servoSettints";
    protected static final String description = "set settings for a servo";


    private static final int INDEX_SENSOR 				= 0;
    private static final int INDEX_MIN_RANGE			= 1;
    private static final int INDEX_MAX_RANGE 			= 2;
    private static final int INDEX_OFFSET				= 3;
    private static final int INDEX_SCALE				= 4;
    private static final int INDEX_FLAGS				= 5;
    

public Msg_servoSettings() 
{
    this.add(new RemoteParameterUint8("index","servo index"));
    this.add(new RemoteParameterServoPosition("min range","servo min range "));
    this.add(new RemoteParameterServoPosition("max range","servo max range"));
    this.add(new RemoteParameterUint16("offset","servo offset"));
    this.add(new RemoteParameterUint16("scale","servo scale"));
    this.add(new RemoteParameterServoFlags());
}
    
    
public Msg_servoSettings(int command) 
{
    this();
    this.setId(command);
}


@Override
public String getName() 
{
    return(Msg_servoSettings.name);
}


@Override
public String getDescription() 
{
    return(Msg_servoSettings.description);
}



public void setData(int index, float minRange, float maxRange,int offset, int scale, boolean reverse)
{
    (( RemoteParameterUint8) this.get(Msg_servoSettings.INDEX_SENSOR)).setValue(index);
    (( RemoteParameterServoPosition) this.get(Msg_servoSettings.INDEX_MIN_RANGE)).setPosition(minRange);
    (( RemoteParameterServoPosition) this.get(Msg_servoSettings.INDEX_MAX_RANGE)).setPosition(maxRange);
    (( RemoteParameterUint16) this.get(Msg_servoSettings.INDEX_OFFSET)).setValue(offset);
    (( RemoteParameterUint16) this.get(Msg_servoSettings.INDEX_SCALE)).setValue(scale);
    (( RemoteParameterServoFlags) this.get(Msg_servoSettings.INDEX_FLAGS)).setReverse(true);

}


/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */
public int getIndex()
{
    return((( RemoteParameterUint8) this.get(Msg_servoSettings.INDEX_SENSOR)).getValue());
}


/**
 * get gradient
 * @return gradient 
 */
public float getMinRange()
{
    return((( RemoteParameterServoPosition) this.get(Msg_servoSettings.INDEX_MIN_RANGE)).getPosition());
}


public float getMaxRange()
{
    return((( RemoteParameterServoPosition) this.get(Msg_servoSettings.INDEX_MAX_RANGE)).getPosition());
}


/**
 * get offset
 * @return offset 
 */
public int getOffset()
{
    return((( RemoteParameterUint16) this.get(Msg_servoSettings.INDEX_OFFSET)).getValue());
}

public int getScale()
{
    return((( RemoteParameterUint16) this.get(Msg_servoSettings.INDEX_SCALE)).getValue());
}

public boolean isReverse()
{
    return((( RemoteParameterServoFlags) this.get(Msg_servoSettings.INDEX_FLAGS)).isReverse());
}



public boolean isOn()
{
    return((( RemoteParameterServoFlags) this.get(Msg_servoSettings.INDEX_FLAGS)).isOn());
}



public boolean forceFeedbackisOn()
{
    return((( RemoteParameterServoFlags) this.get(Msg_servoSettings.INDEX_FLAGS)).forceFeedbackisOn());
}


public boolean positionFeedbackisOn()
{
    return((( RemoteParameterServoFlags) this.get(Msg_servoSettings.INDEX_FLAGS)).positionFeedbackisOn());
}


public static Msg_servoSettings getCommand(int id)
{
    Msg_servoSettings cmd;
    cmd = new Msg_servoSettings(id);
    
    return(cmd);
}



public static Msg_servoSettings getCommand(int command,int index, float minRange, float maxRange,int offset, int scale, boolean reverse)
{

    Msg_servoSettings cmd;
    cmd = Msg_servoSettings.getCommand(command);
    cmd.setData(index, minRange, maxRange, offset,scale, reverse);
    
    return(cmd);
}



}

"""
