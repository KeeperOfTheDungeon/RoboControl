from RoboControl.Com.Remote.Parameter.RemoteParameterUint8 import RemoteParameterUint8
from RoboControl.Com.Remote.Parameter.RemoteParameterUint32 import RemoteParameterUint32
from RoboControl.Com.Remote.RemoteStream import RemoteStream

INDEX_ACTUAL_CPU_LOAD = 0
INDEX_MIN_CPU_LOAD = 1
INDEX_MAX_CPU_LOAD = 2


class Stream_cpuStatistics(RemoteStream):

    def __init__(self, id):
        super().__init__(id, "cpuStatus", "status of the cpu containing values for min max and last cycle duration")

        self._parameter_list.append(RemoteParameterUint8("min", "min load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("max", "max load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("actual", "actual load of the device cpu"))
        self._parameter_list.append(RemoteParameterUint8("status", "actual status of the device cpu"))

        self.set_id(id)

    def get_last_load(self):
        return self._parameter_list[INDEX_ACTUAL_CPU_LOAD].get_value()

    def get_min_load(self):
        return self._parameter_list[INDEX_MIN_CPU_LOAD].get_value()

    def get_max_load(self):
        return self._parameter_list[INDEX_MAX_CPU_LOAD].get_value()


"""
	

	private static final int INDEX_MIN_CPU_LOAD 		= 0;
	private static final int INDEX_ACTUAL_CPU_LOAD	 	= 1;
	private static final int INDEX_MAX_CPU_LOAD 		= 2;
	private static final int INDEX_CPU_STATUS	 		= 3;
	
	protected static final String name = "cpuStatus";
	protected static final String description = "status of the cpu containing values for min max and last cycle duration";
	
	


public Stream_cpuStatistics(int command)
{
	this();
	this.setId(command);
}



public void setData(int minLoad,int maxLoad,int currentLoad, int status)
{
	(( RemoteParameterUint8) this.get(Stream_cpuStatistics.INDEX_MIN_CPU_LOAD)).setValue(minLoad);
	(( RemoteParameterUint8) this.get(Stream_cpuStatistics.INDEX_MAX_CPU_LOAD)).setValue(maxLoad);
	(( RemoteParameterUint8) this.get(Stream_cpuStatistics.INDEX_ACTUAL_CPU_LOAD)).setValue(currentLoad);
	(( RemoteParameterUint8) this.get(Stream_cpuStatistics.INDEX_CPU_STATUS)).setValue(status);
}

public static Stream_cpuStatistics getCommand(int command)
{
	Stream_cpuStatistics cmd;
	cmd = new Stream_cpuStatistics(command);
	
	return(cmd);
}

public static Stream_cpuStatistics getCommand(int command,int minLoad, int maxLoad, int currentLoad, int status)
{
	Stream_cpuStatistics cmd;
	cmd = Stream_cpuStatistics.getCommand(command);
	cmd.setData(minLoad, maxLoad,currentLoad ,status );
	
	return(cmd);
}

	
}
"""
