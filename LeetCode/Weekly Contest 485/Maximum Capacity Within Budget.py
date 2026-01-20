from bisect import bisect_right
from typing import List


class Solution:
    def maxCapacity(self, costs: List[int], capacity: List[int], budget: int) -> int:
        n = len(costs)

        arr = sorted(zip(costs, capacity))

        sc = [x[0] for x in arr]
        cp = [x[1] for x in arr]

        pref = [0] * n
        pref[0] = cp[0]

        for i in range(1, n):
            pref[i] = max(pref[i - 1], cp[i])

        ans = 0
        idx = bisect_right(sc, budget - 1) - 1
        if idx >= 0:
            ans = max(ans, pref[idx])

        for i in range(n):
            rem = (budget - 1) - sc[i]
            if rem <= 0: continue

            j = bisect_right(sc, rem, 0, i) - 1
            if j >= 0:
                ans = max(ans, cp[i] + pref[j])
        return ans