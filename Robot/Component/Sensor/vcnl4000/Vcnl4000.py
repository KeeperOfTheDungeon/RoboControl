from RoboControl.Robot.Component.RobotComponent import RobotComponent
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000DistanceSensor import Vcnl4000DistanceSensor
from RoboControl.Robot.Component.Sensor.vcnl4000.Vcnl4000LuxSensor import Vcnl4000LuxSensor


class Vcnl4000(RobotComponent):
    _max_range = 0
    _min_range = 0
    _beam_width = 0

    def __init__(self, meta_data):
        super().__init__(meta_data)

        self._lux_sensor = Vcnl4000LuxSensor(meta_data)
        self._distance_sensor = Vcnl4000DistanceSensor(meta_data)

    def get_lux_sensor(self):
        return self._lux_sensor

    def get_distance_sensor(self):
        return self._distance_sensor

    def set_transmitter(self, transmitter):
        super().set_transmitter(transmitter)
        self._lux_sensor.set_transmitter(transmitter)
        self._distance_sensor.set_transmitter(transmitter)


"""

public class Vcnl4000 extends RobotComponent<Vcnl4000ChangeNotifier,ComponentSettingsChangeNotifier,Vcnl4000Protocol >
{

    

    protected Vcnl4000LuxSensor luxSensor;
    protected Vcnl4000DistanceSensor distanceSensor;

    
    protected Vcnl4000AveragingModes	averagingMode	= Vcnl4000AveragingModes.getDefault();
    protected Vcnl4000FrequencyModes 	proximityFrequency 	= Vcnl4000FrequencyModes.getDefault();
    protected Vcnl4000IrCurrent			irCurrent		= Vcnl4000IrCurrent.getDefault();
    
    protected boolean 					autoConversion;
    protected boolean 					autoCompensation;

    
    
public Vcnl4000(ComponentMetaData metaData,Vcnl4000Protocol protocol) 
{
    super(metaData, protocol);
    
    this.luxSensor = new Vcnl4000LuxSensor(metaData, protocol.luxProtocol);
    this.distanceSensor = new Vcnl4000DistanceSensor(metaData,protocol.distanceProtocol);
}







public LuxValue getLuxValue()
{
    return (this.luxSensor.getLuxValue());
}



public DistanceValue getDistanceValue()
{
    return (this.distanceSensor.getDistanceValue());
}


public boolean remote_setSettings(Vcnl4000AveragingModes averagingMode, Vcnl4000FrequencyModes 	proximityFrequency,
            Vcnl4000IrCurrent irCurrent, boolean autoConversion, boolean autoCompensation)
{
    if (this.componentProtocol==null)
        return(false);
    
    
    return(sendData(Cmd_setVcnl4000Settings.getCommand(this.componentProtocol.cmdSetSettingsId, this.localId,
                    irCurrent, averagingMode, proximityFrequency,
                       autoConversion,  autoCompensation)));
}




public boolean remote_getRawProximityValue()
{
    if (this.componentProtocol==null)
        return(false);

    return(sendData(Cmd_getVcnl4000RawProximity.getCommand(this.componentProtocol.cmdGetRawProximityId, this.localId)));
}


public boolean remote_getDistanceTable()
{
    if (this.componentProtocol==null)
        return(false);

    return(sendData(Cmd_getVcnl4000DistanceTable.getCommand(this.componentProtocol.cmdGetDistanceTableId, this.localId)));
}


public boolean remote_setDistanceTable( DistanceTable distances)
{
    if (this.componentProtocol==null)
        return(false);

    return(sendData(Cmd_setVcnl4000DistanceTable.getCommand(this.componentProtocol.cmdSetDistanceTableId, this.localId, distances)));
}





public void setSettings(Vcnl4000IrCurrent irCurrent, Vcnl4000AveragingModes averagingMode, Vcnl4000FrequencyModes 	proximityFrequency,
         boolean autoConversion, boolean autoCompensation)
{
    this.averagingMode = averagingMode;
    this.proximityFrequency = proximityFrequency;
    this.irCurrent = irCurrent;
    this.autoConversion = autoConversion;
    this.autoCompensation = autoCompensation;
    this.notifySetupChanged();
    
}







@Override
public ArrayList<ComponentValue<?>> getDataValues()
{
    
    ArrayList<ComponentValue<?>> values = this.luxSensor.getDataValues();
    
    
    values.addAll(this.distanceSensor.getDataValues());
    
    return (values);
}






/**
 * set transmitter for this component. All data will be sent thru this transmitter
 * @param transmitter transmitter
 */
@Override
public void setTransmitter(RemoteDataTransmitter transmitter)
{
    super.setTransmitter(transmitter);
    
    this.luxSensor.setTransmitter(transmitter);
    this.distanceSensor.setTransmitter(transmitter);
}




public Vcnl4000IrCurrent getIrCurrent()
{
    return (this.irCurrent );
}




public Vcnl4000AveragingModes getAveraging()
{
    return (this.averagingMode);
}



public Vcnl4000FrequencyModes getProximityFrequency()
{
    return (this.proximityFrequency);
}




public boolean getAutoConversion()
{
    return (this.autoConversion);
}




public boolean getAutoCompensation()
{
    return (this.autoCompensation);
}







}
"""
