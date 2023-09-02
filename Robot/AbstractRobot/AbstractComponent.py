from typing import List

from RoboControl.Robot.Value.ComponentValue import ComponentValue


class AbstractComponent:
    def __init__(self, meta_data):
        self._global_id = meta_data["global_id"]
        self._name = meta_data["name"]
        self._transmitter: "Connection" = None

    def get_name(self):
        return self._name

    get_component_name = get_name

    def set_component_name(self, name: str) -> None:
        self._name = name

    def get_global_id(self) -> int:
        """ "gets component global id this is the unique id for this component in a Robot" """
        return self._global_id

    def set_transmitter(self, transmitter: "Connection"):
        """ set transmitter for this component. All data will be sent thru this transmitter """
        self._transmitter = transmitter

    def get_data_values(self) -> List[ComponentValue]:
        return []  # TODO ??

    def get_control_values(self) -> List[ComponentValue]:
        return []  # TODO ??

    def get_control_clients(self) -> List[ComponentValue]:
        return []  # TODO ??





"""	

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














"""
