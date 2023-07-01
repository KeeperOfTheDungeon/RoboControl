from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8


class Cmd_setLedColor(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "setLedBrightness", "set brightness of a LED")
        self._parameter_list.append(RemoteParameterUint8("index", "LED index"))
        self._parameter_list.append(RemoteParameterUint8("brightness", "LED brightness"))

    def set_index(self, index):
        self._parameter_list[self._index].set_value(index)

    def get_index(self):
        return self._parameter_list[self._index].get_value()

    def set_data(self, index, brightness):
        self.get(self._index).set_value(index)
        self.get(self._led_brightness).set_value(brightness * 255)

    def get_brightness(self):
        value = self.get(self._led_brightness).get_value()
        value /= 255
        return value

    def get_command(id, index, brightness):
        cmd = Cmd_setLedColor(id)
        cmd.set_data(index, brightness)
        return cmd


"""


package de.hska.lat.robot.component.actor.led.protocol;



import de.hska.lat.color.HsvColor;
import de.hska.lat.comm.remote.RemoteCommand;
import de.hska.lat.comm.remote.parameter.RemoteParameterUint8;
import de.hska.lat.robot.component.generic.colorSensor.protocol.RemoteParameterHsvColor;






/**
 * command that ping a device, device returns ping response message  
 * @author Oktavian Gniot
 *
 */
public class Cmd_setLedColor extends RemoteCommand
{
    

    /**
     * 
     */
    private static final long serialVersionUID = -7446077035148723843L;


    private static final int INDEX_LED 		= 0;
    private static final int INDEX_COLOR 	= 1;
    

    protected static final String name = "setLedColor";
    protected static final String description = "set color of an RGB LED";
    
    
    
public Cmd_setLedColor() 
{
    
    this.add(new RemoteParameterUint8("index","Led index"));
    this.add(new RemoteParameterHsvColor("color","Led color"));
}



public Cmd_setLedColor(int command) 
{
    this();
    this.setId(command);
}


public void setData(int index, HsvColor color)
{
    (( RemoteParameterUint8) this.get(Cmd_setLedColor.INDEX_LED)).setValue(index);
    (( RemoteParameterHsvColor) this.get(Cmd_setLedColor.INDEX_COLOR)).setColor(color);
}



public int getIndex()
{
    return((( RemoteParameterUint8) this.get(Cmd_setLedColor.INDEX_LED)).getValue());
}


public HsvColor getColor()
{
    return((( RemoteParameterHsvColor) this.get(Cmd_setLedColor.INDEX_COLOR)).getColor());
}




@Override
public String getName() 
{
    return(Cmd_setLedColor.name);
}


@Override
public String getDescription() 
{
    return(Cmd_setLedColor.description);
}



public static Cmd_setLedColor getCommand(int command)
{
    Cmd_setLedColor cmd;
    cmd = new Cmd_setLedColor(command);
    
    return(cmd);
}

public static Cmd_setLedColor getCommand(int command,int index, HsvColor color)
{
    Cmd_setLedColor cmd;
    cmd = Cmd_setLedColor.getCommand(command);
    cmd.setData(index, color);
    
    return(cmd);
}


}
"""
