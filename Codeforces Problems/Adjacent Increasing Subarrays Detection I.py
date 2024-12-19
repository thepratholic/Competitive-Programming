from typing import List


class Solution:
    def f(self, nums, start, k):
        for i in range(start, start + k - 1):
            if nums[i] >= nums[i + 1]: return False
        return True

    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        n = len(nums)

        for i in range(n - 2 * k + 1):
            if self.f(nums, i, k) and self.f(nums, i + k, k):
                return True
        return False