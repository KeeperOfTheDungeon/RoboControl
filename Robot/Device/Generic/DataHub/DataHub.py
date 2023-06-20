from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Robot.Device.Protocol.DeviceProtocol import DeviceProtocol
from RoboControl.Robot.Device.RobotDevice import RobotDevice


class DataHub(RobotDevice):

    def build(self):
        self._protocol = DeviceProtocol(self)


"""
package de.hska.lat.robot.device.generic.dataHub;




import java.util.ArrayList;

import de.hska.lat.robot.component.ComponentMetaData;
import de.hska.lat.robot.component.text.Text;
import de.hska.lat.robot.component.text.TextSet;
import de.hska.lat.robot.device.DeviceEventNotifier;
import de.hska.lat.robot.device.RobotDevice;
import de.hska.lat.robot.device.protocol.Msg_pingResponse;




public class DataHub  extends RobotDevice<DeviceEventNotifier, DataHubProtocol> {

    
    public static final String NAME = "DataHub";
    public static final String ROBOT_NAME = "name";
    public static final int ID = 0;
    
    protected TextSet texts;
    
    
public DataHub(ArrayList<ComponentMetaData> metaData) 
{
    super(DataHub.NAME, DataHub.ID);
    aquisators= DataHubAquisator.aquisators;
    
    
    this.addTexts(metaData);
    
    this.protocol=new DataHubProtocol(this);
    
}



protected void addTexts(ArrayList<ComponentMetaData> texts)
{

    
    this.texts = new TextSet(texts,DataHubProtocol.getTextProtocol(this.getId()));
    
    for (Text text : this.texts)
    {
        this.componentList.add(text);
    }
    
    this.setList.add(this.texts);

}
 


@Override
protected void processPingResponse(Msg_pingResponse remoteMessage)
{
    super.processPingResponse(remoteMessage);
    
    
}


/**
 * Get this data hub texts
 * @return
 */
public TextSet getTexts()
{
    return(this.texts);
    
}



@Override
public void loadSetup()
{
    for(Text text : this.texts)
    {
        text.remote_getText();
    }
}




}
"""
