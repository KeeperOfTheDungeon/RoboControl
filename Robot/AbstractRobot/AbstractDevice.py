from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage

class AbstractRobotDevice:
	

	#_transmitter = 
	  #protected LinkedList <N> eventListener = new LinkedList <N>();

		#protected DataAquisator [] aquisators;  
	def __init__(self, device_meta_data):
		self._device_name = device_meta_data.get_name()
		self._id = device_meta_data.get_id()
		self._event_listener = list()

	def set_transmitter(self, transmitter):
		self._transmitter = transmitter

	def add_event_listener(self, listener):
		self._event_listener.append(listener)

	def get_device_name(self):
		return self._device_name	

	def add_component_set(self, component_set):
		self._set_list.append(component_set)
		for component in component_set:
			self._component_list.append(component)



	def send_data(self, remote_data):
		remote_data.set_destination(self._id)
		self._transmitter.send_data(remote_data)




	def remote_ping_device():
#		cmd_ping = CmdPing()
#		cmd_ping
#		self.send_data()
		pass

"""	

@Override
public boolean remote_pingDevice() 
{
	return(this.sendData(Cmd_ping.getCommand(DeviceProtocol.CMD_PING)));	
	
}



}

/**
 * 
 * @author Tavin
 *
 * 
 *
 * @param <S> sensor listener interface  for this device
 * @param <P>
 */

public abstract class RobotDevice <N extends DeviceEventNotifier, P extends DeviceProtocol> extends AbstractRobotDevice<RobotComponent<?,?,?>,P> 
		implements ControlInterface 
{

public RobotDevice(String name,int id)
{
	this.name=name;
	this.id=id;
	this.transmitter = null;
}


public RobotDevice(DeviceMetaData metaData)
{
	this.name=metaData.getDeviceName();
	this.id=metaData.getDeviceId();

}





/**
 * remove an event listener 
 * @param listener to be removed from listener list
 */
public void removeEventListener(N listener)
{
	this.eventListener.remove(listener);
}





public DataAquisator [] getAquisators()
{
	return(this.aquisators);
}




/**
 * 
 */
public void loadSetup()
{
	for (RobotComponent<?,?,?> component : this.componentList)
	{
		component.remote_loadDefaults();
		component.remote_getSettings();
	}
}


/**
 * called when connection to remote robot succeeded
 */
public void onConnected()
{
	this.loadSetup();
	for (RobotComponent<?,?,?> component: this.componentList)
	{
		component.onConnected();
	}
}

/**
 * called when disconnecting form a remote robot
 */

public void onDisconnected()
{
	for (RobotComponent<?,?,?> component: this.componentList)
	{
		component.onConnected();
	}
}

/**
 * a ping response message was received, notify all listeners
 * @param remoteMessage
 */
protected void processPingResponse(Msg_pingResponse remoteMessage)
{
	for (N listener : this.eventListener)
	{
		listener.pingReceived(this);
	}
	
}



@Override
public boolean remote_startStreamData(int index, int period)
{
	
	return(this.sendData(Cmd_startStreamData.getCommand(DeviceProtocol.CMD_START_STREAM_DATA,index, period)));
}


@Override
public boolean remote_stopStreamData(int index) 
{
	return(this.sendData(Cmd_stopStreamData.getCommand(DeviceProtocol.CMD_STOP_STREAM_DATA,index)));	
}


@Override
public boolean remote_clearAllDataStreams() 
{
	return(this.sendData(Cmd_clearAllDataStreams.getCommand(DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS)));	
}


@Override
public boolean remote_pauseAllDataStreams() 
{
	return(this.sendData(Cmd_pauseAllDataStreams.getCommand(DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS)));	
}



@Override
public boolean remote_continueAllDataStreams() 
{
	return(this.sendData(Cmd_continueAllDataStreams.getCommand(DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS)));	
}


@Override
public boolean remote_saveStreams() 
{
	return(this.sendData(Cmd_saveDataStreams.getCommand(DeviceProtocol.CMD_SAVE_STREAMS)));	
}

@Override
public boolean remote_loadStreams() 
{
	return(this.sendData(Cmd_loadDataStreams.getCommand(DeviceProtocol.CMD_LOAD_STREAMS)));	
}









@Override
public boolean remote_getNextError() 
{
	return(this.sendData(Cmd_getNextError.getCommand(DeviceProtocol.CMD_GET_NEXT_ERROR)));	
}



@Override
public boolean remote_getErrorCount() 
{
	return(this.sendData(Cmd_getErrorCount.getCommand(DeviceProtocol.CMD_GET_ERROR_COUNT)));	
}




@Override
public boolean remote_clearComStatistics() 
{
	return(this.sendData(Cmd_clearComStatistics.getCommand(DeviceProtocol.CMD_CLEAR_COM_STATISTICS)));	
}



@Override
public boolean remote_clearCpuStatistics() 
{
	return(this.sendData(Cmd_clearCpuStatistics.getCommand(DeviceProtocol.CMD_CLEAR_CPU_STATISTICS)));	
}



@Override
public boolean decodeStream(RemoteStream remoteStreamData)
{
	
	if (remoteStreamData instanceof Stream_cpuStatistics)
	{
		this.cpuStatus.processCpuStatusMessage((Stream_cpuStatistics) remoteStreamData);
		return(true);
	}
	else if (remoteStreamData instanceof Stream_comStatistics)
	{
		this.comStatus.processComStatusMessage((Stream_comStatistics) remoteStreamData);
		return(true);
	}
	
	return(false);
}



@Override
public boolean decodeMessage(RemoteMessage remoteMessage)
{
	
	if (remoteMessage instanceof Msg_pingResponse)
	{
		this.processPingResponse((Msg_pingResponse) remoteMessage);
		return(true);
	}

	
	return(false);
}




}
"""