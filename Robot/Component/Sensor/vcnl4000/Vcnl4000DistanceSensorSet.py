from RoboControl.Robot.Component.generic.distance.DistanceSensorSet import DistanceSensorSet


class Vcnl4000DistanceSensorSet(DistanceSensorSet):
    def __init__(self, sensors, protocol):
        super().__init__(sensors, protocol)

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        return stream_list


"""package de.hska.lat.robot.component.sensor.vcnl4000;


import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.robot.component.generic.distance.DistanceSensorProtocol;
import de.hska.lat.robot.component.generic.distance.DistanceSensorSet;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Msg_vcnl4000DistanceTable;
import de.hska.lat.robot.component.sensor.vcnl4000.protocol.Msg_vcnl4000RawProximity;



public class Vcnl4000DistanceSensorSet   extends DistanceSensorSet<Vcnl4000DistanceSensor,DistanceSensorProtocol>
{

	/**
	 * 
	 */
	private static final long serialVersionUID = 3606052712894068618L;

public Vcnl4000DistanceSensorSet(Vcnl4000Set vcnl4000Set)
{
	for (Vcnl4000 sensor : vcnl4000Set)
	{
		this.add(sensor.getDistanceSensor());
	}
}
		


private void processDistanceTable(Msg_vcnl4000DistanceTable remoteMessage)
{
	Vcnl4000DistanceSensor sensor;
	int index;
	
	index=remoteMessage.getIndex();
	sensor=this.getComponentOnLocalId(index);
	if (sensor!=null)
	{
		
		sensor.setDistanceTable(remoteMessage.getDistanceTable());
	
	}
}





private void processRawProximity(Msg_vcnl4000RawProximity remoteMessage)
{
	
	Vcnl4000DistanceSensor sensor;
	int index;
	
	index=remoteMessage.getIndex();
	sensor=this.getComponentOnLocalId(index);
	if (sensor!=null)
	{
		
		sensor.setProximityValue(remoteMessage.getProximityValue());
	
	}
	// TODO Auto-generated method stub
	System.out.println("Msg_vcnl4000RawProximity");
}



@Override
public boolean decodeMessage(RemoteMessage remoteData)
{
	if (remoteData instanceof Msg_vcnl4000RawProximity)
	{
		this.processRawProximity((Msg_vcnl4000RawProximity)remoteData);
	}
	else if (remoteData instanceof Msg_vcnl4000DistanceTable)
	{
		this.processDistanceTable((Msg_vcnl4000DistanceTable)remoteData);
	}
	

	return false;
}






}
"""
