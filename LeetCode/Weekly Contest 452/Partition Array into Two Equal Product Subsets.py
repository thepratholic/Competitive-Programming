from math import prod
from typing import List

class Solution:
    def checkEqualPartitions(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        total_subsets = 1 << n

        for mask in range(1, total_subsets - 1): 
            subset1 = []
            subset2 = []

            for i in range(n):
                if (mask >> i) & 1:
                    subset1.append(nums[i])
                else:
                    subset2.append(nums[i])

            if prod(subset1) == target and prod(subset2) == target:
                return True

        return False