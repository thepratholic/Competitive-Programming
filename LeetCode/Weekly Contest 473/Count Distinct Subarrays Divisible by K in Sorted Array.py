from itertools import groupby
from typing import Counter, List

class Solution:
    def numGoodSubarrays(self, nums: List[int], k: int) -> int:
        count = Counter()
        count[0] = 1
        pref, res = 0, 0

        for x in nums:
            pref = (pref + x) % k
            res += count[pref]
            count[pref] += 1

        for val, it in groupby(nums):
            l = len(list(it))

            for length in range(1, l):
                if (val * length) % k == 0:
                    res -= (l - length)

        return res