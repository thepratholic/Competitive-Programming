from functools import lru_cache


class Solution:
    def minCost(self, n: int) -> int:

        @lru_cache(None)
        def f(x):
            if x == 1:
                return 0

            ans = float('inf')
            for a in range(1, x):
                b = x - a
                cost = a * b + f(a) + f(b)
                ans = min(ans, cost)

            return ans

        return f(n)