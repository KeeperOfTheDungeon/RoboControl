
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Component.Sensor.luxSensor.protocol.Msg_lux import Msg_lux
from RoboControl.Robot.Component.Sensor.luxSensor.protocol.Stream_lux import Stream_lux
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor


class LuxSensorSet(ComponentSet):
	def __init__(self, components, protocol):
		super().__init__(components)
		self._msg_lux = protocol['msg_lux']
		self._stream_lux = protocol['stream_lux']


	def get_command_processors(self):
		command_list = super().get_command_processors()
		return command_list

	def get_message_processors(self):
		msg_list = super().get_message_processors()

		if (self._msg_lux != 0):
			msg_list.append(RemoteProcessor(Msg_lux.get_command(self._msg_lux), self.process_msg_lux))

		return msg_list


	def get_stream_processors(self):
		stream_list = super().get_stream_processors()
		
		if (self._stream_lux != 0):
			stream_list.append(RemoteProcessor(Stream_lux.get_command(self._stream_lux, len(self)), self.process_stream_lux))
		return stream_list


	def process_msg_lux(self, remote_data):
		index = remote_data.get_index()
		value = remote_data.get_lux()
		
		if index < len(self):
			self[index].set_lux(value) 

	def process_stream_lux(self, stream_lux):
		
		for sensor in self:
			index = sensor.get_local_id()
			value = stream_lux.get_lux_Value(index)
			sensor.set_lux(value)

	def process_lux(self, remote_data: Msg_lux) -> None:
		sensor: Sensor = self.get_component_on_local_id(remote_data.get_index())
		if sensor is not None:
			sensor.set_lux(remote_data.get_lux_value())




"""

protected void processLux(Msg_lux remoteData)
{
	T sensor;
	int index;
	
	index = remoteData.getIndex();

	sensor=this.getComponentOnLocalId(index);

	if (sensor!=null)
	{
		sensor.setLux(remoteData.getLuxValue());
	}

	

}

protected void processLuxValues(Stream_lux remoteData)
{
	T sensor;
	int index;
	
	
	for (index=0;index<remoteData.getParameterCount(); index++)
	{
		sensor=this.getComponentOnLocalId(index);

		if (sensor!=null)
		{
			sensor.setLux(remoteData.getLuxValue(index));
		}

	}

}



@Override
public boolean decodeMessage(RemoteMessage remoteData)
{
	if (remoteData instanceof Msg_lux)
	{
		processLux((Msg_lux)remoteData);
	}
	else
	{
		super.decodeMessage(remoteData);		
	}
	
	return false;
}


@Override
public boolean decodeStream(RemoteStream remoteData)
{
	if (remoteData instanceof Stream_lux)
	{
		processLuxValues((Stream_lux)remoteData);
	}
	else
	{
		super.decodeStream(remoteData);		
	}
	return(false);
}



}
"""