from typing import Counter


class Solution:
    def isMiddleElementUnique(self, nums: list[int]) -> bool:
        c = Counter(nums)

        mid = len(nums) // 2

        return c[nums[mid]] == 1