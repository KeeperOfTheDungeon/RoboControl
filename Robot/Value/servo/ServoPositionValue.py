from RoboControl.Robot.Math.Radiant import Radiant
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.RadiantValue import RadiantValue


# WIP This isn't used anywhere in the Java project
class ServoPositionValue(RadiantValue):  # ServoAngleValue
    _is_at_max: bool
    _is_at_min: bool

    _is_active: bool
    _is_on: bool

    _is_inverse: bool
    _is_stalling: bool

    def __init__(self, meta_data):
        meta_data["type_name"] = "servo position"
        meta_data["description"] = "servo position"
        super().__init__(meta_data)
        self._min_range = 0
        self._max_range = 0

    def is_active(self) -> bool:
        return self._is_active

    def set_active(self, status: bool) -> None:
        self._is_active = status

    def is_on(self) -> bool:
        return self._is_on

    def set_on(self, status: bool) -> None:
        self._is_on = status

    def is_inverse(self) -> bool:
        return self._is_inverse

    def set_inverse(self, status: bool) -> None:
        self._is_inverse = status

    def get_position_as_radiant(self) -> float:
        return self.get_value()

    get_rotation = get_position_as_radiant

    def get_position_as_degree(self) -> float:
        return Radiant.convert_radiant_to_degree(self.get_value())

    def is_stalling(self) -> bool:
        return self._is_stalling

    def set_stalling(self, is_stalling: bool) -> None:
        self._is_stalling = is_stalling

    def is_at_min(self) -> bool:
        return self._is_at_min

    def set_at_min(self, status: bool) -> None:
        self._is_at_min = status

    def is_at_max(self) -> bool:
        return self._is_at_max

    def set_at_max(self, status: bool) -> None:
        self._is_at_max = status

    def on_change(self, source: ComponentValue) -> None:
        # if source == self._min_servo_range:
        # 	self._min_range = source.get_value()
        # elif source == self._max_servo_range:
        # 	self._max_range = source.get_value()
        self.set_value(source.get_value())



"""
package de.hska.lat.robot.value.servoPosition;

import de.hska.lat.robot.value.ComponentValue;


public class ServoPositionValue extends ComponentValue<ServoPositionValue>
{

	private static final String TYPE_NAME = "servo position";
	
	protected boolean isAtMax;
	protected boolean isAtMin;
	protected boolean isActive;
	


public ServoPositionValue(String name)
{
	super(name);
	// TODO Auto-generated constructor stub
}


@Override
public String getTypeName()
{
	return(ServoPositionValue.TYPE_NAME);
}
}

"""



"""

public class ServoPosition extends FloatValue //extends ComponentValue<ServoPosition,ServoPositionChangeNotifier> implements FloatValueChangeListener
{

//	protected FloatValue maxServoRange;
//	protected FloatValue minServoRange;
	
	protected float minRange;
	protected float maxRange;

public ServoPosition(float minRange,float maxRange)
{
	super("servo position");

	this.minRange=minRange;
	this.maxRange=maxRange;
	
//	this.minRange = this.minServoRange.getValue();
//	this.maxRange = this.maxServoRange.getValue(); 
	
//	this.minServoRange.addListener(this);
//	this.maxServoRange.addListener(this);
	
}
	
	



public float getPositionAsRadiant()
{

	 float radiant;
	
	radiant = this.value * ((float)Math.PI / 180f );
	
	return(radiant);

}


public float getPositionAsDegree()
{
	return(Radiant.convertRadiantToDegree(this.value));
}




/*
@Override
public void valueChanged(ComponentValue<FloatValue, ?> source)
{
	if (source==minServoRange)
	{
		this.minRange=source.getValue();
	}
	else if (source==maxServoRange)
	{
		this.maxRange=source.getValue();
	}
	
	this.setValue(source.getValue());
}

*/

	



}

"""