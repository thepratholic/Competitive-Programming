from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        first_val = nums[0]
        sum = 0
        maxi = 0
        n = len(nums)

        for i in range(1, n):
            maxi = max(maxi, abs(nums[i] - nums[i-1]))

        maxi = max(maxi, abs(nums[n-1] - nums[0]))
        return maxi