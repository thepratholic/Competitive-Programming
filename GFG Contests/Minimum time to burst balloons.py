from typing import List

class Solution:
    def minTime(self, k : int, positions : List[int]) -> int:
        #code here

        positions.sort()

        n = len(positions)
        min_time = float('inf')

        for i in range(n - k + 1):
            left = positions[i]
            right = positions[i + k - 1]

            time1 = abs(left) + (right - left)

            time2 = abs(right) + (right - left)

            min_time = min(min_time, time1, time2)

        return min_time