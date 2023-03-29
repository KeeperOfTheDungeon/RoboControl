

from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.generic.distance.protocol.Msg_distance import Msg_distance
from RoboControl.Robot.Component.generic.distance.protocol.Stream_distances import Stream_distances
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor
 

class DistanceSensorSet(ComponentSet):
	def __init__(self, sensors, protocol):
		super().__init__(sensors)
		self._msg_distance = protocol['msg_distance']
		self._stream_distance = protocol['stream_distance']


	def get_command_processors(self):
		command_list = super().get_command_processors()
		return command_list


	def get_message_processors(self):
		msg_list = super().get_message_processors()

		if (self._msg_distance != 0):
			msg_list.append(RemoteProcessor(Msg_distance.get_command(self._msg_distance), self.process_msg_distance))
	
		return msg_list


	def get_stream_processors(self):
		stream_list = super().get_stream_processors()
		
		if (self._stream_distance != 0):
			stream_list.append(RemoteProcessor(Stream_distances.get_command(self._stream_distance,len(self)), self.process_stream_distance))

		return stream_list



	def process_msg_distance(self, remote_data):
		index = remote_data.get_index()
		value = remote_data.get_distance()
		
		if index < len(self):
			self[index].set_distance(value) 


	def process_stream_distance(self, stream_distances):
		
		for sensor in self:
			index = sensor.get_local_id()
			value = stream_distances.get_distance(index)
			sensor.set_distance(value)




	"""def proces_stream_sensor_distances(self, sensor_distances):
		for sensor in self.._s
public void processSensorDistances(Stream_distances sensorDistances) 
{
	T sensor;
	int index;
	

	for (index=0;index<sensorDistances.getParameterCount(); index++)
	{
		sensor=this.getComponentOnLocalId(index);

		if (sensor!=null)
		{
			sensor.setDistance(sensorDistances.getDistance(index));
		}

	}
}
"""

"""package de.hska.lat.robot.component.generic.distance;



import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.robot.component.ComponentSet;
import de.hska.lat.robot.component.generic.distance.protocol.*;




/**
 * Super class for Sharp Gp2 Sensor sets.  
 * 
 * @author Oktavian Gniot
 *
 */
public abstract class DistanceSensorSet<T extends DistanceSensor<?,?>,P extends DistanceSensorProtocol>  extends ComponentSet<T,P>
	{

	
/**
	 * 
	 */
	private static final long serialVersionUID = 1985714891299637009L;

	
/*
public DistanceSensorSet(ArrayList<DetectorMetaData> detectors)
{
	for (DetectorMetaData detector: detectors)
	{
		this.add(new T(detector));
	}
	
}
*/

/**
 * pass actual distances in given message to sensor instances
 * 
 * @param sensorDistances message with actual distances
 * @return array of dirty sensors
 */

public void processSensorDistances(Stream_distances sensorDistances) 
{
	T sensor;
	int index;
	

	for (index=0;index<sensorDistances.getParameterCount(); index++)
	{
		sensor=this.getComponentOnLocalId(index);

		if (sensor!=null)
		{
			sensor.setDistance(sensorDistances.getDistance(index));
		}

	}
}

/**
 * pass sensor distance value to sensor instance
 * @param sensorDistance 
 */

public void processSensorDistance(Msg_distance sensorDistance)
{
	T sensor;
	int index;
	
	index=sensorDistance.getIndex();
	sensor=this.getComponentOnLocalId(index);
	if (sensor!=null)
	{
		sensor.setDistance(sensorDistance.getDistance());	
	}
	
}



@Override
public boolean decodeStream(RemoteStream remoteData)
{
	if (remoteData instanceof Stream_distances)
	{
		processSensorDistances((Stream_distances)remoteData);
	}
	else
	{
		super.decodeStream(remoteData);		
	}
	
	return false;
}


@Override
public boolean decodeMessage(RemoteMessage remoteMessage)
{
	if (remoteMessage instanceof Msg_distance)
	{
		processSensorDistance((Msg_distance)remoteMessage);
	}
	else
	{
		super.decodeMessage(remoteMessage);		
	}
	
	return false;
}

}
"""