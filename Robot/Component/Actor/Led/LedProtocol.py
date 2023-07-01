from RoboControl.Robot.Component.Actor.ActorProtocol import ActorProtocol


class LedProtocol(ActorProtocol):
	pass

"""


/**
 * get led command processors
 * @param remoteDecoder barometric sensor set
 * @return commands processors for barometric sensor
 */

public ArrayList<RemoteCommandProcessor> getCommandProcessors(RemoteDecoder remoteDecoder)	
{
	
	ArrayList<RemoteCommandProcessor> commands = super.getCommandProcessors(remoteDecoder);
	
	commands.add(new RemoteCommandProcessor(
			new Cmd_setLedBrightness(this.cmdSetValueId), 
			remoteDecoder));
	
	commands.add(new RemoteCommandProcessor(
			new Cmd_getLedBrightness(this.cmdGetValueId), 
			remoteDecoder));
	
	return(commands);
}
	
/**
 * get led stream processors
 * @param remoteDecoder  led set
 * @return stream processors for led
 */

public ArrayList<RemoteStreamProcessor> getStreamProcessors(RemoteDecoder remoteDecoder)
{
	
	ArrayList<RemoteStreamProcessor> streams =super.getStreamProcessors(remoteDecoder);
	
	/*
	streams.add(new RemoteStreamProcessor(
			new Stream_barometricPresures(this.streamValuesId), 
			sensor));
	*/
	
	return (streams);
	
}

/**
 * get led message processors
 * @param remoteDecoder led set
 * @return message processors for led
 */

public ArrayList<RemoteMessageProcessor> getMessageProcessors(RemoteDecoder remoteDecoder)
{
	
	ArrayList<RemoteMessageProcessor> messages = super.getMessageProcessors(remoteDecoder);
	
	/*
	messages.add(new RemoteMessageProcessor(
			new Msg_ledBrightnes(this.msgValueId), 
			sensorSet));
	*/
	
	return (messages);
}	

}"""