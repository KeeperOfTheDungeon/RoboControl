

from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage


class Msg_vcnl4000Settings(RemoteMessage):
	def __init__(self):

		super().__init__("Vcnl4000Settings","settings for a Vcnl4000 Sensor")
		self._parameter_list.append(RemoteParameterUint8("index","VCNL4000 sensor index"))
	#	self._parameter_list.append(RemoteParameterUint8("brightness","LED brightness"))

		pass



"""package de.hska.lat.robot.component.sensor.vcnl4000.protocol;

import de.hska.lat.comm.remote.RemoteMessage;

import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;
import de.hska.lat.robot.component.sensor.vcnl4000.Vcnl4000AveragingModes;
import de.hska.lat.robot.component.sensor.vcnl4000.Vcnl4000FrequencyModes;
import de.hska.lat.robot.component.sensor.vcnl4000.Vcnl4000IrCurrent;




/**
 * 
 * @author Oktavian Gniot
 *
 *command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor
 */

public class Msg_vcnl4000Settings extends RemoteMessage
{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 2638694167468005642L;



	protected static final String name = "setVcnl4000Settings";
	protected static final String description = "set settings for a Vcnl4000 Sensor";


	private static final int INDEX_SENSOR 				= 0;
	private static final int INDEX_PARAMETERS			= 1;

	

public Msg_vcnl4000Settings() 
{
	this.add(new RemoteParameterUint8("index","VCNL4000 sensor index"));
	this.add(new RemoteParameterVcnl4000Settings());
}
	
	
public Msg_vcnl4000Settings(int command) 
{
	this();
	this.setId(command);
}


@Override
public String getName() 
{
	return(Msg_vcnl4000Settings.name);
}


@Override
public String getDescription() 
{
	return(Msg_vcnl4000Settings.description);
}





public void setData(int index,
		Vcnl4000IrCurrent			irCurrent,
		Vcnl4000AveragingModes		averagingMode,
		Vcnl4000FrequencyModes 		proximityFrequency,
		boolean 					autoConversion,
		boolean 					autoCompensation)
{
	(( RemoteParameterUint8) this.get(Msg_vcnl4000Settings.INDEX_SENSOR)).setValue(index);
	(( RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).setIrCurrent(irCurrent);
	(( RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).setAveragingMode(averagingMode);
	(( RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).setProximityFrequency(proximityFrequency);
	(( RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).setAutoConversion(autoConversion);
	(( RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).setAutoCompensation(autoCompensation);

	
}




public Vcnl4000IrCurrent getIrCurrent()
{
	return((( RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).getIrCurrent());
}


public Vcnl4000AveragingModes getAveragingMode()
{
	return(((RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).getAveragingMode());
}


public Vcnl4000FrequencyModes getProximityFrequency()
{
	return(((RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).getProximityFrequency());
}


public boolean getAutoConversion()
{
	return(((RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).getAutoConversion());
}


public boolean getAutoCompensation()
{
	return(((RemoteParameterVcnl4000Settings) this.get(Msg_vcnl4000Settings.INDEX_PARAMETERS)).getAutoCopensation());
}




/**
 * get sensor index for sensor corresponding to this message
 * @return  index of sensor in sensor set
 */
public int getIndex()
{
	return((( RemoteParameterUint8) this.get(Msg_vcnl4000Settings.INDEX_SENSOR)).getValue());
}



public static Msg_vcnl4000Settings getCommand(int id)
{
	Msg_vcnl4000Settings cmd;
	cmd = new Msg_vcnl4000Settings(id);
	
	return(cmd);
}



public static Msg_vcnl4000Settings getCommand(int command,int index, 
		Vcnl4000IrCurrent			irCurrent,
		Vcnl4000AveragingModes		averagingMode,
		Vcnl4000FrequencyModes 		proximityFrequency,
		boolean 					autoConversion,
		boolean 					autoCompensation
		)
{
	
	Msg_vcnl4000Settings cmd;
	cmd = Msg_vcnl4000Settings.getCommand(command);
	cmd.setData(index, irCurrent, averagingMode, proximityFrequency, autoConversion, autoCompensation);
	
	return(cmd);
}





}

"""