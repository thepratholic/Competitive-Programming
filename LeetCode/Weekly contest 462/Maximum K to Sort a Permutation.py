from typing import List


class Solution:
    def sortPermutation(self, nums: List[int]) -> int:
        if nums == sorted(nums):
            return 0

        val = ~0

        n = len(nums)

        for i in range(n):
            if nums[i] != i:
                val &= nums[i]

        return val