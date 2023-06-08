from RoboControl.Com.Remote.RemoteData import RemoteData


class RemoteCommand(RemoteData):

    def __init__(self, id, name, description):
        super().__init__(id, name, description)


"""package de.hska.lat.comm.remote;





public class RemoteCommand extends RemoteData
{

	

/**
	 * 
	 */
	private static final long serialVersionUID = 8798911052489512840L;






@Override
public RemoteDataPacket getDataPacket()
{
	return(this.makeDataPacket(new RemoteCommandDataPacket(this.destination,this.source ,this.id)));
}






@Override
public String getTypeName()
{
	return ("command");
}




}"""
