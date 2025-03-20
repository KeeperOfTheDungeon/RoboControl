#imagine having typing module support to write
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
#comsystem/routing/inc/com_routing.h
class RoutingTable:
    def __init__(self):
        self.routing_entries : list[RoutingEntry]


#has node limit 
#comsystem/routing/inc/com_routing.h
#framework\comSystem\routing\inc\com_routingDataHub.h
class RoutingTableDataHub(RoutingTable):
    def __init__(self):
        super().__init__()

    def insert(self, node_adress, interface_id):
        """node adress is the element index in entry list"""
        pass

    def get_interface_by_node_adress(node_adress):
        """node adress is the element index in entry list"""
        pass

    def get_interface_by_node_id(node_id):
        pass

    def get_node_id(node_adress):
        """node adress is the element index in entry list"""
        pass
    
    def get_interface_id(node_adress):
        """node adress is the element index in entry list"""
        pass

# has node limit
#comsystem/routing/inc/com_routing.h
# framework\comSystem\routing\inc\com_routingNode.h
class RoutingTableNode(RoutingTable):
    def __init__(self):
        super().__init__()

    def insert(self, node_adress, interface_id):
        pass
    
    def get_interface_by_node_adress(node_adress):
        """node adress is the element index in entry list"""
        pass

#comsystem/routing/inc/com_routing.h
class RoutingTableEndpoint(RoutingTable):
    def __init__(self):
        super().__init__()



#comsystem/routing/inc/com_routing.h
class RoutingType:
    HUB = 0
    NODE = 1
    ENDPOINT = 2

#comsystem/routing/inc/com_routing.h
class RoutingClassLookUp:
    map = {
        RoutingType.HUB : RoutingTableDataHub,
        RoutingType.NODE : RoutingTableNode,
        RoutingType.ENDPOINT : RoutingTableEndpoint
    }
    
    @staticmethod 
    def get_class(t : int):
        """returns routing class based on RoutingType"""
        try:
            return RoutingClassLookUp.map[t]
        except KeyError:
            raise RuntimeError("routing type does not exist")
        

