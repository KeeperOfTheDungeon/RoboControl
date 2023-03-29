
class RemoteProcerssorList(list):




	def find_on_id(self, id):
		for processor in self:
			if processor.has_remote_id(id):
				return processor
		
		return None

"""package de.hska.lat.robot.device.device.remoteProcessor;

import java.util.ArrayList;




//public class RemoteProcessorList<R extends RemoteData_new,E extends RemoteExecutor<R>,P extends RemoteProcessor<?, ?>>
public class RemoteProcessorList<P extends RemoteProcessor<?>>
//
{

	protected ArrayList<P> remoteList = new ArrayList<P>();
	

/**
 * add a remote processor to processor list
 * @param remoteProcessor remote processor to be added
 */
	
public void add(P remoteProcessor)
{
	this.remoteList.add(remoteProcessor);
}
	
	
/**
 * add remote processors to list	
 * @param remoteProcessorList list with remote processors
 */
public void addAll(ArrayList<P>  remoteProcessorList)
{
	for (P processor:  remoteProcessorList )
	{
		this.remoteList.add(processor);
	}
}




public P findOnId(int id)
{
	
	for (P processor: this.remoteList)
	{
		if (processor.hasRemoteId(id))
		{
			return(processor);
		}
	}
	
	// TODO Auto-generated method stub
	return(null);
}


}
"""