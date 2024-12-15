from typing import List


class Solution:
    def buttonWithLongestTime(self, events: List[List[int]]) -> int:
        max_unit_time = events[0][1]
        resIndex = events[0][0]

        for i in range(1, len(events)):
            timeTaken = events[i][1] - events[i-1][1]

            if timeTaken > max_unit_time or (timeTaken == max_unit_time and events[i][0] < resIndex):
                resIndex = events[i][0]
                max_unit_time = timeTaken

        return resIndex
