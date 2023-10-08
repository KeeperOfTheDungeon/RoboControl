from RoboControl.Robot.AbstractRobot.AbstractListener import CurrentSensorListener
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_getActualCurrentDrain import \
    Cmd_getActualCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_getMaximalCurrentDrain import \
    Cmd_getMaximalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_getTotalCurrentDrain import Cmd_getTotalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_resetMaximalCurrentDrain import \
    Cmd_resetMaximalCurrentDrain
from RoboControl.Robot.Component.generic.currentSensor.protocol.Cmd_resetTotalCurrentDrain import \
    Cmd_resetTotalCurrentDrain
from RoboControl.Robot.Value.current.CurrentValue import CurrentValue


class CurrentSensor(Sensor):
    _sensor_listener: list[CurrentSensorListener]

    def __init__(self, meta_data):
        super().__init__(meta_data)

        protocol = meta_data["protocol"]
        self._cmd_get_max_current = protocol["cmd_getMaxCurrent"]
        self._cmd_get_total_current = protocol["cmd_getTotalCurrent"]
        self._cmd_reset_max_current = protocol["cmd_resetMaxCurrent"]
        self._cmd_reset_total_current = protocol["cmd_resetTotalCurrent"]

        self._window_size = 0
        self._threshold = 0
        self._actual = CurrentValue(meta_data)
        self._total = CurrentValue(meta_data)
        self._max = CurrentValue(meta_data)

    def get_actual(self):
        return self._actual

    def get_total(self):
        return self._total

    def get_max(self):
        return self._max

    def get_actual_value(self):
        return self._actual

    def set_actual(self, value):
        self._actual.set_value(value)

        for listener in self._sensor_listener:
            listener.current_value_changed()

    def get_max_value(self):
        return self._max

    def set_max(self, value):
        self._max.set_value(value)

        for listener in self._sensor_listener:
            listener.current_value_changed()

    def get_total_value(self):
        return self._total

    def set_total(self, value):
        self._total.set_value(value)

        for listener in self._sensor_listener:
            listener.current_value_changed()

    def remote_get_current(self):
        cmd = Cmd_getActualCurrentDrain.get_command(self._cmd_get_value, self._local_id)
        self.send_data(cmd)

    def remote_get_max_current(self):
        cmd = Cmd_getMaximalCurrentDrain.get_command(self._cmd_get_max_current, self._local_id)
        self.send_data(cmd)

    def remote_get_total_current(self):
        cmd = Cmd_getTotalCurrentDrain.get_command(self._cmd_get_total_current, self._local_id)
        self.send_data(cmd)

    def remote_reset_max_current(self):
        cmd = Cmd_resetMaximalCurrentDrain.get_command(self._cmd_reset_max_current, self._local_id)
        self.send_data(cmd)

    def remote_reset_total_current(self):
        cmd = Cmd_resetTotalCurrentDrain.get_command(self._cmd_reset_total_current, self._local_id)
        self.send_data(cmd)


"""package de.hska.lat.robot.component.currentSensor;

import java.util.ArrayList;


    
public CurrentSensor(ComponentMetaData metaData, CurrentSensorProtocol protocol)
{
    super(metaData, protocol);
    
    this.actual = new CurrentValue(metaData.getName()+" actual current");
    this.total = new CurrentValue(metaData.getName() + " total current");
    this.max = new CurrentValue(metaData.getName() + " max current");
}





/**
 * get actual current level for this source 
 * @return
 */



/**
 * get size of measurement window , the real size is 10 * windowSize 
 * @return actual window size
 */

public int getWindowSize()
{
    return (this.windowSize);
}

public void setWindowSize(int windowSize)
{
    int index;
    

    this.windowSize=windowSize;
    
    for (index=0;index<this.setupListener.size();index++)
    {
        this.setupListener.get(index).currentWindowSizeChanged(this);
    }


    
    
}


/**
 * get current threshold, threshold is the minimum level value for current sensing 
 * @return actual threshold
 */
public int getThreshold()
{
    return (this.threshold);
}

public void setThreshold(int threshold)
{
    int index;

    this.threshold=threshold;
        
    for (index=0;index<this.setupListener.size();index++)
    {
            this.setupListener.get(index).currentThresholdChanged(this);
    }

}





public boolean remote_setSettings(int windowSize, int threshold)
{
    
    if (this.componentProtocol==null)
        return(false);
    

    return(sendData(Cmd_setCurrentSettings.getCommand(this.componentProtocol.cmdSetSettingsId, this.localId, windowSize, threshold)));
}

public boolean remote_resetTotal()
{
    if (this.componentProtocol==null)
        return(false);
    
    return(sendData(Cmd_resetTotalCurrentDrain.getCommand(this.componentProtocol.cmdResetTotalCurrentDrainId, this.localId )));
}

public boolean remote_resetMax()
{
    if (this.componentProtocol==null)
        return(false);
    
    return(sendData(Cmd_resetMaximalCurrentDrain.getCommand(this.componentProtocol.cmdResetMaximalCurrentDrainId, this.localId )));
}

public CurrentValue getValue()
{
    return (this.actual);
}


@Override
public ArrayList<ComponentValue<?>> getDataValues()
{
    
    ArrayList<ComponentValue<?>> values = new ArrayList<ComponentValue<?>>();
    values.add(this.actual);
    values.add(this.total);
    values.add(this.max);
            
    return (values);
}




    
}
"""
