from collections import defaultdict
from typing import List


class Solution:
    def minOperations(self, nums: List[int], target: List[int]) -> int:
        n = len(nums)

        nums_to_target = defaultdict(int)

        for i in range(n):
            if nums[i] != target[i]:
                nums_to_target[nums[i]] = target[i]


        return len(nums_to_target)