from RoboControl.Robot.Component.Sensor.LuxSensor import LuxSensor

VCNL4000_MAX_RANGE = 16383.5
VCNL4000_MIN_RANGE = 0.0


class Vcnl4000LuxSensor(LuxSensor):
    def __init__(self, meta_data):
        meta_data["min_range"] = VCNL4000_MIN_RANGE
        meta_data["max_range"] = VCNL4000_MAX_RANGE
        meta_data["protocol"]['cmd_getValue'] = meta_data["protocol"]['cmd_getLux']
        super().__init__(meta_data)
        self._gain = 0

    # self._cmd_get_settings  = protocol["cmd_getSettings"]

    def get_message_processors(self):
        pass


"""
public class Vcnl4000LuxSensor extends LuxSensor <ComponentSettingsChangeNotifier, LuxSensorProtocol >
{

    
    
    protected int gain;
    protected int address;
    


}
"""
