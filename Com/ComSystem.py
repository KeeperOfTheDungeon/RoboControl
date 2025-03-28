# framework\comSystem\inc\com_statusCodes.h
class ComStatusCodes:
    CSSC_OK = 0
    CSSC_FAIL = -1
    CSSC_INVALID_PACKET_SIZE = -100
    CSSC_INVALID_COMMAND = -101
    CSSC_WRONG_HEX_NUMBER = -102

# framework\comSystem\inc\com_channel.h
class ComChannel: # ??? Connection


# framework\comSystem\com_system.c
class ComSystemStatus:
    connectedToMainHub = False

class ComChannelConfigData:

# framework\comSystem\com_system.c
# framework\comSystem\inc\com_system.h
class ComSystem:

    def __init__(self, channelConfigData: list[ChannelConfigData]):
        self.undeliverablePackets = 0
        
        self.status = ComSystemStatus
        self.com_channels = []