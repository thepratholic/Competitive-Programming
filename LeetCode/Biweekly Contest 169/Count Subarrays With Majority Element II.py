from bisect import bisect_left
from typing import List

from sortedcontainers import SortedList


class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        a = [-1] * n

        for i in range(n):
            if nums[i] == target: a[i] = 1

        sl = SortedList()
        sl.add(0)
        ans = 0
        cur = 0

        for i in range(n):
            cur += a[i]

            idx = bisect_left(sl, cur)
            ans += idx
            sl.add(cur)

        return ans