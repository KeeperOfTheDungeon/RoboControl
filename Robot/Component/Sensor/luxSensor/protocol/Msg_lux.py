from typing import List, Union

from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Component.Sensor.luxSensor.protocol.RemoteParameterLuxValue import RemoteParameterLuxValue

INDEX_SENSOR = 0
INDEX_LUX = 1


class Msg_lux(RemoteMessage):
    _parameter_list: List[Union[RemoteParameterUint8, RemoteParameterLuxValue]]

    def __init__(self, id: int):
        super().__init__(id, "luxValue", "actual lux value measured by a light sensor")
        self._sensor_index = 0
        self._sensor_value = 0
        self._parameter_list.append(RemoteParameterUint8("index", "sensor index"))
        self._parameter_list.append(RemoteParameterLuxValue("distance", "light value in lux"))

    def get_command(id):
        cmd = Msg_lux(id)
        return (cmd)

    def get_index(self):
        return self._parameter_list[INDEX_SENSOR].get_value()

    def get_lux(self):
        return self._parameter_list[INDEX_LUX].get_lux()


"""

	

public Msg_lux() 
{
	this.add(new RemoteParameterUint8("index","sensor index"));
	this.add(new RemoteParameterLuxValue("distance","light value in lux"));
}
	
	
public Msg_lux(int command) 
{
	this();
	this.setId(command);
}



public void setData(int index, float value)
{
	(( RemoteParameterUint8) this.get(Msg_lux.INDEX_SENSOR)).setValue(index);
	(( RemoteParameterLuxValue) this.get(Msg_lux.INDEX_LUX)).setValue(value);
}


/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */
public int getIndex()
{
	return((( RemoteParameterUint8) this.get(Msg_lux.INDEX_SENSOR)).getValue());
}



public float getLuxValue()
{
	return((( RemoteParameterLuxValue) this.get(Msg_lux.INDEX_LUX)).getValue());
}





public static Msg_lux getCommand(int id)
{
	Msg_lux cmd;
	cmd = new Msg_lux(id);
	
	return(cmd);
}



public static Msg_lux getCommand(int command, int index,
		int distance)
{

	Msg_lux cmd;
	cmd = Msg_lux.getCommand(command);
	cmd.setData(index, distance);
	
	return(cmd);
}


}"""
