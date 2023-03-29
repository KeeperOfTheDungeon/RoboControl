from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Actor.servo.protocol.RemoteParameterServoPosition import RemoteParameterServoPosition
from RoboControl.Robot.Component.generic.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue


SENSOR_INDEX = 0
INDEX_SPEED = 1

class Msg_servoSpeed(RemoteMessage):

	def __init__(self, id):
		super().__init__(id, "msg_servoSpeed", "actual servo speed")
		#self._servo_index = 0
		#self._servo_position = 0
		self._parameter_list.append(RemoteParameterUint8("index", "servo index"))
		self._parameter_list.append(RemoteParameterUint16("speed","servo speed"))


	def get_command(id):
		cmd = Msg_servoSpeed(id)
		return (cmd)


	def get_index(self):
		return self._parameter_list[SENSOR_INDEX].get_value()


	def get_speed(self):
		return self._parameter_list[INDEX_SPEED].get_value()



"""


public void setData(int index, int position)
{
	(( RemoteParameterUint8) this.get(Msg_servoSpeed.INDEX_SERVO)).setValue(index);
	(( RemoteParameterUint16) this.get(Msg_servoSpeed.INDEX_SPEED)).setValue(position);
}


/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */
public int getIndex()
{
	return((( RemoteParameterUint8) this.get(Msg_servoSpeed.INDEX_SERVO)).getValue());
}




public static Msg_servoSpeed getCommand(int id)
{
	Msg_servoSpeed cmd;
	cmd = new Msg_servoSpeed(id);
	
	return(cmd);
}



public static Msg_servoSpeed getCommand(int command, int index,
		int speed)
{

	Msg_servoSpeed cmd;
	cmd = Msg_servoSpeed.getCommand(command);
	cmd.setData(index, speed);
	
	return(cmd);
}


}

"""