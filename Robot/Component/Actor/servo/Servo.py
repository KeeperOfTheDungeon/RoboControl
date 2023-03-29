
from RoboControl.Robot.Component.Actor.Actor import Actor
from RoboControl.Robot.Component.Actor.Led.protocol.Cmd_getLedBrightness import Cmd_getLedBrightness
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_moveServoTo import Cmd_moveServoTo
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_servoOff import Cmd_servoOff
from RoboControl.Robot.Component.Actor.servo.protocol.Cmd_servoOn import Cmd_servoOn
from RoboControl.Robot.Value.servo.ServoDestinationValue import ServoDestinationValue
from RoboControl.Robot.Value.servo.ServoPositionValue import ServoPositionValue
from RoboControl.Robot.Value.servo.ServoVelocityValue import ServoVelocityValue



class Servo(Actor):
	
	def __init__(self, meta_data):
		super().__init__(meta_data)
		self._velocity = ServoVelocityValue(meta_data)
		self._velocity_control = ServoVelocityValue(meta_data)
		self._position = ServoPositionValue(meta_data)
		self._destination = ServoDestinationValue(meta_data)
		self._destination_control = ServoDestinationValue(meta_data)

		protocol = meta_data["protocol"]
		self._cmd_servoOn  = protocol["cmd_servoOn"]
		self._cmd_servoOff  = protocol["cmd_servoOff"]
		self._cmd_moveServoTo  = protocol["cmd_moveServoTo"]

		self._isOn = False
		self._isActive = False
		self._isInreverseMode = False



	def get_min_range(self):
		self._servo_position.get_min_range()


	def set_min_range(self, min_range):
		pass

	def get_max_range(self):
		self._servo_position.get_max_range()

	def set_max_range(self, max_range):
		pass


	def set_position(self, position):
		self._position.set_value(position)



	def set_destination(self, destination):
		self._destination.set_value(destination)


	def get_position_value(self):
		return self._position

	def remote_servo_on(self):
		cmd = Cmd_servoOn.get_command(self._cmd_servoOn, 1 << self._local_id)
		self.send_data(cmd)

	def remote_servo_off(self):
		cmd = Cmd_servoOff.get_command(self._cmd_servoOff, 1 << self._local_id)
		self.send_data(cmd)


	def remote_move_servo_to(self, position):
		cmd = Cmd_moveServoTo.get_command(self._cmd_moveServoTo,  self._local_id, position)
		self.send_data(cmd)

	# move Servo


	

"""

	protected ServoVelocityValue velocityControl;
	protected ServoVelocityValue velocity;
	
	protected ServoDestinationValue destinationControl;
	protected ServoDestinationValue destination;
"""


