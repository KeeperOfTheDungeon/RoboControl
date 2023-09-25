from RoboControl.Robot.Component.Actor.Led.Led import Led
from RoboControl.Robot.Component.ComponentSet import ComponentSet


# unused
class LedSet(ComponentSet):
    def __init__(self, components, protocol):
        # TODO why typecast here?
        super().__init__(
            [Led(component) for component in components]
        )

    def get_command_processors(self):
        command_list = super().get_command_processors()
        return command_list

    def get_message_processors(self):
        msg_list = super().get_message_processors()
        return msg_list

    def get_stream_processors(self):
        stream_list = super().get_stream_processors()
        return stream_list
