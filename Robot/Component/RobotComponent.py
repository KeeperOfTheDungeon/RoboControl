from RoboControl.Robot.AbstractRobot.AbstractComponent import AbstractComponent
from RoboControl.Robot.Component.ComponentProtocol import Cmd_getComponentSettings
from RoboControl.Robot.Component.ComponentProtocol import Cmd_getComponentValue
from RoboControl.Robot.Component.ComponentProtocol import Cmd_loadComponentDefaults
from RoboControl.Robot.Component.ComponentProtocol import Cmd_saveComponentDefaults


class RobotComponent(AbstractComponent):

    def __init__(self, meta_data):
        super().__init__(meta_data)
        self._setup_listener  = list()
        self._value_listener = list()
        # TODO why here?
        self._sensor_listener = list()
        self._local_id = meta_data["local_id"]
        self._device_address = meta_data["protocol"]["device_id"]

        self.component_protocol = meta_data["protocol"]

        self._cmd_get_settings = self.component_protocol["cmd_getSettings"]
        self._cmd_set_settings = self.component_protocol["cmd_setSettings"]
        self._cmd_save_defaults = self.component_protocol["cmd_saveDefaults"]
        self._cmd_load_defaults = self.component_protocol["cmd_loadDefaults"]
        self._cmd_get_value = self.component_protocol["cmd_getValue"]

    def send_data(self, remote_data):
        remote_data.set_destination_address(self._device_address)
        if self._transmitter is not None:
            self._transmitter.transmitt(remote_data)
        return None

    def remote_load_defaults(self):
        return self.send_data(Cmd_loadComponentDefaults.get_command(self._cmd_save_defaults, self._local_id))

    def remote_save_defaults(self):
        return self.send_data(Cmd_saveComponentDefaults.get_command(self._cmd_load_defaults, self._local_id))

    def remote_get_settings(self):
        return self.send_data(Cmd_getComponentSettings.get_command(self._cmd_get_settings, self._local_id))

    def remote_get_component_value(self):
        return self.send_data(Cmd_getComponentValue.get_command(self._cmd_get_value, self._local_id))

    def on_connected(self):
        pass

    def on_disconnected(self):
        pass

    def get_local_id(self):
        return self._local_id

    def get_device_address(self):
        return self._device_address

    def actualize_now(self):
        return False

    def decode_command(self, remote_data):
        return False

    def decode_message(self, remote_data):
        return False

    def decode_stream(self, remote_data):
        return False

    def decode_exception(self, remote_data):
        return False

    def decode(self, remoteData):
        return False

    def notify_setup_changed(self):
        for listener in self._setup_listener:
            listener.settings_changed(self)

    def add_setup_listener(self, listener) -> None:
        self._setup_listener.append(listener)

    def remove_setup_listener(self, listener) -> None:
        self._setup_listener.remove(listener)

    def add_value_listener(self, listener) -> None:
        self._value_listener.append(listener)

    def remove_value_listener(self, listener) -> None:
        self._value_listener.remove(listener)

    def notify_value_changed(self) -> None:
        for listener in self._value_listener:
            listener.value_changed()

    def get_values(self):
        values = list()

    def add_sensor_listener(self, listener):
        self._sensor_listener.append(listener)


