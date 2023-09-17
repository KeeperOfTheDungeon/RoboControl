from RoboControl.Robot.Component.Actor.servo.Servo import Servo
from RoboControl.Robot.Component.Actor.servo.protocol.Stream_servosDestinations import Stream_servosDestinations
from RoboControl.Robot.Component.Actor.servo.protocol.Stream_servosPositions import Stream_servosPositions
from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor


class ServoSet(ComponentSet):
    def __init__(self, components, protocol):
        # self._msg_distance = protocol['msg_distance']
        self._stream_positions = protocol['stream_servoPositions']
        self._stream_destinations = protocol['stream_servoDestinations']

        actors = list()

        for component in components:
            actor = Servo(component)
            actors.append(actor)

        super().__init__(actors)

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()

        if (self._stream_positions != 0):
            stream_list.append(RemoteProcessor(Stream_servosPositions.get_command(self._stream_positions, len(self)),
                                               self.process_stream_positions))

        if (self._stream_destinations != 0):
            stream_list.append(RemoteProcessor(Stream_servosDestinations.get_command(self._stream_positions, len(self)),
                                               self.process_stream_destinations))

        return stream_list

    """def decode_stream(self, remote_data):
        if isinstance(remote_data,Stream_servosPositions):
            self.process_stream_positions(remote_data)
        if isinstance(remote_data,Stream_servosDestinations):
            self.process_stream_destinations(remote_data)
    """

    def process_stream_positions(self, stream_positions):

        for sensor in self:
            index = sensor.get_local_id()
            value = stream_positions.get_position(index)
            sensor.set_position(value)

    def process_stream_destinations(self, stream_destitions):

        for sensor in self:
            index = sensor.get_local_id()
            value = stream_destitions.get_destination(index)
            sensor.set_destination(value)


