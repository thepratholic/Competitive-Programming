from collections import defaultdict
from typing import List


class Solution:
    def alternatingXOR(self, nums: List[int], target1: int, target2: int) -> int:
        n = len(nums)
        MOD = (10 ** 9) + 7

        mp1 = defaultdict(int)
        mp2 = defaultdict(int)
        mp2[0] += 1
        xr = 0
        ans = 0

        for i in range(n):
            xr ^= nums[i]

            end_t1 = mp2[xr ^ target1]
            end_t2 = mp1[xr ^ target2]

            mp1[xr] = (mp1[xr] + end_t1) % MOD
            mp2[xr] = (mp2[xr] + end_t2) % MOD

            if i == n - 1:
                ans = (end_t1 + end_t2) % MOD

        return ans