"""
package de.hska.lat.robot.component;

import java.util.ArrayList;

import de.hska.lat.robot.abstractRobot.component.AbstractRobotComponent;
import de.hska.lat.robot.component.protocol.Cmd_getComponentSettings;
import de.hska.lat.robot.component.protocol.Cmd_loadComponentDefaults;
import de.hska.lat.robot.component.protocol.Cmd_saveComponentDefaults;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteDecoder;
import de.hska.lat.comm.remote.RemoteCommand;
import de.hska.lat.comm.remote.RemoteData;
import de.hska.lat.comm.remote.RemoteException;
import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.RemoteStream;



/**
 * 
 * @author Oktavian Gniot
 *
 * @param <I>
 */

public abstract class RobotComponent<I extends ComponentChangeNotifier,S extends ComponentSettingsChangeNotifier, P extends ComponentProtocol> 
						extends AbstractRobotComponent implements  RemoteDecoder
						{


		

	
	

	protected ArrayList <I> sensorListener = new ArrayList <I> ();
	protected ArrayList <S> setupListener = new ArrayList <S> ();


	
	// remove make components independend from device

	
	
	
	protected int localId;
	
	/**
	 * robot   
	 */

	protected int deviceAddres;
	
	protected P componentProtocol;
	
	
protected void notifySetupChanged()
{
	for (S  listener : this.setupListener)
	{
		listener.settingsChanged(this);
	}
}
	
public 	RobotComponent(ComponentMetaData metaData, P protocol )
{
	super(metaData);
	this.localId=metaData.getLocalId();
	this.deviceAddres = metaData.getDeviceId();
	
	this.componentProtocol = protocol;
}
	




/**
 * add given sensor listener to components context
 *  
 * @param sensorListener sensor listener
 */

public void addSensorListener(I sensorListener)
{
	this.sensorListener.add(sensorListener);	
}

/**
 * remove given Sensor listener from components context 
 * 
 * @param sensorListener sensor listener to be removed
 */

public void removeSensorListener(I sensorListener)
{
	this.sensorListener.remove(sensorListener);
}



/**
 * add given setup listener to components context
 *  
 * @param sensorListener setup listener
 */

public void addSetupListener(S setupListener)
{
	this.setupListener.add(setupListener);	
}

/**
 * remove given setup listener from components context 
 * 
 * @param setupListener sensor listener to be removed
 */

public void removeSetupListener(S setupListener)
{
	this.setupListener.remove(setupListener);
}




/**
 * 
 * gets component local id i.e. index in component set messages
 * 
 * @return local component id
 */

public int getLocalId()
{
	return(this.localId);
}



/**
 * gets address of device that contains this component
 * @return device address
 */
public int getDeviceAddres()
{
	return(this.deviceAddres);
}


/**
 * called when connestion to remote robot succed
 */
public void onConnected()
{
}

/**
 * called whwn diconesting form a remote robot
 */

public void onDisconnected()
{
	
}

/**
 * get values of this component. Some components may be composed of more then one value  
 * @return all values of this component
 */

/*
public ArrayList<ComponentValue<?>> getValues()
{
	
	ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();

			
	return (values);
}
*/

/**
 * 
 * @param data
 * @return
 */

protected boolean sendData(RemoteData data)
{
	data.setDestination(this.deviceAddres);
	
	if (this.transmitter == null)
		return(false);
	
	return (this.transmitter.transmitt(data));
}



/**
 * send save default command to remote counterpart
 * @return true if command could be send, false if not
 */

public boolean remote_saveDefaults()
{
	if (this.componentProtocol == null)
		return(false);
	
	
	return(sendData(Cmd_saveComponentDefaults.getCommand(this.componentProtocol.cmdSaveDefaultsId,this.localId)));
}



/**
 * send load default command to remote counterpart
 * @return true if command could be send, false if not
 */

public boolean remote_loadDefaults()
{
	
	if (this.componentProtocol == null)
		return(false);
	
	return(sendData(Cmd_loadComponentDefaults.getCommand(this.componentProtocol.cmdLoadDefaultsId,this.localId)));
}


/**
 * send get setting command to remote counterpart
 * @return true if command could be send, false if not
 */

public boolean remote_getSettings()
{
	if (this.componentProtocol == null)
		return(false);
	
	
	return(sendData(Cmd_getComponentSettings.getCommand(this.componentProtocol.cmdGetSettingsId,this.localId)));
}





/**
 * get actual value(s) from real component. 
 * @return
 *//*
public boolean actualizeNow()
{
	return(false);
}
*/

@Override
public boolean decodeStream(RemoteStream remoteStreamData)
{
	return(false);
}


@Override
public boolean decode(RemoteData remoteData)
{
	return false;
}


@Override
public boolean decodeCommand(RemoteCommand remoteData)
{
	return false;
}


@Override
public boolean decodeMessage(RemoteMessage remoteData)
{
	return false;
}

@Override
public boolean decodeException(RemoteException remoteData)
{
	return false;
}





}

"""