"""package de.hska.lat.robot.component.actor.servo;




import de.hska.lat.comm.remote.RemoteMessage;
import de.hska.lat.comm.remote.RemoteStream;
import de.hska.lat.robot.component.ComponentSet;
import de.hska.lat.robot.component.actor.servo.feedbackServo.protocol.Stream_servoRawAnalogPosition;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.Msg_servoForceThreshold;
import de.hska.lat.robot.component.actor.servo.protocol.*;








/**
 * 
 * @author Oktavian Gniot
 *
 * Class contains a list of servos controlled by head controller
 *
 */

public class ServoSet extends ComponentSet<Servo, ServoProtocol> 
        
{


    
    



/**
     * 
     */
    private static final long serialVersionUID = -6296184626671050693L;



protected ServoSet()
{
    
}



public void  processServoSettings(Msg_servoSettings remoteData)
{
    Servo servo;

    
    servo=this.getComponentOnLocalId(remoteData.getIndex());
    if (servo!=null)
    {
        servo.setServoSetup(remoteData.getMinRange(), remoteData.getMaxRange(), 
                remoteData.getOffset(), remoteData.getScale(),
                remoteData.isReverse());
        servo.setOn(remoteData.isOn());
        servo.setForceFeedbackOn(remoteData.forceFeedbackisOn());
        servo.setpositionFeedbackisOn(remoteData.positionFeedbackisOn());
    }

}
    



/**
 * decode servo speed message and sets the new speed value in servo component 
 * 
 * @param servoData DataPacket that contains new servo speed 
 */

public void  processServoSpeed(Msg_servoSpeed remoteData)
{
    Servo servo;

    servo=this.getComponentOnLocalId(remoteData.getIndex());
    if (servo!=null)
    {
        servo.setSpeed(remoteData.getSpeed());
    }
    
}


/**
 * decode servo force threshold message and sets the new force threshold value in servo component 
 * 
 * @param servoData DataPacket that contains new servo speed 
 */

public void  processServoForceThreshold(Msg_servoForceThreshold remoteData)
{
    Servo servo;

    servo=this.getComponentOnLocalId(remoteData.getIndex());
    if (servo!=null)
    {
        servo.setForceThreshold(remoteData.getForceThreshold());
    }
    
}

/**
 * decode servos positions from remoteStreamData
 * 
 * @param servoPositions DataPacket containing positions for all servos in ServoSet
 */
public void processServosPositions(Stream_servosPositions servoPositions)
{
    Servo servo;

    int index;


    for (index=0;index<servoPositions.getParameterCount(); index++)
    {
        servo=this.getComponentOnLocalId(index);
        if (servo!=null)
        {
            servo.setPosition(servoPositions.getPosition(index));
        }
    }

}



public void  processServosDestinations(Stream_servosDestinations servoPosition)
{
    Servo servo;

    int index;


    for (index=0;index<servoPosition.getParameterCount(); index++)
    {
        servo=this.getComponentOnLocalId(index);
        if (servo!=null)
        {
            servo.setDestination(servoPosition.getDestination(index));
            
        }
    }
}


public void  processServosStatus(Stream_servosStatus servosStatus)
{
    Servo servo;
    int index;

    for (index=0;index<servosStatus.getParameterCount(); index++)
    {
        servo=this.getComponentOnLocalId(index);
        
        if (servo!=null)
        {
        servo.setActive(servosStatus.isActive(index));
        servo.setAtMax(servosStatus.isAtMax(index));
        servo.setAtMin(servosStatus.isAtMin(index));
        servo.setStalling(servosStatus.isStalling(index));
        servo.setOn(servosStatus.isOn(index));
        servo.setReverse(servosStatus.isReverse(index));
        }
        
    }
}
/**
 * decode servo position from DataPacket
 *  
 * @param servoPosition DataPacket containing actual servo position
 */

public void  processServoPosition(Msg_servoPosition servoPosition)
{
    Servo servo;


    servo=this.getComponentOnLocalId(servoPosition.getIndex());
    if (servo!=null)
    {
        servo.setPosition(servoPosition.getPosition());
    }
    
}


private void processServosRawAnalogValues(
        Stream_servoRawAnalogPosition rawAnalogValues)
{

    int index;

    for (index=0;index<rawAnalogValues.getParameterCount(); index++)
    {
        System.out.println ("Servo : "+index+"  Value : "+rawAnalogValues.getPosition(index));
        
    }
    
}



@Override
public boolean decodeStream(RemoteStream remoteData)
{
    if (remoteData instanceof Stream_servosPositions)
    {
        processServosPositions((Stream_servosPositions)remoteData);
    }
    else if (remoteData instanceof Stream_servosDestinations)
    {
        processServosDestinations((Stream_servosDestinations)remoteData);
    }
    else if (remoteData instanceof Stream_servosStatus)
    {
        processServosStatus((Stream_servosStatus)remoteData);
    }
    else if (remoteData instanceof Stream_servoRawAnalogPosition)
    {
        processServosRawAnalogValues((Stream_servoRawAnalogPosition)remoteData);
    }
    
    return false;
}





@Override
public boolean decodeMessage(RemoteMessage remoteData)
{
    if (remoteData instanceof Msg_servoSpeed)
    {
         this.processServoSpeed((Msg_servoSpeed) remoteData);
    }
    else if (remoteData instanceof Msg_servoSpeed)
    {
    //	processServosPositions((Stream_servosPositions)remoteData);
    } 

    
    else if (remoteData instanceof Msg_servoPosition)
    {
        this.processServoPosition((Msg_servoPosition) remoteData);

    } 

    else if (remoteData instanceof Msg_servoSettings)
    {
		this.processServoSettings((Msg_servoSettings) remoteData);
	} 
	
	else if (remoteData instanceof Msg_servoForceThreshold)
	{
		this.processServoForceThreshold((Msg_servoForceThreshold) remoteData );
	}  
	
	
	return false;
}

}"""
