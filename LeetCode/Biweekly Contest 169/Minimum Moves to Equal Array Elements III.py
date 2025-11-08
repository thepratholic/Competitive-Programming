from typing import List


class Solution:
    def minMoves(self, nums: List[int]) -> int:
        n = len(nums)

        maxi = max(nums)

        ops = 0
        for i in range(n):
            if nums[i] == maxi: continue
            else:
                ops += abs(nums[i] - maxi)

        return ops