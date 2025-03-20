#comsystem/routing/inc/com_routing.h

class RoutingMsgTypes:
    INVALID_COM_ADRESS = "0xff"
    UNREACHED_COM_ADRESS = "0xfe"
    INVALID_COM_INTERFACE = "0xff"

class RoutingTable:
    pass

class RoutingDataHub(RoutingTable):
    pass

class RoutingNode(RoutingTable):
    pass

class RoutingEndpoint(RoutingTable):
    pass

class RoutingType:
    HUB = 0
    NODE = 1
    ENDPOINT = 2

class RoutingClassLookUp:
    map = {
        RoutingType.HUB : RoutingDataHub,
        RoutingType.NODE : RoutingNode,
        RoutingType.ENDPOINT : RoutingEndpoint
    }
    
    @staticmethod 
    def get_class(t : int):
        try:
            return map[t]
        except KeyError:
            raise RuntimeError("routing type does not exist")