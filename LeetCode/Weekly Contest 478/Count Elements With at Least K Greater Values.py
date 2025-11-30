from bisect import bisect_right
from typing import List


class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        n = len(nums)
        nums.sort()

        if k == 0:
            return n

        ans = 0

        for i in range(n):
            idx = bisect_right(nums, nums[i])

            if idx < n and (n - idx >= k):
                ans += 1

        return ans