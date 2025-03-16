from typing import List


class Solution:
    def maxSum(self, nums: List[int]) -> int:
        seen = set()
        n = len(nums)

        for i in range(n):
            if nums[i] > 0:
                seen.add(nums[i])

        if len(seen) == 0:
            return max(nums)
        else:
            return sum(seen)