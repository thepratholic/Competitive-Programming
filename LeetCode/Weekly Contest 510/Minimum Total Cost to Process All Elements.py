from math import ceil


class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        available = k
        how_many = 0
        MOD = (10 ** 9) + 7

        for x in nums:
            if available > x:
                available -= x

            else:
                extra = x - available
                mn_ops = ceil(extra / k)
                available += mn_ops * k
                available -= x

                how_many += mn_ops

        ans = how_many * (how_many + 1) // 2
        return ans % MOD