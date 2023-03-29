from RoboControl.Robot.Component.RobotComponent import RobotComponent


class ComponentSet(list):
	def __init__(self, components):
		#self._component_list = list(components)
		self.extend(components)

		pass

	def get_component_on_global_id(self, id):
	#	for component in self._component_list:
	#		if component.
		pass

	def get_component_on_local_id(self, id):
	#	for component in self._component_list:
	#		if component.
		pass

	#def get_all_id


	def get_data_values(self):
		data_values = list()
		for component in self._component_list:
			self._component_list += component.get_values()



	def get_command_processors(self):
		return list()

	def get_message_processors(self):
		return list()

	def get_stream_processors(self):
		return list()










"""package de.hska.lat.robot.component;

import java.util.ArrayList;

import de.hska.lat.comm.remote.RemoteCommand;
import de.hska.lat.comm.remote.RemoteData;
import de.hska.lat.comm.remote.RemoteDataTransmitter;
import de.hska.lat.comm.remote.RemoteException;
import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteDecoder;
import de.hska.lat.robot.value.ComponentValue;




/**
 * Basis class for a list of device components of same type 
 * 
 * @author Oktavian Gniot
 *
 */


public class ComponentSet<T extends RobotComponent<?,?,?>,P extends ComponentProtocol> extends ArrayList<T>
		implements RemoteDecoder
{

	/**
	 * 
	 */
	private static final long serialVersionUID = 4132550575974166030L;

	
	protected RemoteDataTransmitter transmitter;
	
public  ComponentSet()
{
}


/**
 * search for an component with given id
 * 
 * @param id id of component to be found
 * @return component wit given id or null
 */

public T getComponentOnGlobalId(int id)
{

	
	for (T component : this)
	{
		if (component.getGlobalId()==id)
			return(component);
	}

	return(null);
}

/**
 * find component with given id in this set
 * @param id components id
 * @return component or null if a component with this id does not exists
 */

public T getComponentOnLocalId(int id)
{

	
	for (T component : this)
	{
		if (component.getLocalId()==id)
			return(component);
	}

	return(null);
}


/**
 * get ids of all components in this set
 * @return ids array with ids of components
 */

public int[] getIds()
{
	
	int ids [] = new int[this.size()];
	int index;
	
	for(index=0;index<this.size();index++)
	{
		ids[index]=this.get(index).getGlobalId();
	}

	
	return (ids);
}



/**
 *  
 */

public void loadSettings()
{
	for (T sensor : this)
	{
		sensor.remote_loadDefaults();
		sensor.remote_getSettings();
	}
}



/**
 * returns an array list with all components of this set
 * @return list with all components in this set
 */
public ArrayList<T> getComponents()
{
	ArrayList<T> componentList = new ArrayList<T>();
	
	for(T component : this)
	{
		componentList.add(component);
	}
		
	return(componentList);
}



public void setTransmitter(RemoteDataTransmitter transmitter)
{
	this.transmitter = transmitter;
	
	for (T component : this)
	{
		component.setTransmitter(transmitter);
	}
	
}




}
"""