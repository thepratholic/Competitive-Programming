from functools import lru_cache
import sys


sys.setrecursionlimit(300000)

class Solution:
    def minCost(self, s: str, encCost: int, flatCost: int) -> int:
        n = len(s)

        pref = [0] * n
        pref[0] = 1 if s[0] == '1' else 0

        for i in range(1, n):
            pref[i] = pref[i - 1] + (1 if s[i] == '1' else 0)

        def get(l, r):
            return pref[r] - (pref[l - 1] if l > 0 else 0)

        @lru_cache(None)
        def f(l, r):
            sz = r - l + 1
            x = get(l, r)

            if x == 0:
                cost = flatCost

            else:
                cost = sz * x * encCost

            if sz & 1:
                return cost

            mid = (l + r) >> 1
            ans = f(l, mid) + f(mid + 1, r)

            return min(ans, cost)

        res = f(0, n - 1)
        f.cache_clear()
        return res