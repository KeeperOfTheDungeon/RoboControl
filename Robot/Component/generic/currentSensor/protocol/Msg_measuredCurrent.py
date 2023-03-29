from RoboControl.Com.Remote.Parameter.RemoteParameterUint16 import RemoteParameterUint16
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage



SENSOR_INDEX 	= 0
SENSOR_CURRENT 	= 1

class Msg_measuredCurrent(RemoteMessage):

	def __init__(self, id):
		super().__init__(id, "Msg_measuredCurrent", "measured current drain by this sensor")

		self._parameter_list.append(RemoteParameterUint8("index","current sensor index"))
		self._parameter_list.append(RemoteParameterUint16("drain","measured current drain by this sensor"))


	def get_command(id):
		cmd = Msg_measuredCurrent(id)
		return (cmd)


	def get_index(self):
		return self._parameter_list[SENSOR_INDEX].get_value()


	def get_current(self):
		return self._parameter_list[SENSOR_CURRENT].get_value()


"""package de.hska.lat.robot.component.currentSensor.protocol;

import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint16;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;




public class Msg_measuredCurrent extends RemoteMessage
{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 2638694167468005642L;



	protected static final String name = "currentDrain";
	protected static final String description = " measured current drain by this sensor";


	private static final int INDEX_SENSOR 			= 0;
	private static final int INDEX_DRAIN			= 1;



public Msg_measuredCurrent() 
{
	this.add(new RemoteParameterUint8("index","current sensor index"));
	this.add(new RemoteParameterUint16("drain","measured current drain by this sensor"));

}
	
	
public Msg_measuredCurrent(int command) 
{
	this();
	this.setId(command);
}


@Override
public String getName() 
{
	return(Msg_measuredCurrent.name);
}


@Override
public String getDescription() 
{
	return(Msg_measuredCurrent.description);
}



public void setData(int index, int maxDrain)
{
	(( RemoteParameterUint8) this.get(Msg_measuredCurrent.INDEX_SENSOR)).setValue(index);
	(( RemoteParameterUint16) this.get(Msg_measuredCurrent.INDEX_DRAIN)).setValue(maxDrain);


}


/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */
public int getIndex()
{
	return((( RemoteParameterUint8) this.get(Msg_measuredCurrent.INDEX_SENSOR)).getValue());
}


/**
 * get gradient
 * @return gradient 
 */
public int getDrain()
{
	return((( RemoteParameterUint8) this.get(Msg_measuredCurrent.INDEX_DRAIN)).getValue());
}






public static Msg_measuredCurrent getCommand(int id)
{
	Msg_measuredCurrent cmd;
	cmd = new Msg_measuredCurrent(id);
	
	return(cmd);
}



public static Msg_measuredCurrent getCommand(int command, int index,
		int maxDrain)
{
	Msg_measuredCurrent cmd;
	cmd = Msg_measuredCurrent.getCommand(command);
	cmd.setData(index, maxDrain);
	
	return(cmd);
}


}"""

