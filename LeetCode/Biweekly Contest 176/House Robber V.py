from functools import lru_cache
from typing import List


class Solution:
    def rob(self, nums: List[int], color: List[int]) -> int:
        n = len(nums)

        @lru_cache(None)
        def f(i):
            if i == n:
                return 0

            take = 0
            if i + 1 < n and color[i] == color[i + 1]:
                take = nums[i] + f(i + 2)

            else:
                take = nums[i] + f(i + 1)

            not_take = f(i + 1)

            return max(take, not_take)

        return f(0)