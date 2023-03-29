

from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Component.generic.distance.protocol.Cmd_getDistance import Cmd_getDistance

from RoboControl.Robot.Value.distance.DistanceValue import DistanceValue


class DistanceSensor(Sensor):

	def __init__(self, meta_data):
		super().__init__(meta_data)
		self._distance_value = DistanceValue(meta_data)


	def get_distance_value(self):
		return self._distance_value

	def get_distance(self):
		self._distance_value.get_milimeters()


	def set_distance(self, value):
		self._distance_value.set_value(value)


	def remote_get_distance(self):
		cmd = Cmd_getDistance.get_command(self._cmd_get_value , self._local_id)
		self.send_data(cmd)



"""package de.hska.lat.robot.component.generic.distance;


import java.util.ArrayList;

import de.hska.lat.robot.component.ComponentMetaData;

import de.hska.lat.robot.component.ComponentSettingsChangeNotifier;

import de.hska.lat.robot.component.sensor.Sensor;
import de.hska.lat.robot.component.sensor.SensorProtocol;
import de.hska.lat.robot.value.ComponentValue;
import de.hska.lat.robot.value.distance.DistanceValue;



/**
 * 
 * @author Oktavian Gniot
 *
 * basis class for distance sensors, keeps distance values and 3D position of detected object  
 *
 * @param <T> Change notifier 
 * @param <C> Control notifier  
 */

public abstract class DistanceSensor<S extends ComponentSettingsChangeNotifier , P extends SensorProtocol> 
		extends  Sensor <DistanceChangeNotifier,S,P> 
{

	

	
	
	
	protected DistanceValue distance;
	




	
//2012.02.15	
public DistanceSensor(ComponentMetaData metaData, float minRange, float maxRange, float beamWidth, P protocol) 
{
	super(metaData, protocol);
	//TODO this is not correct !!!! 
	
	this.distance = new DistanceValue(this.getComponentName(), minRange, maxRange, beamWidth);
}

public void setDistance(float distance)
{
	
	this.distance.setValue(distance);
	
	for (DistanceChangeNotifier  listener :  sensorListener )
	{
		listener.distanceChanged(this);
	}
}

/**
 * set granularity of sensor distance change messages. 
 * @param granularity new granularity in millimeters
 */

public void setGranularity(float granularity)
{
	this.distance.setGranularity(granularity);
}

/**
 * gets actual granularity of sensor distance change messages
 * @return
 */
public float getGranularity()
{
	return(this.distance.getGranularity());
}

/**
 * returns actual sensor distance in millimeters  
 * @return distance in millimeters
 */
public float getMilimeters()
{
	return (this.distance.getValue());
}


/**
 * returns actual sensor distance in centimeters  
 * @return distance in centimeters
 */

public float getCentimeters()
{
	int distance;
	distance = (int)this.distance.getValue() /10;
	
	return (distance);
}


public DistanceValue getDistanceValue()
{
	return (this.distance);
}


public float getMaxRange()
{
	return(this.distance.getMaxRange());
}

public float getMinRange()
{
	return(this.distance.getMinRange());
}


@Override
public ArrayList<ComponentValue<?>> getDataValues()
{
	
	ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();
	
	values.add(this.distance);	
			
	return (values);
}

public float getBeamWidth()
{
	return(this.distance.getBeamWidth());

}





}
"""