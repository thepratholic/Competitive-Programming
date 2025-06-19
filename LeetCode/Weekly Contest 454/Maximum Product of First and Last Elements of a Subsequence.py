from typing import List
from sortedcontainers import SortedSet

class Solution:
    def maximumProduct(self, nums: List[int], m: int) -> int:
        ans = float("-inf")
        n = len(nums)

        if m == 1:
            for i in nums:
                ans = max(ans, i * i)
            return ans

        valid = SortedSet()

        for i in range(m - 1, n):
            valid.add(nums[i - (m - 1)])
            mx, mn = valid[-1], valid[0]
            ans = max(ans, nums[i] * mx)
            ans = max(ans, nums[i] * mn)
        return ans