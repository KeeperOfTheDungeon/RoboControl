from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000 import Vcnl4000
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000DistanceSensorSet import Vcnl4000DistanceSensorSet
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000LuxSensorSet import Vcnl4000LuxSensorSet
from RoboControl.Robot.Component.Sensor.vcnl4000.protocol.Msg_vcnl4000Settings import Msg_vcnl4000Settings

class Vcnl4000Set(ComponentSet):
	def __init__(self, components, protocol):

		lux_sensors = list()
		distance_semsors = list()
		vcnl_sensors = list()

		for component in components:
			sensor = Vcnl4000(component)
			vcnl_sensors.append(sensor)
			lux_sensors.append(sensor.get_lux_sensor())
			distance_semsors.append(sensor.get_distance_sensor())

		super().__init__(vcnl_sensors)

		
		protocol["cmd_getValue"] = protocol["cmd_getLux"]
		self._lux_sensor_set = Vcnl4000LuxSensorSet(lux_sensors, protocol)

		protocol["cmd_getValue"] = protocol["cmd_getDistance"]
		self._distance_sensor_set = Vcnl4000DistanceSensorSet(distance_semsors, protocol)
		


	def get_distance_sensor(self):
		return self._distance_sensor
		




	def get_lux_sensors(self):
		return self._lux_sensor_set

	def get_distance_sensors(self):
		return self._lux_distance_ensor_set


	
	def process_settings(settings):
		if isinstance(settings,  Msg_vcnl4000Settings):
			pass



	def get_command_processors(self):
		command_list = super().get_command_processors()
		command_list.extend(self._lux_sensor_set.get_command_processors())
		command_list.extend(self._distance_sensor_set.get_command_processors())
	
		return command_list


	def get_message_processors(self):
		msg_list = super().get_message_processors()
		msg_list.extend(self._lux_sensor_set.get_message_processors())
		msg_list.extend(self._distance_sensor_set.get_message_processors())

		return msg_list


	def get_stream_processors(self):
		stream_list = super().get_stream_processors()
		stream_list.extend(self._lux_sensor_set.get_stream_processors())
		stream_list.extend(self._distance_sensor_set.get_stream_processors())
	
		return stream_list





"""
private void processSettings(Msg_vcnl4000Settings remoteMessage)
{
	Vcnl4000 sensor;
	int index;
	
	index=remoteMessage.getIndex();
	sensor=this.getComponentOnLocalId(index);
	if (sensor!=null)
	{
		
		sensor.setSettings(
		remoteMessage.getIrCurrent(),
		remoteMessage.getAveragingMode(),
		remoteMessage.getProximityFrequency(),
		remoteMessage.getAutoConversion(),
		remoteMessage.getAutoCompensation()
		);
	
	}
}
"""
	

"""package de.hska.lat.robot.component.sensor.vcnl4000;



import java.util.ArrayList;



import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.robot.component.ComponentSet;
import de.hska.lat.robot.component.detector.DetectorMetaData;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Msg_vcnl4000Settings;



/**
 * Super class for Vcnl 4000 Sensor sets.  
 * 
 * @author Oktavian Gniot
 *
 */
public class Vcnl4000Set  extends ComponentSet<Vcnl4000, Vcnl4000Protocol>
{



	
/**
	 * 
	 */
	private static final long serialVersionUID = 7626423114169877335L;



public Vcnl4000Set()
{
	
}
	
	
	
public Vcnl4000Set(ArrayList<DetectorMetaData> detectors,Vcnl4000Protocol protocol)
{
	
	
	for (DetectorMetaData detector: detectors)
	{
		this.add(new Vcnl4000(detector,protocol));
	}
	
	this.luxSensorSet = new Vcnl4000LuxSensorSet(this);
	this.distanceSensorSet = new Vcnl4000DistanceSensorSet(this);
	
}


protected void init()
{
	this.luxSensorSet = new Vcnl4000LuxSensorSet(this);
	this.distanceSensorSet = new Vcnl4000DistanceSensorSet(this);
}






@Override
public boolean decodeMessage(RemoteMessage remoteData)
{
	if (remoteData instanceof Msg_vcnl4000Settings)
	{
		this.processSettings((Msg_vcnl4000Settings)remoteData);
	}


	return false;
}




}
"""
