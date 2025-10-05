from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)

        xor = 0

        for i in range(n):
            xor ^= nums[i]

        if xor != 0:
            return n

        else:
            if all(x == 0 for x in nums):
                return 0

            return n - 1