
from RoboControl.Robot.Component.RobotComponent import RobotComponent


class Actor(RobotComponent):
	
	def __init__(self, meta_data):
		super().__init__(meta_data)
		

"""

public abstract class Actor<L extends ComponentChangeNotifier,S extends  ComponentSettingsChangeNotifier, P extends  ActorProtocol, C extends ComponentValue<?>> extends RobotComponent<L,S,P> 
{

	
	protected C controlValue;
	
public Actor(ComponentMetaData metaData, P protocol)
{
		super(metaData, protocol);

}



/**
 * return 
 * @return
 */

public C getControlValue()
{
	return(this.controlValue);
}



public abstract boolean remote_getValue();


@Override
public ArrayList<ComponentValue<?>> getControlValues()
{
	
	ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();
	values.add(this.controlValue);
			
	return (values);
}


}
"""