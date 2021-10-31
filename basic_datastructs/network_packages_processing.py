import sys
from collections import deque


class NetworkPacketHandler:
    def __init__(self, size):
        self._buffer_size = size
        self._buffer = deque()
        self._start_times = []

    def _packet_handling(self, packet):
        """Average time complexity: O(1)
        Worst time complexity: O(n), where n = len(self._buffer) at the time of the function call
        """
        # Packets that have already been handled before the arrival of a new packet
        while self._buffer and self._buffer[0] <= packet.get('arrival'):
            self._buffer.popleft()  # are removed from the buffer

        if len(self._buffer) < self._buffer_size:
            self._buffer.append(packet.get('finish'))
            self._start_times.append(packet.get('start'))
        else:
            self._start_times.append(-1)

    def packet_arrival(self, packet):
        """Average time complexity: O(1)
        Worst time complexity: O(n), where n = len(self._buffer) at the time of the function call
        """
        arrival, duration = (int(i) for i in packet)
        start_time = max(self._buffer[-1], arrival) if self._buffer else arrival
        finish_time = start_time + duration

        packet = {'arrival': arrival, 'start': start_time, 'finish': finish_time}
        self._packet_handling(packet)

    def packet_handling_start_times(self):
        """Time complexity: O(1)"""
        return self._start_times


def network_packets_handling(size, packets):
    """Time complexity: O(n), where n = len(packets)"""
    handler = NetworkPacketHandler(size)
    for packet in packets:
        handler.packet_arrival(packet)

    return handler.packet_handling_start_times()


def main():
    size, n_ = (int(i) for i in input().split())
    packets = [tuple(line.split()) for line in sys.stdin.readlines()]

    start_times = network_packets_handling(size, packets)
    print(*start_times, sep='\n')


if __name__ == '__main__':
    main()