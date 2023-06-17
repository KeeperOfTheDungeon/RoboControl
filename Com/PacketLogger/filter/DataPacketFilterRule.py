from RoboControl.Com.Remote.RemoteDataPacket import RemoteDataPacket


class DataPacketFilterRule:
    """ "superclass for all DataPacket filters" """

    _pass_filter: bool = True

    def is_pass_filter(self) -> bool:
        """ "returns actual type of this filter (pass filter or block filter)" """
        return self._pass_filter

    def set_pass_filter(self, status: bool) -> None:
        """
        set this filter type to pass (true) or block (false) filter.
          a pass filter returns true on match when checking packets.
          block filter returns false on match when checking packets.
        :param status:
        :return:
        """
        self._pass_filter = status

    # TODO abstract
    def check(self, data_packet: RemoteDataPacket) -> bool:
        """
        "Check given RemoteMessage"

        :param data_packet:
        :return: "true when given RemoteMessage has passed this filters check, false if not"
        """
        raise ValueError("Not implemented")

    # TODO abstract
    def get_name(self) -> str:
        raise ValueError("Not implemented")
