# import copy
import traceback
from typing import Optional

from RoboControl.Com.Remote.RemoteCommand import RemoteCommand
from RoboControl.Com.Remote.RemoteCommandDataPacket import RemoteCommandDataPacket
from RoboControl.Com.Remote.RemoteData import RemoteData
from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket
from RoboControl.Com.Remote.RemoteExceptionDataPacket import RemoteExceptionDataPacket
from RoboControl.Com.Remote.RemoteMessage import RemoteMessage
from RoboControl.Com.Remote.RemoteMessageDataPacket import RemoteMessageDataPacket
from RoboControl.Com.Remote.RemoteStream import RemoteStream
from RoboControl.Com.Remote.RemoteStreamDataPacket import RemoteStreamDataPacket
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessor import RemoteProcessor
from RoboControl.Robot.Device.remoteProcessor.RemoteProcessorList import RemoteProcessorList


class RemotePacketHandler:
    def __init__(self):
        self._command_processor_list = RemoteProcessorList()
        self._message_processor_list = RemoteProcessorList()
        self._stream_processor_list = RemoteProcessorList()
        self._exception_processor_list = RemoteProcessorList()

    def add_stream_processor(self, stream: RemoteStream, handler) -> "RemotePacketHandler":
        processor = RemoteProcessor(stream, handler)
        self._stream_processor_list.append(processor)
        return self

    def add_stream_processor_list(self, processor_list: RemoteProcessorList) -> "RemotePacketHandler":
        self._stream_processor_list.extend(processor_list)
        return self

    def add_command_processor(self, command: RemoteCommand, handler) -> "RemotePacketHandler":
        processor = RemoteProcessor(command, handler)
        self._command_processor_list.append(processor)
        return self

    def add_command_processor_list(self, processor_list: RemoteProcessorList) -> "RemotePacketHandler":
        self._command_processor_list.extend(processor_list)
        return self

    def add_message_processor(self, message: RemoteMessage, handler) -> "RemotePacketHandler":
        processor = RemoteProcessor(message, handler)
        self._message_processor_list.append(processor)
        return self

    def add_message_processor_list(self, processor_list: RemoteProcessorList) -> "RemotePacketHandler":
        self._message_processor_list.extend(processor_list)
        return self

    def _find_processor(self, data_packet: RemoteDataPacket, remote_id: int) -> Optional[RemoteProcessor]:
        if isinstance(data_packet, RemoteCommandDataPacket):
            # print ("ARD : Command Prozessor", processor)
            return self._command_processor_list.find_on_id(remote_id)
        elif isinstance(data_packet, RemoteMessageDataPacket):
            return self._message_processor_list.find_on_id(remote_id)
        elif isinstance(data_packet, RemoteStreamDataPacket):
            return self._stream_processor_list.find_on_id(remote_id)
        elif isinstance(data_packet, RemoteExceptionDataPacket):
            return self._exception_processor_list.find_on_id(remote_id)
        print("unsuported data packet type")
        return None

    def parse_data_packet(self, data_packet: RemoteDataPacket) -> Optional[RemoteData]:
        # print ("ARD : ParseDataPAcket", query_id, data_packet)
        remote_id = data_packet.get_command()
        processor = self._find_processor(data_packet, remote_id)
        if processor is not None:
            try:
                remote_data = processor.get_remote_data()
                remote_data.parse_data_packet(data_packet)
                data_packet.set_remote_data(remote_data)
                processor.execute(remote_data)
                return remote_data
            except Exception as e:
                print(traceback.format_exc())
                traceback.print_exception(e)
        return None
