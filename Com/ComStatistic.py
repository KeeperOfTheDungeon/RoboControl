import threading
# disabled for micropython  # from typing import TypeAlias

import sched
import time

# disabled for micropython  # "long": TypeAlias = int


class ComStatistic:
    chars_sent_count: "long" = 0
    chars_recived_count: "long" = 0
    chars_dropped_count: "long" = 0

    packet_sent_count: "long" = 0
    packet_recived_count: "long" = 0
    packet_dropped_count: "long" = 0
    packet_error_count: "long" = 0

    in_chars_per_seconds: "long" = 0
    out_chars_per_seconds: "long" = 0

    def __init__(self):
        self._scheduler = None  # self._run_timer()

    def _run_timer(self):
        my_scheduler = sched.scheduler(time.time, time.sleep)

        class TimerClass:
            last_chars_send = 0
            last_chars_recived = 0

            def update(inner_self) -> None:
                print("hey")
                char_in = self.get_recived_chars_count()
                char_out = self.get_send_chars_count()

                self.in_chars_per_seconds = char_in - inner_self.last_chars_recived
                self.out_chars_per_seconds = char_out - inner_self.last_chars_send

                inner_self.last_chars_recived = char_in
                inner_self.last_chars_send = char_out

        tc = TimerClass()
        my_scheduler.enter(60, 1, tc.update, (my_scheduler,))  # timer.scheduleAtFixedRate(TimerClass(), 1000, 1000)
        t = threading.Thread(target=my_scheduler.run, args=())
        t.start()
        return my_scheduler

    def get_recived_chars_count(self) -> "long":
        return self.chars_recived_count

    def get_send_chars_count(self) -> "long":
        return self.chars_sent_count

    def count_up_recived_chars(self, count: int = 1) -> None:
        self.chars_recived_count += count

    def count_up_sent_chars(self, count: int = 1) -> None:
        self.chars_sent_count += count

    def get_sent_packets_count(self) -> "long":
        return self.packet_sent_count

    def count_up_sent_packet_chars(self, count: int = 1) -> None:
        self.packet_sent_count += count

    def get_recived_packets_count(self) -> "long":
        return self.packet_recived_count

    def count_up_recived_packets(self, count: int = 1) -> None:
        self.packet_recived_count += count

    def get_dropped_packets_count(self) -> "long":
        return self.packet_dropped_count

    def count_up_dropped_packets(self, count: int = 1) -> None:
        self.packet_dropped_count += count

    def get_error_packets_count(self) -> "long":
        return self.packet_error_count

    def count_up_error_packets(self, count: int = 1) -> None:
        self.packet_error_count += count

    def get_in_chars_per_second(self) -> "long":
        """ "get amount of chars received in last second" """
        return self.in_chars_per_seconds

    def get_out_chars_per_second(self) -> "long":
        """ "get amount of chars send in last second" """
        return self.out_chars_per_seconds
