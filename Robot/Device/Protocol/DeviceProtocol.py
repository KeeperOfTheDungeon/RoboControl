
from RoboControl.Robot.AbstractRobot.AbstractProtocol import AbstractProtocol
from RoboControl.Robot.Device.Protocol.Cmd_getNodeId import Cmd_getNodeId
from RoboControl.Robot.Device.Protocol.Cmd_ping import Cmd_ping
from RoboControl.Robot.Device.Protocol.Msg_pingResponse import Msg_pingResponse
from RoboControl.Robot.Device.Protocol.Stream_comStatistics import Stream_comStatistics
from RoboControl.Robot.Device.Protocol.Stream_cpuStatistics import Stream_cpuStatistics
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor




CMD_PING						= 0x03

CMD_GET_NODE_ID					= 0x05
	
CMD_GET_COM_STATISTICS			= 0x06
CMD_CLEAR_COM_STATISTICS		= 0x07
	
CMD_GET_CPU_STATISTICS			= 0x08	
CMD_CLEAR_CPU_STATISTICS		= 0x09
	
CMD_GET_NEXT_ERROR				= 0x0A	
CMD_GET_ERROR_COUNT				= 0x0B
	
CMD_START_STREAM_DATA			= 0x10
CMD_STOP_STREAM_DATA			= 0x11
CMD_CLEAR_ALL_DATA_STREAMS		= 0x12
CMD_PAUSE_ALL_DATA_STREAMS		= 0x13
CMD_CONTINUE_ALL_DATA_STREAMS	= 0x14
CMD_SAVE_STREAMS				= 0x15
CMD_LOAD_STREAMS				= 0x16



MSG_PING_RESPONSE				= 0x01
	
MSG_COM_STATUS					= 0x03
MSG_CPU_STATUS					= 0x04

	
STREAM_COM_STATISTICS			= 0x03
STREAM_CPU_STATISTICS			= 0x04

class DeviceProtocol(AbstractProtocol):
        

	def __init__(self, device):
		super().__init__()
		self._device_id	= device.get_id()
		self._device = device
		
	

	#	self._remote_message_processor_list.append(RemoteProcessor(Msg_pingResponse.get_command(),device) )



"""

public DeviceProtocol(AbstractRobotDevice<?,?> device)
{
	this.streamList.add(new RemoteStreamProcessor(new Stream_cpuStatistics(DeviceProtocol.STREAM_CPU_STATISTICS),device));
	this.streamList.add(new RemoteStreamProcessor(new Stream_comStatistics(DeviceProtocol.STREAM_COM_STATISTICS),device));
	

	this.messageList.add(new RemoteMessageProcessor(new Msg_pingResponse(DeviceProtocol.MSG_PING_RESPONSE),device));
	
	
//	this.commandList.add(new RemoteCommandProcessor(new Cmd_pingResponse(DeviceProtocol.MSG_PING_RESPONSE),device)); )
}
	


package de.hska.lat.robot.device.protocol;


import de.hska.lat.agent.device.DeviceAgent;



import de.hska.lat.robot.abstractRobot.device.AbstractRobotDevice;
import de.hska.lat.robot.abstractRobot.device.protocol.AbstractProtocol;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteCommandProcessor;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteMessageProcessor;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteStreamProcessor;



public class DeviceProtocol extends AbstractProtocol
	{

	
	public static final byte MSG_PING_RESPONSE	= 0x01;
	
	public static final byte MSG_COM_STATUS	= 0x03;
	public static final byte MSG_CPU_STATUS	= 0x04;

	
	public static final byte STREAM_COM_STATISTICS	= 0x03;
	public static final byte STREAM_CPU_STATISTICS	= 0x04;
	

	

/*	
	
	protected RemoteCommandProcessorList commandList = new RemoteCommandProcessorList();
	
	protected RemoteStreamDataProcessorList streamDataList = new RemoteStreamDataProcessorList();
	protected RemoteMessageProcessorList messageList = new RemoteMessageProcessorList();
	protected RemoteExceptionProcessorList exceptionList = new RemoteExceptionProcessorList();
	

	*/

	



	

	



/**
 * create default device protocol including all system commands
 * @param device device 
 */

public DeviceProtocol(DeviceAgent<?> device)

{
	this.commandList.add(new RemoteCommandProcessor(new Cmd_startStreamData(DeviceProtocol.CMD_START_STREAM_DATA),device));
	this.commandList.add(new RemoteCommandProcessor(new Cmd_stopStreamData(DeviceProtocol.CMD_STOP_STREAM_DATA),device));
	this.commandList.add(new RemoteCommandProcessor(new Cmd_clearAllDataStreams(DeviceProtocol.CMD_CLEAR_ALL_DATA_STREAMS),device));
	this.commandList.add(new RemoteCommandProcessor(new Cmd_pauseAllDataStreams(DeviceProtocol.CMD_PAUSE_ALL_DATA_STREAMS),device));	
	this.commandList.add(new RemoteCommandProcessor(new Cmd_continueAllDataStreams(DeviceProtocol.CMD_CONTINUE_ALL_DATA_STREAMS),device));
	this.commandList.add(new RemoteCommandProcessor(new Cmd_saveDataStreams(DeviceProtocol.CMD_SAVE_STREAMS),device));
	this.commandList.add(new RemoteCommandProcessor(new Cmd_loadDataStreams(DeviceProtocol.CMD_LOAD_STREAMS),device));
}
	


//public get


}

"""
	