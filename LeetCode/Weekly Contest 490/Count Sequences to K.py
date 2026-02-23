from fractions import Fraction
from functools import lru_cache
from typing import List

class Solution:
    def countSequences(self, nums: List[int], k: int) -> int:
        n = len(nums)

        k = Fraction(k, 1) # in built Fraction hai, mene google kia toh mil gaya

        @lru_cache(None)
        def f(i, val):
            if i == n:
                return 1 if val == k else 0

            res = 0
            res += f(i + 1, val)
            res += f(i + 1, val * nums[i])
            res += f(i + 1, val / nums[i])

            return res

        return f(0, Fraction(1, 1))