from asyncio.windows_events import NULL
from RoboControl.Robot.AbstractRobot.AbstractRobot import AbstractRobot
from RoboView.Robot.Viewer.RobotSettings import RobotSettings


class Robot(AbstractRobot):
    def __init__(self, name):
        super().__init__()
        self._name = name

    def on_connected(self):
        super().on_connected()

        # AbstractRobotDevice<?,?> dataHub = this.deviceList.getDeviceOnId(DataHub.ID);
        # dataHub.remote_pingDevice();

        for device in self._device_list:
            device.set_transmitter(self._connection)
            device.on_connected()

    def receive(self, remote_data):
        source = remote_data.get_source_addres()
        device = self.get_device_on_id(source)

        if device is not None:
            device.receive(remote_data)
            # dataPacketLogger.addInputPacket(dataPacket);


"""
package de.hska.lat.robot;





import java.util.ArrayList;

import de.hska.lat.behavior.behavior.RobotBehavior;
import de.hska.lat.behavior.control.BehaviorControl;
import de.hska.lat.comm.remote.RemoteDataPacket;
import de.hska.lat.navigation.Destination;
import de.hska.lat.navigation.path.NavigationPath;
import de.hska.lat.perception.fieldOfView.FieldOfView;
import de.hska.lat.perception.panorama.Panorama;
import de.hska.lat.robot.abstractRobot.AbstractRobot;
import de.hska.lat.robot.abstractRobot.RobotConnectionListener;
import de.hska.lat.robot.abstractRobot.device.AbstractRobotDevice;
import de.hska.lat.robot.component.ComponentMetaData;
import de.hska.lat.robot.component.RobotComponent;
import de.hska.lat.robot.component.generic.navigator.Navigator;
import de.hska.lat.robot.device.RobotDevice;
import de.hska.lat.robot.device.generic.dataHub.DataHub;
import de.hska.lat.robot.morphology.model.MorphologicModel;
import de.hska.lat.robot.connection.Connection;
import de.hska.lat.robot.morphology.appearance.AppearanceModel;

/**
 * A instance of this class represents a robot. It contains all robot devices and provides connection for data transfer
 * between this java robot representation and real robot.
 *    
 * @author Oktavian Gniot
 *
 */

public class Robot extends AbstractRobot<Robot, RobotDevice<?,?>,RobotComponent<?,?,?>>

{


    
//	protected RobotDeviceList deviceList=new RobotDeviceList();
    
    protected MorphologicModel morphologicModel;
    protected AppearanceModel appearanceModel;
    
    
    protected ArrayList<FieldOfView<?>> fieldsOfViews = new ArrayList<FieldOfView<?>>();  
//	protected Vector<PerceptionSphere> perceptionSpheres = new Vector<PerceptionSphere>(); 
    

    protected Navigator<?> navigator;

    
    protected Destination destination = new Destination();
    protected NavigationPath navigationPath = new NavigationPath();

    protected RobotBehavior<?> behavior;

    
    
    
protected void addMainHub(ComponentMetaData nameMetaData)
{
    ArrayList<ComponentMetaData> metaData = new ArrayList<ComponentMetaData> ();
    metaData.add(nameMetaData);
    
    this.deviceList.add(new DataHub(metaData));

}



/**
 * get the name of this robots type
 * @return
 *//*
public String getTypeName()
{
    return(typeName);
}


*/


/**
 * get name of this robot
 * @return name of this robot
 */
public String getRobotName() 
{
    return (name);
}


public void addFieldOfView(FieldOfView<?> fieldOfView)
{
    this.fieldsOfViews.add(fieldOfView);
}



public FieldOfView<?> getFieldOfViewOnName(String name)
{
    
    for (FieldOfView<?> fieldOfView: this.fieldsOfViews)
    {
        if (fieldOfView.getName().equals(name))
            return(fieldOfView);
    }
    return(null);
}

/**
 * Return this Robot field of view i.e. derived robot specific field of view class
 * @return robots field of view
 */
public FieldOfView<?> getFieldOfViewOnId(int id)
{
    
    for (FieldOfView<?> fieldOfView: this.fieldsOfViews)
    {
        if (fieldOfView.hasId(id))
            return(fieldOfView);
    }
    return(null);
}







public Destination getDestination()
{
    return(this.destination);
}




public NavigationPath getNavigationPath()
{
    return(this.navigationPath);
}


/**
 * connect to remote device over given connection
 */
@Override
public void connect(Connection connection)
{
    connection.setRemote();
    super.connect(connection);
}



/**
 * called when robot gets connected to remote device , load all setup data;
 */



/**
 * called when robot gets disconnected from remote device 
 */


public void onDisconnected()
{
    
    for (RobotDevice<?,?> device : this.deviceList)
    {
        device.onDisconnected();
    }
    
    for (RobotConnectionListener listener : 	this.connectionListener)
    {
        listener.disconnected(this);
    }
}










public Panorama[] getPanoramas()
{
    // TODO Auto-generated method stub
    return null;
}



public RobotBehavior<?> getBehavior()
{
    // TODO Auto-generated method stub
    return (this.behavior);
}



public ArrayList<BehaviorControl> getControls()
{
    
    ArrayList<BehaviorControl> controlls = this.behavior.getControls();
    
     return(controlls);
}







}
"""
