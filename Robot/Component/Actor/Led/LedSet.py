from RoboControl.Robot.Component.Actor.Led.Led import Led
from RoboControl.Robot.Component.ComponentSet import ComponentSet

#unused
class LedSet(ComponentSet):
    def __init__(self, components, protocol):
        actors = list()
        for component in components:
            actor = Led(component)
            actors.append(actor)

        super().__init__(actors)



    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list


    def get_message_processors(self):
        msg_list = super().get_message_processors()
        return msg_list


    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        return stream_list



"""package de.hska.lat.robot.component.actor.led;



/**
 * 
 * @author Oktavian Gniot
 *
 * 
 *
 */

public class LedSet extends ComponentSet<Led, LedProtocol> {


protected LedSet()
{
}	


public LedSet(ArrayList<ComponentMetaData> leds, LedProtocol protocol)
{

        
    for (ComponentMetaData led: leds)
    {
        this.add(new Led(led, protocol));
    }
    

    
}






}
"""