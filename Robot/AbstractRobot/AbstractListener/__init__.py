import abc

from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


# FIXME The classes here should have their own files


# TODO
class ChangeListener(abc.ABC):  # ChangeListener = ActionListener??
    def on_change(self):
        raise ValueError("WIP AbstractListener.on_change should be overridden")


# TODO
class PacketLoggerListener(ChangeListener):
    pass


# TODO
class SensorListener(ChangeListener):
    pass


class ValueListener(ChangeListener):
    def value_changed(self):
        pass


class SetupListener(abc.ABC):
    def settings_changed(self, component: "RobotComponent") -> None:
        pass


class ServoSensorListener(SensorListener):
    def servo_position_changed(self, servo: "Servo") -> None:
        pass


class ServoSetupListener(SetupListener, ServoSensorListener):  # ServoSetupChangeNotifier
    def servo_setup_changed(self, servo: "Servo") -> None:
        pass

    def servo_speed_changed(self, global_id: int, speed: int) -> None:
        pass

    def servo_force_threshold_changed(self, global_id: int, threshold: int) -> None:
        pass


class ServoDataListener(ServoSensorListener):  # ServoChangeNotifier
    def position_feedback_on(self, servo: "Servo") -> None:
        pass

    def force_feedback_on(self, servo: "Servo") -> None:
        pass

    def is_on(self, servo: "Servo") -> None:
        pass

    def is_at_min(self, servo: "Servo") -> None:
        pass

    def is_at_max(self, servo: "Servo") -> None:
        pass

    def is_active(self, servo: "Servo") -> None:
        pass


class CurrentSensorListener(SensorListener):
    def current_value_changed(self) -> None:
        pass


class LuxSensorListener(SensorListener):
    def lux_value_changed(self, sensor: "LuxSensor") -> None:
        pass


class DistanceSetupListener(SetupListener):
    def distance_table_changed(self, sensor: "DistanceSensor") -> None:
        pass


class ComStatusListener(abc.ABC):
    def com_status_changed(self, status: "ComStatus") -> None:
        pass


class CpuStatusListener(abc.ABC):
    def cpu_status_changed(self, status: "CpuStatus") -> None:
        pass


class DataPacketReceiver(abc.ABC):
    def receive(self, data_packet: RemoteDataPacket) -> None:
        pass


class DeviceEventNotifier(abc.ABC):
    def ping_received(self, device: "RobotDevice") -> None:
        pass


class ComponentValueChangeListener(abc.ABC):
    def component_value_changed(self, component_value: "ComponentValue") -> None:
        pass


class ConnectionListener(abc.ABC):
    def connect(self, *args):
        pass

    def disconnect(self, *args):
        pass


class CurrentSensorChangeNotifier(abc.ABC):
    # public interface CurrentSensorChangeNotifier extends ComponentChangeNotifier
    def current_value_changed(self, current: "CurrentSensor") -> None:
        pass


class CurrentSensorSetupChangeNotifier(abc.ABC):
    # CurrentSensorSetupChangeNotifier extends ComponentSettingsChangeNotifier
    def current_threshold_changed(self, current: "CurrentSensor") -> None:
        pass

    def current_window_size_changed(self, current: "CurrentSensor") -> None:
        pass


class DistanceChangeNotifier(abc.ABC):
    # public interface DistanceChangeNotifier extends ComponentChangeNotifier

    def distance_changed(self, sensor: "DistanceSensor") -> None:
        pass


class LuxChangeNotifier(abc.ABC):
    # public interface LuxChangeNotifier extends AnalogDetectorChangeNotifier

    def lux_value_changed(self, sensor: "LuxSensor") -> None:
        pass


class Vcnl4000DistanceSensorSettingsChangeNotifier(abc.ABC):
    # public interface Vcnl4000DistanceSensorSettingsChangeNotifier extends ComponentSettingsChangeNotifier

    def distance_table_changed(self, sensor: "Vcnl4000DistanceSensor") -> None:
        pass
