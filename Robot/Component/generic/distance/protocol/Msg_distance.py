from RoboControl.Com.Remote.Parameter.RemoteParameterUint24 import RemoteParameterUint24
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage



SENSOR_INDEX = 0
SENSOR_VALUE = 1

class Msg_distance(RemoteMessage):

	def __init__(self, id):
		super().__init__(id, "Msg_distance", "actual distance measured by an distance sensor")



		self._parameter_list.append(RemoteParameterUint8("index","sensor index"))
		self._parameter_list.append(RemoteParameterUint24("distance","distance value in mm"))


	def get_command(id):
		cmd = Msg_distance(id)
		return (cmd)

	def get_index(self):
		return self._parameter_list[SENSOR_INDEX].get_value()


	def get_distance(self):
		return self._parameter_list[SENSOR_VALUE].get_value()



"""
package de.hska.lat.robot.component.generic.distance.protocol;

import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint24;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;



/**
 * 
 * @author Oktavian Gniot
 *
 *command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor
 */

public class Msg_distance extends RemoteMessage
{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 2638694167468005642L;



	protected static final String name = "distance";
	protected static final String description = "actual distance measured by an distance sensor";


	private static final int INDEX_SENSOR = 0;
	private static final int INDEX_DISTANCE = 1;
	

public Msg_distance() 
{
	this.add(new RemoteParameterUint8("index"," sensor index"));
	this.add(new RemoteParameterUint24("distance","ddistance value in mm"));
}
	
	
public Msg_distance(int command) 
{
	this();
	this.setId(command);
}


@Override
public String getName() 
{
	return(Msg_distance.name);
}


@Override
public String getDescription() 
{
	return(Msg_distance.description);
}



public void setData(int index, int value)
{
	(( RemoteParameterUint8) this.get(Msg_distance.INDEX_SENSOR)).setValue(index);
	(( RemoteParameterUint24) this.get(Msg_distance.INDEX_DISTANCE)).setValue(value);
}


/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */
public int getIndex()
{
	return((( RemoteParameterUint8) this.get(Msg_distance.INDEX_SENSOR)).getValue());
}


/**
 * get gradient
 * @return gradient 
 */
public int getDistance()
{
	return((( RemoteParameterUint24) this.get(Msg_distance.INDEX_DISTANCE)).getValue());
}





public static Msg_distance getCommand(int id)
{
	Msg_distance cmd;
	cmd = new Msg_distance(id);
	
	return(cmd);
}



public static Msg_distance getCommand(int command, int index,
		int distance)
{

	Msg_distance cmd;
	cmd = Msg_distance.getCommand(command);
	cmd.setData(index, distance);
	
	return(cmd);
}


}
"""
