from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition
from RoboControl.Robot.Component.generic.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue

SENSOR_INDEX = 0
SERVO_POSITION = 1


class Msg_servoPosition(RemoteMessage):

    def __init__(self, id):
        super().__init__(id, "msg_servoPosition", "actual servo position")
        self._servo_index = 0
        self._servo_position = 0
        self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
        self._parameter_list.append(RemoteParameterServoPosition("position", "servo position"))

    def get_command(id):
        cmd = Msg_servoPosition(id)
        return (cmd)

    def get_index(self):
        return self._parameter_list[SENSOR_INDEX].get_value()

    def get_position(self):
        return self._parameter_list[SERVO_POSITION].get_value()


"""ackage de.hska.lat.robot.component.actor.servo.protocol;

import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;


""""""
/**
 * 
 * @author Oktavian Gniot
 *
 *command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor
 */

public class Msg_servoPosition extends RemoteMessage
{
    
    /**
     * 
     */
    private static final long serialVersionUID = 2638694167468005642L;



    protected static final String name = "servoPosition";
    protected static final String description = "actual servo position";


    private static final int INDEX_SERVO = 0;
    private static final int INDEX_POSITION = 1;
    

public Msg_servoPosition() 
{
    this.add(new RemoteParameterUint8("index","servo index"));
    this.add(new RemoteParameterServoPosition("position","servo position"));
}
    
    
public Msg_servoPosition(int command) 
{
    this();
    this.setId(command);
}


@Override
public String getName() 
{
    return(Msg_servoPosition.name);
}


@Override
public String getDescription() 
{
    return(Msg_servoPosition.description);
}



public void setData(int index, float servoPosition)
{
    (( RemoteParameterUint8) this.get(Msg_servoPosition.INDEX_SERVO)).setValue(index);
    (( RemoteParameterServoPosition) this.get(Msg_servoPosition.INDEX_POSITION)).setPosition(servoPosition);
}


/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */




public static Msg_servoPosition getCommand(int id)
{
    Msg_servoPosition cmd;
    cmd = new Msg_servoPosition(id);
    
    return(cmd);
}



public static Msg_servoPosition getCommand(int command, int index,
        float position)
{

    Msg_servoPosition cmd;
    cmd = Msg_servoPosition.getCommand(command);
    cmd.setData(index, position);
    
    return(cmd);
}


}

"""
