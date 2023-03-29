from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.Parameter.RemoteParameterUint32 import RemoteParameterUint32
from RoboControl.Com.Remote.RemoteStream import RemoteStream


INDEX_TRANSMITTED_MESSAGES = 0 
INDEX_RECEIVED_MESSAGES = 1
INDEX_INVALID_MESSAGES = 2
INDEX_LOST_MESSAGES = 3

class Stream_comStatistics(RemoteStream):
	
	def __init__(self, id):
		super().__init__(id, "comStatus", "status of the com system")

		self._parameter_list.append(RemoteParameterUint32("transmitted","number of transmitted messages"))
		self._parameter_list.append(RemoteParameterUint32("received","number of recived messages thrue this device"))
		self._parameter_list.append(RemoteParameterUint32("invalid","number of invalid messages received thrue this device"))
		self._parameter_list.append(RemoteParameterUint32("lost","number of lost mesages"))
		self._parameter_list.append(RemoteParameterUint32("undeliverable","number of undeliverable mesages"))
		self._parameter_list.append(RemoteParameterUint8("status","actual status of the device com system"))
		

	def get_transmitted_messages_count(self):
		return self._parameter_list[INDEX_TRANSMITTED_MESSAGES].get_value()

	def get_received_messages_count(self):
		return self._parameter_list[INDEX_RECEIVED_MESSAGES].get_value()
	
	def get_invalid_messages_count(self):
		return self._parameter_list[INDEX_INVALID_MESSAGES].get_value()

	def get_lost_messages_count(self):
		return self._parameter_list[INDEX_LOST_MESSAGES].get_value()








"""package de.hska.lat.robot.device.protocol;

import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint32;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;

public class Stream_comStatistics extends RemoteStream
{

	/**
	 * 
	 */
	private static final long serialVersionUID = 6500019264652495992L;

	
	
	private static final int INDEX_TRANSMITTED_MESSAGES		= 0;
	private static final int INDEX_RECEIVED_MESSAGES		= 1;
	private static final int INDEX_INVALID_MESSAGES			= 2;
	private static final int INDEX_LOST_MESSAGES			= 3;
	private static final int INDEX_LOST_UNDELIVERABLE		= 4;
	private static final int INDEX_COM_STATUS				= 5;
	
	protected static final String name = "comStatus";
	protected static final String description = "status of the com system";
	
	
	
	
	
	
public Stream_comStatistics()
{



public Stream_comStatistics(int command)
{
	this();
	this.setId(command);
}


public void setData(int transmitted ,int received,int invalid, int lost, int status, int undeliverable)
{
	(( RemoteParameterUint32) this.get(Stream_comStatistics.INDEX_TRANSMITTED_MESSAGES)).setValue(transmitted);
	(( RemoteParameterUint32) this.get(Stream_comStatistics.INDEX_RECEIVED_MESSAGES)).setValue(received);
	(( RemoteParameterUint32) this.get(Stream_comStatistics.INDEX_INVALID_MESSAGES)).setValue(invalid);
	(( RemoteParameterUint32) this.get(Stream_comStatistics.INDEX_LOST_MESSAGES)).setValue(lost);
	(( RemoteParameterUint32) this.get(Stream_comStatistics.INDEX_LOST_UNDELIVERABLE)).setValue(undeliverable);
	(( RemoteParameterUint8) this.get(Stream_comStatistics.INDEX_COM_STATUS)).setValue(status);
}




public static Stream_comStatistics getCommand(int command)
{
	Stream_comStatistics cmd;
	cmd = new Stream_comStatistics(command);
	
	return(cmd);
}

public static Stream_comStatistics getCommand(int command, int transmitted,int received, int invalid, int lost, int status, int undeliverable)
{
	Stream_comStatistics cmd;
	cmd = Stream_comStatistics.getCommand(command);
	cmd.setData(transmitted, received,invalid ,lost ,status, undeliverable);
	
	return(cmd);
}



}
"""
