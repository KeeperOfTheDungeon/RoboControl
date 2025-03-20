


# NODEID.h
# comsystem/routing/inc/com_routing.h
# board.h
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
    
    # com_config.h TODO: device config pass through that gets used here (e.g. pico 2x uart)
    MAX_NODES = 50
    COM_INTERFACE_COUNT = 2 
    DATA_PACKET_POOL_SIZE = 20
    DATA_PACKET_PAYLOAD_SIZE = 40
    MAX_DATA_POINTS = 255 # used for RoutingTableNode entry count

    COM_DEFAULT_UP_INTERFACE = 0
class RoutingEntry:
    def __init__(self, node_id = None, interface_id = None):
        self.node_id : int | None = node_id
        self.interface_id: int | None = interface_id

# framework\comSystem\routing\inc\com_routingNode.h
class RoutingEntryNode:
    def __init__(self, adress = None, interface_id = None):
        self.adress : int | None = adress
        self.interface_id: int | None = interface_id

    
#comsystem/routing/inc/com_routing.h
class RoutingTable:
    def __init__(self):
        self.routing_entries : list[RoutingEntry]= [RoutingEntry(RoutingConst.NODE_ID_INVALID, RoutingConst.INVALID_COM_INTERFACE) for _ in range(RoutingConst.MAX_NODES)]

    def insert(self):
        raise NotImplementedError()
    
    def get_interface_by_node_adress(node_adress):
        raise NotImplementedError()
    
# comsystem/routing/inc/com_routing.h
# framework\comSystem\routing\inc\com_routingDataHub.h
# framework\comSystem\routing\com_routingDataHub.c
class RoutingTableDataHub(RoutingTable):
    def __init__(self):
        super().__init__()

    def insert(self, node_adress, interface_id):
        """node adress is the element index in entry list"""
        if self.routing_entries[node_adress].interface_id != interface_id:
            self.routing_entries[node_adress] != interface_id
            self.routing_entries[node_adress].node_id = RoutingConst.NODE_ID_INVALID
            self.routing_entries[node_adress].interface_id = interface_id


    def get_interface_by_node_adress(self, node_adress):
        """node adress is the element index in entry list"""
        return self.routing_entries[node_adress].interface_id

    def get_interface_by_node_id(self, node_id):
        return next((entry.interface_id for entry in self.routing_entries if entry.node_id == node_id), -1)

    def get_node_id(self, node_adress):
        """node adress is the element index in entry list"""
        return self.routing_entries[node_adress].node_id
    
    def get_interface_id(self, node_adress):
        """node adress is the element index in entry list"""
        self.routing_entries[node_adress].interface_id

    def set_node_at_adress(self, node_adress, new_node_id):
        self.routing_entries[node_adress].node_id = new_node_id

#comsystem/routing/inc/com_routing.h
# framework\comSystem\routing\inc\com_routingNode.h
# framework\comSystem\routing\com_routingNode.c
class RoutingTableNode(RoutingTable):
    def __init__(self):
        self.routing_entries : list[RoutingEntryNode]= [RoutingEntryNode(RoutingConst.INVALID_COM_ADRESS, RoutingConst.INVALID_COM_INTERFACE) for _ in range(RoutingConst.MAX_DATA_POINTS)]


    def insert(self, node_adress, interface_id):
        if interface_id == RoutingConst.COM_DEFAULT_UP_INTERFACE:
            return
        
        for entry in self.routing_entries:
            if entry.adress == node_adress:
                entry.interface_id = interface_id
                return
            if entry.adress == RoutingConst.INVALID_COM_ADRESS:
                entry.adress = node_adress
                entry.interface_id = interface_id
                return
        
    
    def get_interface_by_node_adress(self, node_adress):
        """node adress is the element index in entry list"""
        return next((entry.interface_id for entry in self.routing_entries if entry.adress == node_adress), RoutingConst.COM_DEFAULT_UP_INTERFACE)

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
        

