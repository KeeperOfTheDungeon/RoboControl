class AbstractComponent:

	def __init__(self, meta_data):
		self._global_id = meta_data["global_id"]
		self._name = meta_data["name"]


 


"""
package de.hska.lat.robot.abstractRobot.component;

import java.util.ArrayList;

import de.hska.lat.comm.remote.RemoteDataTransmitter;
import de.hska.lat.robot.component.ComponentMetaData;
import de.hska.lat.robot.control.client.ControlClient;
import de.hska.lat.robot.value.ComponentValue;
import de.hska.lat.settings.Settings;

public abstract class AbstractRobotComponent
{

	

	
	protected RemoteDataTransmitter transmitter;
	
	
	protected String instanceKey;
	
	protected Settings settings;
	
	/**
	 * gets name of this component
	 * @return component name
	 */

public AbstractRobotComponent(ComponentMetaData metaData)
{
	this.name=metaData.getName();

	this.globalId=metaData.getGlobalId();
	

	this.instanceKey=this.getClass().getName()+"."+this.globalId;
}


public void setComponentName(String name)
{
	this.name = name;
}
	
public String getComponentName()
{
	return(this.name);
}

/**
 * gets component global id this is the unique id for this component in a Robot
 * @return global id
 */


public int getGlobalId()
{
	return(this.globalId);
}




/**
 * set transmitter for this component. All data will be sent thru this transmitter
 * @param transmitter transmitter
 */
public void setTransmitter(RemoteDataTransmitter transmitter)
{
	this.transmitter = transmitter;
}



/**
 * recover a String value from active settings. This property key will be generated from instance key + local key 
 * @param key local key
 * @param value
 * @return
 */
protected String recoverString(String key, String value)
{
	return(this.settings.recoverString(this.instanceKey+key, value));
}

/**
 * recover a integer value from active settings. This property key will be generated from instance key + local key 
 * @param key local key
 * @param value value
 * @return
 */
protected int recoverInt(String key, int value)
{
	return(this.settings.recoverInt(this.instanceKey+key, value));
}


/**
 * recover a boolean  value from active settings. This property key will be generated from instance key + local key 
 * @param key local key
 * @param value value
 * @return
 */
protected boolean recoverBoolean(String key, boolean value)
{
	return(this.settings.recoverBoolean(this.instanceKey+key, value));
}



/**
 * save a string value in active settings. This property key will be generated from instance key + local key 
 * @param key local key
 * @param value string value to be saved
 */
protected void saveString(String key, String value)
{
	this.settings.saveString(this.instanceKey+key, value);
}


/**
 * save a integer value in active settings. This property key will be generated from instance key + local key 
 * @param key local key
 * @param value integer value to be saved
 */
protected void saveInt(String key, int value)
{
	this.settings.saveInt(this.instanceKey+key, value);
}


/**
 * save a boolean value in active settings. This property key will be generated from instance key + local key 
 * @param key local key
 * @param value boolean value to be saved
 */
protected void saveBoolean(String key, boolean value)
{
	this.settings.saveBoolean(this.instanceKey+key, value);
}



/**
 * get component all data values   
 * @return list with this component data values
 */
public ArrayList<ComponentValue<?>> getDataValues()
{
	
	ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();

			
	return (values);
}



/**
 * get component all control values   
 * @return list with this component control values
 */
public ArrayList<ComponentValue<?>> getControlValues()
{
	
	ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();

			
	return (values);
}







/**
 * get component all control clients   
 * @return list with this component control clients
 */
public ArrayList<ControlClient>  getControlClients()
{
	ArrayList<ControlClient> clients = new ArrayList<ControlClient>();
	return(clients);
}








public void onLoadSettings()
{

	
}



public void onSaveSettings()
{

}


}
"""