from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Robot.Device.Protocol import DeviceProtocol

INDEX_TTL = 0

class Msg_pingResponse(RemoteMessage):
	
	def __init__(self):
		super().__init__(DeviceProtocol.MSG_PING_RESPONSE,"msgpingResponse", "response to a ping command")
		self._ttl_index = 0
		self._parameter_list.append(RemoteParameterUint8("ttl","time to live"))



	def get_command(id):
		cmd = Msg_pingResponse()
		return (cmd)


	def get_ttl(self):
		return self._parameter_list[INDEX_TTL].get_value()


"""

/**
 * 
 * @author Oktavian Gniot
 *
 *command containing new settings (gradient, offset, maximal measurable distance) for a GP2 sensor
 */

public class Msg_pingResponse extends RemoteMessage
{
	
	/**
	 * 
	 */
	private static final long serialVersionUID = 2638694167468005642L;



	protected static final String name = "pingResponse";
	protected static final String description = "response to a ping command";


	private static final int INDEX_TTL			= 0;


public void setData(int nodeType)
{
	(( RemoteParameterUint8) this.get(Msg_pingResponse.INDEX_TTL)).setValue(nodeType);
}






public static Msg_pingResponse getCommand(int id)
{
	Msg_pingResponse cmd;
	cmd = new Msg_pingResponse(id);
	
	return(cmd);
}



public static Msg_pingResponse getCommand(int command, int ttl)
{

	Msg_pingResponse cmd;
	cmd = Msg_pingResponse.getCommand(command);
	cmd.setData(ttl);
	
	return(cmd);
}


}

"""