"""
	def remote_set_brightness(self,brightness):
	#return(sendData(Cmd_setLedBrightness.getCommand(this.componentProtocol.cmdSetValueId,this.localId,brightness)));
		pass	

	def remote_get_value(self):
		cmd = Cmd_getLedBrightness.getCommand(self._componentProtocol.cmd_get_value_id,self._local_id)
		#return(sendData(Cmd_getLedBrightness.getCommand(this.componentProtocol.cmdGetValueId,this.localId)));
"""
"""
package de.hska.lat.robot.component.actor.servo;


import java.util.ArrayList;

import de.hska.lat.robot.component.ComponentMetaData;
import de.hska.lat.robot.component.actor.Actor;
import de.hska.lat.robot.component.actor.servo.feedbackServo.protocol.Cmd_calibrateServo;
import de.hska.lat.robot.component.actor.servo.feedbackServo.protocol.Cmd_positionFeedbackOff;
import de.hska.lat.robot.component.actor.servo.feedbackServo.protocol.Cmd_positionFeedbackOn;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.Cmd_forceFeedbackOff;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.Cmd_forceFeedbackOn;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.Cmd_getServoForceThreshold;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.Cmd_setServoForcePosition;
import de.hska.lat.robot.component.actor.servo.forceFeedback.protocol.Cmd_setServoForceThreshold;
import de.hska.lat.robot.component.actor.servo.protocol.*;
import de.hska.lat.robot.value.ComponentValue;
import de.hska.lat.robot.value.ComponentValueChangeListener;
import de.hska.lat.robot.value.servo.ServoAngleValue;


public abstract class Servo extends Actor<ServoChangeNotifier, ServoSetupChangeNotifier, ServoProtocol, ServoAngleValue> implements ComponentValueChangeListener
{

	
	protected ServoAngleValue value;
		
	


	protected int offset = 800;
	protected int scale = 15707;
	protected int speed;
	protected int forceThreshold;

	protected boolean forceFeedbackisOn = false;
	protected boolean positionFeedbackisOn = false;

	protected boolean stalling = false;

	protected ServoVelocityValue velocityControl;
	protected ServoVelocityValue velocity;
	
	protected ServoDestinationValue destinationControl;
	protected ServoDestinationValue destination;
	
protected Servo(ComponentMetaData metaData, ServoProtocol protocol) 
{
	super(metaData, protocol);
	
	
	this.controlValue = new ServoAngleValue(metaData.getName());
	this.controlValue.addListener(this);
	

	this.value = new ServoAngleValue(metaData.getName());
	this.value.addListener(this);

	
	
	this.velocityControl = new ServoVelocityValue(metaData.getName());
	this.velocityControl.addListener(this);
	
	this.velocity = new ServoVelocityValue(metaData.getName());
	this.velocity.addListener(this);
	
	
	this.destinationControl = new ServoDestinationValue(metaData.getName());
	this.destinationControl.addListener(this);
	
	this.destination = new ServoDestinationValue(metaData.getName());
	this.destination.addListener(this);
	
}



public void setServoSetup(float minRange, float maxRange, 
		int offset, int scale,
			boolean reverse) 
{
	this.value.setRange(minRange, maxRange);

	this.offset = offset;
	this.scale = scale;
	this.reverse = reverse;

	for (ServoSetupChangeNotifier listener : this.setupListener) 
	{
		listener.servoSetupChanged(this);
	}

}




public boolean setSpeed(int speed) 
{
	int index;

	if (this.speed != speed) 
	{
		this.speed = speed;

		
		for (index = 0; index < this.setupListener.size(); index++) 
		{
			this.setupListener.get(index).servoSpeedChanged(this.globalId,
					speed);
		}

		return (true);
	}

	return (false);
}

public boolean setForceThreshold(int threshold) 
{
	int index;

	if (this.forceThreshold != threshold) 
	{
		this.forceThreshold = threshold;

		
		for (index = 0; index < this.setupListener.size(); index++) 
		{
			this.setupListener.get(index).servoForceThresholdChanged(this.globalId,
					threshold);
		}

		return (true);
	}

	return (false);
}

/**
 * Set position of a servo
 * 
 * @param newPosition
 *            new Position of Servo
 */

public void setPosition(float newPosition)
{
	this.value.setValue(newPosition);
}

	/**
	 * get actual position of a servo
	 * 
	 * @return Servo Position
	 */
	/*
	 * public int getPosition() { return(this.s_position); }
	 */

	
	/*
	public float getPositionAsDegree()
	{
		return (this.position.getValue());
	}
*/

public void setDestination(float newDestination){
	
	this.destination.setValue(newDestination);
	
}
	
/**
 * get actual position of this servo in radiant	
 * @return position in radiant
 */

public float getPosition() 
{
	return (this.value.getValue());
}

	
	
public ServoAngleValue getAngleValue() 
{
	return (this.value);
}


/**
 * return this servos velocity control value. Servo movement can be controlled by returned value. 
 * @return servos velocity control value
 */
public ServoVelocityValue getVelocityControlValue()
{
	return(this.velocityControl);
}

/**
 * return this servos destination control value. Servo movement can be controlled by returned value. 
 * @return servos destination control value
 */
public ServoDestinationValue getDestinationControlValue()
{
	return(this.destinationControl);
}

public ServoDestinationValue getDestinationValue()
{
	return this.destination;
}

	/*
	 * public boolean setRealPosition(int newPosition) {
	 * 
	 * if (this.realPosition!=newPosition) { this.realPosition=newPosition;
	 * return(true); }
	 * 
	 * return(false); }
	 */
	/**
	 * get actual position of a servo
	 * 
	 * @return Servo Position
	 */
	/*
	 * public int getRealPosition() { return(this.realPosition); }
	 */

public float getMinRange() 
{
	return (this.value.getMinRange());
}

public float getMaxRange() 
{
	return (this.value.getMaxRange());
}




	public int getOffset() {
		return (this.offset);
	}

	public int getSpeed() {
		return (this.speed);
	}

	
public int getScale()
{

	return (this.scale);
}
	
	

/**
 * get the actual position of this servo in degree
 * @return position in degree
 */
public float getPositionAsDegree()
{
	return (this.value.getPositionAsDegree());
}



public boolean setOn(boolean status) 
{


	if (this.isOn != status) {
		this.isOn = status;
		this.value.setOn(status);

		
	for (ServoChangeNotifier notifier: this.sensorListener )
	{
		notifier.isOn(this);	
	}
		
		return (true);

	}

	return (false);
}

public boolean isOn() 
{
	return (this.isOn);
}

public boolean setForceFeedbackOn(boolean status) 
{


	if (this.forceFeedbackisOn != status) {
		this.forceFeedbackisOn = status;

		
	for (ServoChangeNotifier notifier: this.sensorListener )
	{
		notifier.forceFeedbackOn(this);	
	}
		
		return (true);

	}

	return (false);
}

public boolean forceFeedbackisOn(){
	return this.forceFeedbackisOn;
}


public boolean setpositionFeedbackisOn(boolean status) 
{


	if (this.positionFeedbackisOn != status) {
		this.positionFeedbackisOn = status;

		
	for (ServoChangeNotifier notifier: this.sensorListener )
	{
		notifier.positionFeedbackOn(this);	
	}
		
		return (true);

	}

	return (false);
}

public boolean positionFeedbackisOn()
{
	return this.positionFeedbackisOn;
}





// 2012.2.9
public boolean setAtMin(boolean status) 
{
	if (this.value.isAtMin() != status) 
	{
		this.value.setAtMin(status); 


		for (ServoChangeNotifier notifier: this.sensorListener )
		{
			notifier.isAtMin(this);	
		}	

		return (true);
	}

	return (false);	
}


// 2012.2.9
public boolean isAtMin() 
{
	return (this.value.isAtMin());
}



// 2012.2.9
public boolean setAtMax(boolean status) 
{
	if (this.value.isAtMax() != status) 
	{
		this.value.setAtMax(status); 


		for (ServoChangeNotifier notifier: this.sensorListener )
		{
			notifier.isAtMax(this);	
		}	

		return (true);
	}

	return (false);
	
	

}


// 2012.2.9
public boolean isAtMax() 
{
	return (this.value.isAtMax());
}

	
	
	
	
public boolean setActive(boolean status) 
{

	if (this.active != status) 
	{
		this.active = status;
		this.value.setActive(status);

		for (ServoChangeNotifier notifier: this.sensorListener )
		{
			notifier.isActive(this);	
		}	

		return (true);
	}

	return (false);
}





	public boolean isActive() {
		return (this.active);
	}

/**
 * set servos inverse flag if inverse servo change its driving direction
 * from left to right to from right to left
 * 
 * @param direction
 *            true for inverted , false for normal
 * @return
 */

public boolean setReverse(boolean direction) 
{
	if (this.reverse != direction) 
	{	
		this.reverse = direction;
		this.value.setInverse(direction);
		return (true);
	}

	return (false);

}

/**
 * 
 * 
 * @return status of the inverse flag
 */

public boolean isReverse()
{
	return (this.reverse);
}



public boolean setStalling(boolean status) 
{
	if (this.stalling != status) 
	{
		this.stalling = status;
		this.value.setStalling(status);
		return (true);
	}

	return (false);

}



public boolean isStalling() 
{
	return (this.stalling);
}

	
	
	
	
	
	
	
	
	
	
public boolean remote_servoOn()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_servoOn.getCommand(this.componentProtocol.servoOnCommandId,this.localId)));
}
	

public boolean remote_servoOff()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_servoOff.getCommand(this.componentProtocol.servoOffCommandId,this.localId)));
}


public boolean remote_getServoPosition()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_getServoPosition.getCommand(this.componentProtocol.getServoPositionCommandId, this.localId)));
}




public boolean remote_getServoSpeed()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_getServoSpeed.getCommand(this.componentProtocol.getServoSpeedCommandId, this.localId)));
}

public boolean remote_getServoForceThreshold()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_getServoForceThreshold.getCommand(this.componentProtocol.getServoForceThresholdCommandId, this.localId)));
}


public boolean remote_getServoStatus()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_getServoStatus.getCommand(this.componentProtocol.getServoStatusCommandId, this.localId)));
}


public boolean remote_calibrate()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_calibrateServo.getCommand(this.componentProtocol.cmdCalibrateServoId, this.localId)));
}



/**
 * move a servo at given velocity. 
 * @param velocity servos movement velocity in radiant
 * @return boolean if command could be sent, false if not
 */
public boolean remote_move(float velocity)
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_servoMove.getCommand(this.componentProtocol.cmdMoveId, this.localId, velocity)));
}





public boolean remote_moveTo(float position)
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_moveServoTo.getCommand(this.componentProtocol.moveServoToCommandId, this.localId, position)));
}


public boolean remote_moveToAtSpeed(float position, float speed)
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_moveServoToAtSpeed.getCommand(this.componentProtocol.moveServoToAtSpeedCommandId, this.localId, position, speed)));
}



public boolean remote_setServoPosition(float position)
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_setServoPosition.getCommand(this.componentProtocol.setServoPositionCommandId, this.localId, position)));
}


public boolean remote_setServoSpeed(int position)
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_setServoSpeed.getCommand(this.componentProtocol.setServoSpeedCommandId, this.localId, position)));
}

public boolean remote_setServoForceThreshold(int value)
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_setServoForceThreshold.getCommand(this.componentProtocol.setServoForceThresholdCommandId, this.localId, value)));
}

public boolean remote_setServoForcePosition(int value)
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_setServoForcePosition.getCommand(this.componentProtocol.setServoForcePositionCommandId, this.localId, value)));
}


public boolean remote_setServoDefaults(float minRange, float maxRange, int offset, int scale, 
		boolean inverse)
{
	
	if (this.componentProtocol==null)
		return(false);
	
	return(sendData(Cmd_setServoSettings.getCommand(this.componentProtocol.cmdSetSettingsId, this.localId,
			minRange, maxRange, offset, scale, inverse)));
}

public ServoAngleValue getServoValue()
{
	// TODO Auto-generated method stub
	return (this.value);
}


public boolean remote_forceFeedbackOn()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_forceFeedbackOn.getCommand(this.componentProtocol.forceFeedbackOnCmdId,this.localId)));
}

public boolean remote_forceFeedbackOff()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_forceFeedbackOff.getCommand(this.componentProtocol.forceFeedbackOffCmdId,this.localId)));
}

public boolean remote_positionFeedbackOn()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_positionFeedbackOn.getCommand(this.componentProtocol.positionFeedbackOnCmdId,this.localId)));
}

public boolean remote_positionFeedbackOff()
{
	if (this.componentProtocol==null)
		return(false);
	
	
	return(sendData(Cmd_positionFeedbackOff.getCommand(this.componentProtocol.positionFeedbackOffCmdId,this.localId)));
}



@Override
public boolean remote_getValue()
{
	// TODO Auto-generated method stub
	return false;
}


@Override
public void valueChanged(ComponentValue<?> componentValue)
{
	
	if (componentValue == this.velocityControl)
	{
		this.remote_move(this.velocityControl.getValue());
	}
	
	if (componentValue == this.destinationControl)
	{
		float velocity;
		velocity =  this.destinationControl.getVelocity();
		
		if (velocity == 0)
		{
			this.remote_moveTo(this.destinationControl.getValue());
		}
		else
		{
			this.remote_moveToAtSpeed(this.destinationControl.getValue(), velocity);	
		}
		
	}
		
	
	
	
	else if (componentValue == this.value)
	{
		for (ServoChangeNotifier listener : this.sensorListener)
		{
			listener.servoPositionChanged(this);
		}
		
	}

}


/*
@Override
public void isAtMax(ServoAngleValue value)
{
	for (ServoChangeNotifier notifier: this.sensorListener )
	{
		notifier.isAtMax(this);	
	}	
	
}



@Override
public void isAtMin(ServoAngleValue value)
{
	for (ServoChangeNotifier notifier: this.sensorListener )
	{
		notifier.isAtMin(this);	
	}	
	
}
*/

@Override
public ArrayList<ComponentValue<?>> getDataValues()
{
	
	ArrayList<ComponentValue<?>> values = super.getDataValues();
//	values.add(this.value);
			
	return (values);
}





	/*********************** old **************************/



	/*
	public boolean setServoDefaults(int index, int minRange, int maxRange,
			int offset, boolean reverse) {
		if (this.controllerListener == null)
			return (false);

		return (this.controllerListener.setServoDefaults(this.localId,
				minRange, maxRange, offset, reverse));
	}


*/
}
"""