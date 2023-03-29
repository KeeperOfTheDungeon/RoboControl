class AbstractComponentList:
	def __init__(self):
		pass


	def add_component(self, name, local_id ):
		self._name = name 

"""

package de.hska.lat.robot.abstractRobot.component;

import java.util.ArrayList;

import de.hska.lat.robot.value.ComponentValue;




public class AbstractComponentList<T extends AbstractRobotComponent>  extends ArrayList <T> {



/**
	 * 
	 */
	private static final long serialVersionUID = 4889237517558765138L;

/**
 * search for a component in device with given name 
 * @param name name of the component 
 * @return component or null
 */
public T  getComponentOnName(String name)
{

	for (T component : this)
	{
		if (component.getComponentName().equals(name))
		{
			return(component);
		}
	}
	
	
	return(null);
}
	
/**
 * search for a component in device with given globalId 
 * @param globalId global id of the component 
 * @return component or null
 */

public T getComponentOnGlobalId(int globalId)
{
	
	for (T component : this)
	{
		if (component.getGlobalId()==globalId)
		{
			return(component);
		}
	}
	
	return(null);
}
	
	
public ArrayList<ComponentValue<?>> getDataValues()
{
	
	 ArrayList<ComponentValue<?>> values = new  ArrayList<ComponentValue<?>>();
	
	
		for (T component : this)
		{
			values.addAll(component.getDataValues());
		}
	 
	 
	 return(values);
}
	



public ArrayList<ComponentValue<?>> getControlValues()
{
	
	 ArrayList<ComponentValue<?>> values = new  ArrayList<ComponentValue<?>>();
	
	
		for (T component : this)
		{
			values.addAll(component.getControlValues());
		}
	 
	 
	 return(values);
}

}
"""