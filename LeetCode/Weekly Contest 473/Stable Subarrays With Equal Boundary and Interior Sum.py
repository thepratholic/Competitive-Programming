from collections import defaultdict
from typing import List


class Solution:
    def countStableSubarrays(self, a: List[int]) -> int:
        n = len(a)
        res = 0
        pref = 0
        mpp = defaultdict(lambda : defaultdict(int))

        for i in range(n):
            res += mpp[a[i]].get(pref - a[i], 0)
            pref += a[i]
            mpp[a[i]][pref] += 1

            if i > 0 and a[i] == 0 and a[i - 1] == 0:
                res -= 1

        return res