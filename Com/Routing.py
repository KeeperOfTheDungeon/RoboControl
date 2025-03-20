


# NODEID.h
# comsystem/routing/inc/com_routing.h

class RoutingConst:
    INVALID_COM_ADRESS = 0xff
    UNREACHED_COM_ADRESS = 0xfe
    INVALID_COM_INTERFACE = 0xff

    NODE_ID_INVALID = 0xff
    
    NODE_ADRESS_DATA_HUB = 0
    NODE_ADRESS_MOTION_CONTROLLER = 10
    NODE_ADRESS_HEAD_CAMERA = 7
    NODE_ADDRESS_HEAD_SENSORS = 11
    NODE_ADDRESS_IMU_BOARD = 12

    NODE_TYPE_DATA_HUB = 0
    NODE_TYPE_HEAD_CAMERA = 7
    NODE_TYPE_MOTION_CONTROLLER = 10
    NODE_TYPE_HEAD_SENSORS = 11
    NODE_TYPE_IMU_BOARD = 12

class RoutingEntry:
    def __init__(self, node_id, interface_id):
        self.node_id : int = node_id
        self.interface_id: int = interface_id

    
#comsystem/routing/inc/com_routing.h
#comsystem/routing/inc/com_routing.h
class RoutingTable:
    def __init__(self):
        self.routing_entries : list[RoutingEntry]

    def insert(self):
        raise NotImplementedError()
    
    def get_interface_by_node_adress(node_adress):
        raise NotImplementedError()
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

    def set_node_at_id(node_adres, node_id):
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
#framework\comSystem\routing\inc\com_routingEndpoint.h
class RoutingTableEndpoint(RoutingTable):
    def __init__(self):
        super().__init__()

    def get_interface_by_node_id(node_id):
        pass
    
    def get_interface_by_node_adress(node_adress):
        """node adress is the element index in entry list"""
        pass
    


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
        

