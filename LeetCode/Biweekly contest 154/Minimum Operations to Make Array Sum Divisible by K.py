from typing import List


class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ops = 0

        if sum(nums) % k == 0:
            return ops

        i = 0
        while sum(nums) % k != 0:
            nums[i % n] = nums[i % n] - 1
            ops += 1
            i += 1

        return ops