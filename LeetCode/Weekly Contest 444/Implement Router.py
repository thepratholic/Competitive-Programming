from collections import deque
import bisect
from typing import List

class Router:
    def __init__(self, memoryLimit: int):
        self.memoryLimit = memoryLimit
        self.storage = deque()
        self.packet_set = set()
        self.dest_map = {}

    def addPacket(self, source: int, destination: int, timestamp: int) -> bool:
        packet = (source, destination, timestamp)
        if packet in self.packet_set:
            return False
        if len(self.storage) >= self.memoryLimit:
            self._remove_oldest()
        self.storage.append(packet)
        self.packet_set.add(packet)
        if destination not in self.dest_map:
            self.dest_map[destination] = []
        self.dest_map[destination].append(timestamp)
        return True

    def forwardPacket(self) -> List[int]:
        if not self.storage:
            return []
        packet = self.storage.popleft()
        source, destination, timestamp = packet
        self.packet_set.remove(packet)
        ts_list = self.dest_map[destination]
        idx = bisect.bisect_left(ts_list, timestamp)
        if idx < len(ts_list) and ts_list[idx] == timestamp:
            ts_list.pop(idx)
        if not ts_list:
            del self.dest_map[destination]
        return [source, destination, timestamp]

    def getCount(self, destination: int, startTime: int, endTime: int) -> int:
        if destination not in self.dest_map:
            return 0
        ts_list = self.dest_map[destination]
        left_index = bisect.bisect_left(ts_list, startTime)
        right_index = bisect.bisect_right(ts_list, endTime)
        return right_index - left_index

    def _remove_oldest(self):
        if self.storage:
            packet = self.storage.popleft()
            source, destination, timestamp = packet
            self.packet_set.remove(packet)
            ts_list = self.dest_map[destination]
            idx = bisect.bisect_left(ts_list, timestamp)
            if idx < len(ts_list) and ts_list[idx] == timestamp:
                ts_list.pop(idx)
            if not ts_list:
                del self.dest_map[destination]

# Example object creation and testing:
# if __name__ == "__main__":
#     router = Router(3)
#     print(router.addPacket(1, 4, 90))
#     print(router.addPacket(2, 5, 90))
#     print(router.addPacket(1, 4, 90))
#     print(router.addPacket(3, 5, 95))
#     print(router.addPacket(4, 5, 105))
#     print(router.forwardPacket())
#     print(router.addPacket(5, 2, 110))
#     print(router.getCount(5, 100, 110))
