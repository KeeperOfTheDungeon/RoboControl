# framework\comSystem\inc\com_statusCodes.h
class ComStatusCodes:
    CSSC_OK = 0
    CSSC_FAIL = -1
    CSSC_INVALID_PACKET_SIZE = -100
    CSSC_INVALID_COMMAND = -101
    CSSC_WRONG_HEX_NUMBER = -102

class ComSystemStatus:
    connectedToMainHub = 0

# framework\comSystem\com_system.c
# framework\comSystem\inc\com_system.h
class ComSystem:
    status = ComSystemStatus

    