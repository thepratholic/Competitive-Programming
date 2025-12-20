import heapq
from typing import List


class Solution:
    def maximumScore(self, nums: List[int], s: str) -> int:
        n = len(nums)

        pq = []
        ans = 0
        for i in range(n):
            heapq.heappush(pq, -nums[i])

            if s[i] == '1':
                v = heapq.heappop(pq)
                v = -v
                ans += v

        return ans