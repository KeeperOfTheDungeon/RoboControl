
class ComponentValue:
	def __init__(self,meta_data):

		self._name = meta_data["name"] 
		self._type_name = meta_data["type_name"] 
		self._description = meta_data["description"]
		
		self._max_range = meta_data["max_range"]
		self._min_range = meta_data["min_range"] 
		self._value = 0

		self._overflow = False
		self._underflow = False
		self._valid = False

		self._notifyAllways = True
		self._value_chanege_listener_list = list()

	def set_name(self, name):
		self._name = name


	def get_name(self):
		return self._name

	def has_name(self, name):
		return self._name == name


	def get_type_name(self):
		return self._type_name

	def set_range(self, min, max):
		self._max_range = max
		self._min_range = min

	def get_min_range(self):
		return self._min_range

	def get_max_range(self):
		return self._max_range



	def set_overflow_value(self):
		self._value = self._max_range
		self._overflow = True
		self._underflow = False
		self._valid = True

	def set_underflow_value(self):
		self._value = self._min_range
		self._overflow = False
		self._underflow = True
		self._valid = True


	def set_value(self, value):
		value_changed = False

		if self._notifyAllways == True:
			value_changed = True
		elif (value != self._value):
			value_changed = True

		if value > self._max_range:
			self.set_overflow_value()
		elif value < self._min_range:
			self.set_underflow_value()	
		else:
			self._overflow = False
			self._underflow = False
			self._value = value
			self._valid = True

		if (value_changed == True):
			self.notify_value_changed()

		return(self._value)	


	def get_value(self):
		return(self._value)	


	def is_valid(self):
		return (self._valid)


	def add_listener(self, listener):
		self._value_chanege_listener_list.append(listener)

	def remove_listener(self, listener):
		self._value_chanege_listener_list.remove(listener)

	def notify_value_changed(self):
		for listener in self._value_chanege_listener_list:
			listener()



	def actualize(self):
		return(False)



"""		
package de.hska.lat.robot.value;

import java.util.ArrayList;



public abstract class ComponentValue<v>
{


	
	public ComponentValue(String name)
	{

		this.name = name;
	}

	public ComponentValue(String name, float minRange, float maxRange)
	{
		this.name = name;
		this.minRange = minRange;
		this.maxRange = maxRange;

	}


	/**
	 * get type name of this value
	 * 
	 * @return type name of this value
	 */
	public String getTypeName()
	{
		return (ComponentValue.TYPE_NAME);
	}

	
	
	/**
	 * get description of this type	
	 * @return description of this value
	 */
	public String getTypeDescription()
	{
		return (ComponentValue.TYPE_DESCRIPTION);
	}

	
	
	
	/**
	 * get name of this value
	 * 
	 * @return name of this value
	 */
	public String getName()
	{
		return (this.name);
	}


	@Override
	public String toString()
	{
		return (this.name);
	}


	
	/**
	 * format given float value to a string with
	 * 
	 * @param value
	 * @param fraction
	 * @return
	 */

	public static String toFormatedFractionString(float value, int fraction)
	{
		int fractionSize;
		String valueAsString;

		valueAsString = String.valueOf(value);
		fractionSize = valueAsString.length() - valueAsString.indexOf('.');

		if (fractionSize > fraction)
			fractionSize = fraction + 1;

		valueAsString = valueAsString.substring(0, valueAsString.indexOf('.')
				+ fractionSize);

		return (valueAsString);
	}


}
"""