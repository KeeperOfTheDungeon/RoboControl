from typing import List

from RoboControl.Robot.Component.Actor.ActorProtocol import ActorProtocol
from RoboControl.Robot.Component.Actor.Led.protocol.Cmd_getLedBrightness import Cmd_getLedBrightness
from RoboControl.Robot.Component.Actor.Led.protocol.Cmd_setLedBrightness import Cmd_setLedBrightness
from RoboControl.Robot.Device.remoteProcessor.RemoteDecoder import RemoteDecoder
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor


class LedProtocol(ActorProtocol):
    def get_command_processors(self, remote_decoder: RemoteDecoder) -> List[RemoteProcessor]:
        """ "get led command processors"
        @:param "remoteDecoder barometric sensor set"
        @:return "commands processors for barometric sensor"
        """
        commands = super().get_command_processors(remote_decoder)
        for cmd in [
            RemoteProcessor(Cmd_setLedBrightness(self._cmd_set_value_id), remote_decoder),
            RemoteProcessor(Cmd_getLedBrightness(self._cmd_get_value_id), remote_decoder),
        ]:
            commands.append(cmd)
        return commands

    def get_stream_processors(self, remote_decoder: RemoteDecoder) -> List[RemoteProcessor]:
        """ "get led stream processors"
        @:param "remoteDecoder led set"
        @:return "stream processors for led"
        """
        commands = super().get_stream_processors(remote_decoder)
        # commands.append( Stream_barometricPressures(self.streamValuesId, sensor) )
        return commands

    def get_message_processors(self, remote_decoder: RemoteDecoder) -> List[RemoteProcessor]:
        """ "get led message processors"
        @:param "remoteDecoder led set"
        @:return "message processors for led"
        """
        commands = super().get_message_processors(remote_decoder)
        # commands.append( Msg_ledBrightness(self.msgValueId, sensorSet) )
        return commands
