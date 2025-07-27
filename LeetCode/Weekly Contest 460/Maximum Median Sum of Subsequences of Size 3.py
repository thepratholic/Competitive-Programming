from typing import List


class Solution:
    def maximumMedianSum(self, nums: List[int]) -> int:
        n = len(nums)

        nums.sort()

        ans = 0
        for i in range(n // 3, n, 2):
            ans += nums[i]

        return ans