#comsystem/routing/inc/com_routing.h

class RoutingMsgTypes:
    INVALID_COM_ADRESS = "0xff"
    UNREACHED_COM_ADRESS = "0xfe"
    INVALID_COM_INTERFACE = "0xff"


class RoutingEntry:
    def __init__(self, node_id, interface_id):
        self.node_id : int = node_id
        self.interface_id: int = interface_id

    
#comsystem/routing/inc/com_routing.h
class RoutingTable:
    def __init__(self):
        pass

#comsystem/routing/inc/com_routing.h
class RoutingDataHub(RoutingTable):
    pass
#comsystem/routing/inc/com_routing.h
class RoutingNode(RoutingTable):
    pass
#comsystem/routing/inc/com_routing.h
class RoutingEndpoint(RoutingTable):
    pass



#comsystem/routing/inc/com_routing.h
class RoutingType:
    HUB = 0
    NODE = 1
    ENDPOINT = 2

#comsystem/routing/inc/com_routing.h
class RoutingClassLookUp:
    map = {
        RoutingType.HUB : RoutingDataHub,
        RoutingType.NODE : RoutingNode,
        RoutingType.ENDPOINT : RoutingEndpoint
    }
    
    @staticmethod 
    def get_class(t : int):
        """returns routing class based on RoutingType"""
        try:
            return RoutingClassLookUp.map[t]
        except KeyError:
            raise RuntimeError("routing type does not exist")
        

