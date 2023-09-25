from RoboControl.Robot.Device.control.DataAquisator import DataAquisator

# "command for aquisation of device cpu status"
AQUISATE_CPU_STATUS = 1
# "command for aquisation of device com system status"
AQUISATE_COM_STATUS = 2


class DeviceAquisators:
    """ "defines aquisition commands for generic device"  """

    @staticmethod
    def get_data_aquisators():
        return [
            DataAquisator("cpu status", 100, AQUISATE_CPU_STATUS),
            DataAquisator("com status", 100, AQUISATE_COM_STATUS),
        ]
