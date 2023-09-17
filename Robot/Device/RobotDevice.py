from RoboControl.Robot.AbstractRobot.AbstractRobotDevice import AbstractRobotDevice
from RoboControl.Robot.Device.Protocol import DeviceProtocol
from RoboControl.Robot.Device.Protocol.Cmd_clearAllDataStreams import Cmd_clearAllDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_clearComStatistics import Cmd_clearComStatistics
from RoboControl.Robot.Device.Protocol.Cmd_clearCpuStatistics import Cmd_clearCpuStatistics
from RoboControl.Robot.Device.Protocol.Cmd_continueAllDataStreams import Cmd_continueAllDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_getNodeId import Cmd_getNodeId

from RoboControl.Robot.Device.Protocol.Cmd_loadDataStreams import Cmd_loadDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_pauseAllDataStreams import Cmd_pauseAllDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_ping import Cmd_ping
from RoboControl.Robot.Device.Protocol.Cmd_saveDataStreams import Cmd_saveDataStreams
from RoboControl.Robot.Device.Protocol.Cmd_startStreamData import Cmd_startStreamData
from RoboControl.Robot.Device.Protocol.Cmd_stopStreamData import Cmd_stopStreamData
from RoboControl.Robot.Device.Protocol.Msg_pingResponse import Msg_pingResponse
from RoboControl.Robot.Device.Protocol.Stream_comStatistics import Stream_comStatistics
from RoboControl.Robot.Device.Protocol.Stream_cpuStatistics import Stream_cpuStatistics

from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor


# from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
# from RoboControl.Com.Remote.RemoteMessage import RemoteMessage


class RobotDevice(AbstractRobotDevice):

    def __init__(self, component_config):
        super().__init__(component_config)
        self.build()

    # self.build_protocol()

    def get_data_aquisators(self):
        aquisators = ["cpu status", "com ststus"]
        return aquisators


    def build_protocol(self):
        stream = Stream_comStatistics(DeviceProtocol.STREAM_COM_STATISTICS)
        handler = self._com_status.process_com_status_message
        processor = RemoteProcessor(stream, handler)
        self._remote_stream_processor_list.append(processor)

        stream = Stream_cpuStatistics(DeviceProtocol.STREAM_CPU_STATISTICS)
        handler = self._cpu_status.process_cpu_status_message
        processor = RemoteProcessor(stream, handler)
        self._remote_stream_processor_list.append(processor)

        command = Cmd_ping(DeviceProtocol.CMD_PING)
        handler = self.process_ping_command
        processor = RemoteProcessor(command, handler)
        self._remote_command_processor_list.append(processor)

        command = Cmd_getNodeId(DeviceProtocol.CMD_GET_NODE_ID)
        handler = self.process_Node_id_command
        processor = RemoteProcessor(command, handler)
        self._remote_command_processor_list.append(processor)

        message = Msg_pingResponse(DeviceProtocol.MSG_PING_RESPONSE)
        handler = self.process_ping_response
        processor = RemoteProcessor(message, handler)
        self._remote_message_processor_list.append(processor)

        """
        this.commandList.add(new RemoteCommandProcessor(new Cmd_startStreamData(DeviceProtocol.CMD_START_STREAM_DATA),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_stopStreamData(DeviceProtocol.CMD_STOP_STREAM_DATA),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_clearAllDataStreams(DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_pauseAllDataStreams(DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS),device));	
        this.commandList.add(new RemoteCommandProcessor(new Cmd_continueAllDataStreams(DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_saveDataStreams(DeviceProtocol.CMD_SAVE_STREAMS),device));
        this.commandList.add(new RemoteCommandProcessor(new Cmd_loadDataStreams(DeviceProtocol.CMD_LOAD_STREAMS),device));
        """

    # remote commands

    def remote_ping_device(self):
        cmd = Cmd_ping.get_command(DeviceProtocol.CMD_PING)
        self.send_data(cmd)

    def remote_continue_streams(self):
        cmd = Cmd_continueAllDataStreams.get_command()
        self.send_data(cmd)

    def remote_pause_streams(self):
        cmd = Cmd_pauseAllDataStreams.get_command()
        self.send_data(cmd)

    def remote_clear_streams(self):
        cmd = Cmd_clearAllDataStreams.get_command()
        self.send_data(cmd)

    def remote_save_streams(self):
        cmd = Cmd_saveDataStreams.get_command()
        self.send_data(cmd)

    def remote_load_streams(self):
        cmd = Cmd_loadDataStreams.get_command()
        self.send_data(cmd)

    def remote_start_stream(self, index, period):
        cmd = Cmd_startStreamData.get_command(index, period)
        self.send_data(cmd)

    def remote_stop_stream(self, index):
        cmd = Cmd_stopStreamData.get_command(index)
        self.send_data(cmd)

    def remote_clear_cpu_statistics(self):
        cmd = Cmd_clearCpuStatistics.get_command()
        self.send_data(cmd)

    def Cmd_clear_com_statistics(self):
        cmd = Cmd_clearComStatistics.get_command()
        self.send_data(cmd)




""" 

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

"""

"""


"""

"""
package de.hska.lat.robot.device;




import java.util.LinkedList;

import de.hska.lat.robot.abstractRobot.device.AbstractRobotDevice;
import de.hska.lat.robot.component.ComponentSet;
import de.hska.lat.robot.component.RobotComponent;


import de.hska.lat.robot.device.protocol.*;

import de.hska.lat.robot.device.control.dataAquisation.DataAquisator;
import de.hska.lat.comm.remote.RemoteData;
import de.hska.lat.comm.remote.RemoteDataTransmitter;
import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.RemoteStream;


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

		
	protected LinkedList <N> eventListener = new LinkedList <N>();
	
	protected DataAquisator [] aquisators;



	
	

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
 * add an event listener
 * @param listener listener to be add to listener list
 */

public void addEventListener(N listener)
{
	this.eventListener.add(listener);
}


/**
 * remove an event listener 
 * @param listener to be removed from listener list
 */
public void removeEventListener(N listener)
{
	this.eventListener.remove(listener);
}



public String getDeviceName() 
{
	return (this.name);
}



public void addComponentSet(ComponentSet<?,?> set)
{
	this.setList.add(set);
	
	for (RobotComponent<?,?,?> component:  set)
	{
		this.componentList.add(component);
	}
	
}


public DataAquisator [] getAquisators()
{
	return(this.aquisators);
}







protected boolean sendData(RemoteData data)
{
	data.setDestination((byte)this.id);
	
	if (this.transmitter==null)
		return(false);
	
	return (this.transmitter.transmitt(data));
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
