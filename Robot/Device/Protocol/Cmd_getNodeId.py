from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

INDEX_TTL = 0


class Cmd_getNodeId(RemoteCommand):

    def __init__(self, id):
        super().__init__(id, "getNodeId", " get destinations node id ")

    def get_command(id):
        cmd = Cmd_getNodeId(id)
        cmd.set_id(DeviceProtocol.CMD_GET_NODE_ID)
        return (cmd)


"""
public class Cmd_ping extends RemoteCommand
{
	
	
public Cmd_ping() 
{
	this.add(new RemoteParameterUint8("ttl","time to live"));
}


public Cmd_ping(int command) 
{
	this();
	this.setId(command);
}



@Override
public String getName() 
{
	return(Cmd_ping.name);
}


@Override
public String getDescription() 
{
	return(Cmd_ping.description);
}



public static Cmd_ping getCommand(int command)
{
	Cmd_ping cmd;
	cmd = new Cmd_ping(command);
	cmd.setTtl(10);
	
	return(cmd);
}


}
"""
