from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol


class Cmd_startStreamData(RemoteCommand):

    def __init__(self):
        super().__init__(DeviceProtocol.CMD_START_STREAM_DATA, "startStreamData", "start streaming data")
        self._type_index = 0
        self._period_index = 1
        self._parameter_list.append(RemoteParameterUint8("index", "stream index"))
        self._parameter_list.append(RemoteParameterUint8("period", "stream period"))

        pass

    def set_type(self, type):
        self._parameter_list[self._type_index].set_value(type)

    def set_period(self, new_type):
        self._parameter_list[self._period_index].set_value(new_type)

    @staticmethod
    def get_command(new_type, period):
        cmd = Cmd_startStreamData()
        cmd.set_type(new_type)
        cmd.set_period(period)
        return cmd


"""package de.hska.lat.robot.device.protocol;

import de.hska.lat.comm.remote.RemoteCommand;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;






/**
 * command that ping a device, device returns ping response message  
 * @author Oktavian Gniot
 *
 */
public class Cmd_startStreamData extends RemoteCommand
{
    
    
/**
     * 
     */
    private static final long serialVersionUID = 3564313371574431201L;

    
    
    private static final int INDEX_TYPE = 0;
    private static final int INDEX_PERIOD = 1;
    

    protected static final String name = "startStreamData";
    protected static final String description = "start streaming data";
    
    
public Cmd_startStreamData() 
{
    this.add(new RemoteParameterUint8("type","type of data (device dependent)"));
    this.add(new RemoteParameterUint8("period","period of in 10 ms steps"));
}



public Cmd_startStreamData(int command) 
{
    this();
    this.setId(command);
}


public void setData(int index,int period)
{
    (( RemoteParameterUint8) this.get(Cmd_startStreamData.INDEX_TYPE)).setValue(index);
    (( RemoteParameterUint8) this.get(Cmd_startStreamData.INDEX_PERIOD)).setValue(period);
}



public int getType()
{
    return((( RemoteParameterUint8) this.get(Cmd_startStreamData.INDEX_TYPE)).getValue());
}

public int getPeriod()
{
    
    return((( RemoteParameterUint8) this.get(Cmd_startStreamData.INDEX_PERIOD)).getValue());
}


@Override
public String getName() 
{
    return(Cmd_startStreamData.name);
}


@Override
public String getDescription() 
{
    return(Cmd_startStreamData.description);
}



public static Cmd_startStreamData getCommand(int command)
{
    Cmd_startStreamData cmd;
    cmd = new Cmd_startStreamData(command);
    
    return(cmd);
}

public static Cmd_startStreamData getCommand(int command,int index, int period)
{
    Cmd_startStreamData cmd;
    cmd = Cmd_startStreamData.getCommand(command);
    cmd.setData(index, period);
    
    return(cmd);
}


}
"""
