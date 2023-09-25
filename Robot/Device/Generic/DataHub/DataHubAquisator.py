# "command for aquisation of data hub cpu status"
AQUISATE_CPU_STATUS = 1
# "command for aquisation of data hub com system status"
AQUISATE_COM_STATUS = 2


class DataHubAquisator:
    """ "defines aquisition commands for generic data hub"  """

    @staticmethod
    def get_aquisators():
        return [
            DataAquisator("cpu status", 100, AQUISATE_CPU_STATUS),
            DataAquisator("com status", 100, AQUISATE_COM_STATUS),
        ]
