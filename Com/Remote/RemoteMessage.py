from RoboControl.Com.Remote.RemoteData import RemoteData

class RemoteMessage(RemoteData):
  
    def __init__(self, id,name, description):
        super().__init__(id, name, description)
        
 