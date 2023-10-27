

class ComStatistic:
    chars_sent_count = 0
    chars_recived_count = 0
    chars_dropped_count = 0

    packet_sent_count = 0
    packet_recived_count = 0
    packet_dropped_count = 0
    packet_error_count = 0

    in_chars_per_seconds = 0
    out_chars_per_seconds = 0

    def __init__(self):
        pass

    def get_throughput(self):
        char_in = self.get_recived_chars_count()
        char_out = self.get_send_chars_count()

        self.in_chars_per_seconds = char_in - self.last_chars_recived
        self.out_chars_per_seconds = char_out - self.last_chars_send

        self.last_chars_recived = char_in
        self.last_chars_send = char_out

    def get_recived_chars_count(self):
        return self.chars_recived_count

    def get_send_chars_count(self):
        return self.chars_sent_count

    def count_up_recived_chars(self, count):
        self.chars_recived_count += count

    def count_up_sent_chars(self, count):
        self.chars_sent_count += count

    def get_sent_packets_count(self):
        return self.packet_sent_count

    def count_up_sent_packet_chars(self, count):
        self.packet_sent_count += count

    def get_recived_packets_count(self):
        return self.packet_recived_count

    def count_up_recived_packets(self, count):
        self.packet_recived_count += count

    def get_dropped_packets_count(self):
        return self.packet_dropped_count

    def count_up_dropped_packets(self, count):
        self.packet_dropped_count += count

    def get_error_packets_count(self):
        return self.packet_error_count

    def count_up_error_packets(self, count):
        self.packet_error_count += count

    def get_in_chars_per_second(self):
        """ "get amount of chars received in last second" """
        return self.in_chars_per_seconds

    def get_out_chars_per_second(self):
        """ "get amount of chars send in last second" """
        return self.out_chars_per_seconds
