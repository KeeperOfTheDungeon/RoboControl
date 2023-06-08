from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.RemoteCommand import RemoteCommand

INDEX_TTL = 0


class Cmd_ping(RemoteCommand):
    def __init__(self, id):
        super().__init__(id, "ping", " send ping")
        self._ttl_index = 0
        self._parameter_list.append(RemoteParameterUint8("ttl", "time to live"))

    def set_ttl(self, ttl):
        self._parameter_list[INDEX_TTL].set_value(ttl)

    def get_command(id):
        cmd = Cmd_ping(id)
        cmd.set_ttl(10)
        return cmd


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
