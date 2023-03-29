
from RoboControl.Robot.Component.Sensor.luxSensor.LuxSensorSet import LuxSensorSet


class Vcnl4000LuxSensorSet(LuxSensorSet):
	def __init__(self, sensor_list, protocol):
		super().__init__(sensor_list, protocol)
		


	def get_command_processors(self):
		command_list = super().get_command_processors()
		return command_list

	def get_message_processors(self):
		msg_list = super().get_message_processors()
		return msg_list


	def get_stream_processors(self):
		stream_list = super().get_stream_processors()
		return stream_list





"""package de.hska.lat.robot.component.sensor.vcnl4000;


import de.hska.lat.robot.component.generic.luxSensor.LuxSensorProtocol;
import de.hska.lat.robot.component.generic.luxSensor.LuxSensorSet;


public class Vcnl4000LuxSensorSet   extends LuxSensorSet<Vcnl4000LuxSensor,LuxSensorProtocol>
{

	/**
	 * 
	 */
	private static final long serialVersionUID = 3606052712894068618L;

public Vcnl4000LuxSensorSet(Vcnl4000Set vcnl4000Set)
{
	for (Vcnl4000 sensor : vcnl4000Set)
	{
		this.add(sensor.getLuxSensor());
	}
}
		
	

}"""
