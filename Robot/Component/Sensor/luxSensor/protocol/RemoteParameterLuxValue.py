from RoboControl.Com.Remote.Parameter.RemoteParameter import RemoteParameter


class RemoteParameterLuxValue(RemoteParameter):

	def __init__(self, name, description):
		super().__init__(name, description, 3)
		self._value = 0.0

	def put_data(self, data_buffer):
		data_buffer.append(self._value + 0x800000 )	


	def parse_from_buffer(self ,data_buffer ,index):


		value = data_buffer[index] << 16
		value |= data_buffer[index+1] << 8
		value |= data_buffer[index+2]
		
		self._value = value

		self._value *= 0.25
		return self._byte_size

	def get_lux(self):
		return self._value


"""
package de.hska.lat.robot.component.generic.luxSensor.protocol;

import java.nio.ByteBuffer;

import de.hska.lat.comm.remote.parameter.RemoteParameter;

public class RemoteParameterLuxValue extends RemoteParameter<RemoteParameterLuxValue>
{

	protected static final int BYTE_SIZE = 3;
	protected float value;
	
	
	
public RemoteParameterLuxValue(String name, String description)
{
	super(name, description);
	// TODO Auto-generated constructor stub
}


public void setValue(float value)
{
	this.value = value;
}


public float getValue()
{
	return(this.value);

}







@Override
public int getBufferSize()
{
	return(RemoteParameterLuxValue.BYTE_SIZE);
}



@Override
public void putData(ByteBuffer data)
{
	byte high=0;
	char low=0;
	
//	high = (byte) (this.value>>16);
//	low = (char) (this.value&0xffff);
	
	data.put(high);
	data.putChar(low);
}


@Override
public int parseFromBuffer(ByteBuffer dataBuffer, int index)
{
	int data;
	/*
	 * 	value*=(1<<7);
	
	
	
	if (value >0xffffff)
	{
		this.value = 0xffffff;
	}	
	else	
	{
		this.value = (int) value;
	}

	 */
	byte high;
	char low;
	
	
	high = dataBuffer.get(index++);
	low = dataBuffer.getChar(index);
	
	
	data = high <<16;
	data += low;
	
	
	this.value = ((float) (data)) * 0.25f;
	return(RemoteParameterLuxValue.BYTE_SIZE);
}



@Override
public String getAsString(boolean description)
{
	String returnString ="";
	
	if (description)
	{
		returnString+= this.name+"=";
		
		returnString+= this.value+"lux";
	}
	else
	{
		returnString+= this.value;
	}	
	
	return(returnString);
}
}
"""