
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Component.Sensor.luxSensor.protocol.Cmd_getLux import Cmd_getLux
from RoboControl.Robot.Value.lux.LuxValue import LuxValue


class LuxSensor(Sensor):
	
	def __init__(self, meta_data):
		super().__init__(meta_data)
		self._lux_value = LuxValue(meta_data)


	def get_lux_value(self):
		return self._lux_value


	def set_lux(self, lux):
		self._lux_value.set_value(lux)

	def remote_get_value(self):
		cmd = Cmd_getLux.get_command(self._cmd_get_value , self._local_id)
		self.send_data(cmd)


"""

public abstract class LuxSensor <S extends ComponentSettingsChangeNotifier , P extends LuxSensorProtocol>
			extends Sensor <LuxChangeNotifier,S,P> 
{

	
	protected LuxValue value;

	
	
	
public LuxSensor(ComponentMetaData metaData, P protocol)
{
	super(metaData, protocol);
	
	this.value= new LuxValue(metaData.getName(),10000);
}




public void setLux(float luxValue)
{
	this.value.setValue(luxValue);
	
	for(LuxChangeNotifier listener :  sensorListener )
	{
		listener.luxValueChanged(this);
	}
}



/**
 * get actual lux value measured by this sensor
 * @return light as lux
 */

public float getLux()
{
	return(this.value.getValue());
}




@Override
public ArrayList<ComponentValue<?>> getDataValues()
{
	
	ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();
	
	values.add(this.getLuxValue());

	
	return (values);
}

}
"""