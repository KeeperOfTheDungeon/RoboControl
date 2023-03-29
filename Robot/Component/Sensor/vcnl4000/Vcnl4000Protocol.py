
from RoboControl.Robot.Component.ComponentProtocol import ComponentProtocol


class Vcnl4000Protocol(ComponentProtocol):
	def __init__(self, protocol):
		super()._init__(protocol)

			
	


"""package de.hska.lat.robot.component.sensor.vcnl4000;


import java.util.ArrayList;

import de.hska.lat.robot.component.ComponentProtocol;
import de.hska.lat.robot.component.generic.distance.DistanceSensorProtocol;
import de.hska.lat.robot.component.generic.luxSensor.LuxSensorProtocol;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Cmd_getVcnl4000DistanceTable;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Cmd_getVcnl4000RawProximity;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Cmd_setVcnl4000DistanceTable;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Msg_vcnl4000DistanceTable;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Msg_vcnl4000RawProximity;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Msg_vcnl4000Settings;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteCommandProcessor;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteMessageProcessor;
import de.hska.lat.robot.device.device.remoteProcessor.RemoteStreamProcessor;


public class Vcnl4000Protocol extends ComponentProtocol
{

	
	public final LuxSensorProtocol luxProtocol;
	public final DistanceSensorProtocol distanceProtocol;
	
	public final int cmdGetRawProximityId;
	public final int cmdSetDistanceTableId;
	public final int cmdGetDistanceTableId;
	
	public final int msgRawProximityId;
	public final int msgDistanceTableId;
	
	
public Vcnl4000Protocol(int deviceId,
		int cmdSetSettingsId,
		int cmdGetSettingsId,
		int cmdSaveDefaultsId,
		int cmdLoadDefaultsId,
		int msgSettingsId,
		
		int cmdGetLuxId,
		int msgLuxId,
		int streamLuxId,
		
		int cmdGetDistanceId,
		int msgDistanceId,
		int streamDistanceId,
		
		int cmdGetRawProximityId,
		int msgRawProximityId,
		
		int cmdSetDistanceTableId,
		int cmdGetDistanceTableId,
		int msgDistanceTableId
		)
{
	super(deviceId,
			cmdSetSettingsId,
			cmdGetSettingsId,
			cmdSaveDefaultsId,
			cmdLoadDefaultsId,
			msgSettingsId
			);
	
	

	

	this.luxProtocol = new LuxSensorProtocol(deviceId,
			cmdSetSettingsId,
			cmdGetSettingsId,
			cmdSaveDefaultsId,
			cmdLoadDefaultsId,
			msgSettingsId,
			
			cmdGetLuxId,
			msgLuxId,
			streamLuxId);
	
	
	this.distanceProtocol = new DistanceSensorProtocol(deviceId,
			cmdSetSettingsId,
			cmdGetSettingsId,
			cmdSaveDefaultsId,
			cmdLoadDefaultsId,
			msgSettingsId,
			
			cmdGetDistanceId,
			msgDistanceId,
			streamDistanceId
			);
	
	
	this.cmdGetRawProximityId = cmdGetRawProximityId;
	this.msgRawProximityId = msgRawProximityId; 
	
	this.cmdSetDistanceTableId = cmdSetDistanceTableId;
	this.cmdGetDistanceTableId = cmdGetDistanceTableId;
	this.msgDistanceTableId = msgDistanceTableId;
	
}





/**
 * get VCNL4000 sensor command processors
 * @param sensorSet VCNL4000 sensor set
 * @return commands processors for VCNL4000 sensor
 */

public ArrayList<RemoteCommandProcessor> getCommandProcessors(Vcnl4000Set sensorSet)	
{
	
	ArrayList<RemoteCommandProcessor> commands = new ArrayList<RemoteCommandProcessor>();
	
	commands.addAll(this.luxProtocol.getCommandProcessors(sensorSet.getLuxSensors()));
	commands.addAll(this.distanceProtocol.getCommandProcessors(sensorSet.getDistanceSensors()));

	commands.add(new RemoteCommandProcessor(
			new Cmd_getVcnl4000RawProximity(this.cmdGetRawProximityId), 
			sensorSet));
	
	commands.add(new RemoteCommandProcessor(
			new Cmd_setVcnl4000DistanceTable(this.cmdGetDistanceTableId), 
			sensorSet));
	
	commands.add(new RemoteCommandProcessor(
			new Cmd_getVcnl4000DistanceTable(this.cmdSetDistanceTableId), 
			sensorSet));
	
	return(commands);
}
	
/**
 * get VCNL4000 sensor stream processors
 * @param sensor  VCNL4000 sensor set
 * @return stream processors for VCNL4000 sensor
 */

public ArrayList<RemoteStreamProcessor> getStreamProcessors(Vcnl4000Set sensorSet)
{
	
	ArrayList<RemoteStreamProcessor> streams = new ArrayList<RemoteStreamProcessor>();
	
	streams.addAll(this.luxProtocol.getStreamProcessors(sensorSet.getLuxSensors()));
	streams.addAll(this.distanceProtocol.getStreamProcessors(sensorSet.getDistanceSensors()));
	
	return (streams);
	
}

/**
 * get VCNL4000 sensor message processors
 * @param sensor  VCNL4000 sensor set
 * @return message processors for VCNL4000 sensor
 */

public ArrayList<RemoteMessageProcessor> getMessageProcessors(Vcnl4000Set sensorSet)
{
	
	ArrayList<RemoteMessageProcessor> messages = new ArrayList<RemoteMessageProcessor>();
	
	messages.addAll(this.luxProtocol.getMessageProcessors(sensorSet.getLuxSensors()));
	messages.addAll(this.distanceProtocol.getMessageProcessors(sensorSet.getDistanceSensors()));
	
	
	messages.add(new RemoteMessageProcessor(
			new Msg_vcnl4000Settings(this.msgSettingsId), 
			sensorSet));
	
	messages.add(new RemoteMessageProcessor(
			new Msg_vcnl4000RawProximity(this.msgRawProximityId), 
			sensorSet.getDistanceSensors()));
	
	messages.add(new RemoteMessageProcessor(
			new Msg_vcnl4000DistanceTable(this.msgDistanceTableId), 
			sensorSet.getDistanceSensors()));
	
	return (messages);
}	



}
"""