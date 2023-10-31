from RoboControl.Robot.Component.ComponentSet import ComponentSet
from RoboControl.Robot.Component.Sensor.Sensor import Sensor
from RoboControl.Robot.Device.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Value.ComponentValue import ComponentValue
from RoboControl.Robot.Value.ComponentValue import LightValue

#from RoboControl.Robot.Component.Sensor.LuxSensorProtocol import Cmd_getLux, Msg_lux, Stream_lux

class LightSensor(Sensor):
    _sensor_listener = list()

def __init__(self, meta_data):
        super().__init__(meta_data)
        self._lux_value = LightValue(meta_data)  # ,10000)



class LightSensorSet(ComponentSet):
    def __init__(self, components, protocol):
        super().__init__(
            [LightSensor(component) for component in components]
        )
        #self._cmd_setBrightness = protocol["cmd_setBrightness"]
        #self._cmd_getBrightness = protocol["cmd_getBrightness"]
        #self._msg_lux = protocol['msg_lux']
        #self._stream_lux = protocol['stream_lux']