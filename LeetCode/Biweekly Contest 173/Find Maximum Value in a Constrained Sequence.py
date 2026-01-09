from typing import List


class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        INF = 10**18
        limit = [INF] * n

        limit[0] = 0
        for idx, maxVal in restrictions:
            limit[idx] = maxVal

        for i in range(1, n):
            limit[i] = min(limit[i], limit[i - 1] + diff[i - 1])

        for i in range(n - 2, -1, -1):
            limit[i] = min(limit[i], limit[i + 1] + diff[i])

        return max(limit)