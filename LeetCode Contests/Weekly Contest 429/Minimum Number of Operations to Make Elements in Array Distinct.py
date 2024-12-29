from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        if len(nums) == len(set(nums)):
            return 0


        operations = 0
        while nums:
            nums = nums[3:]
            operations += 1

            if len(nums) == len(set(nums)):
                return operations

        return operations