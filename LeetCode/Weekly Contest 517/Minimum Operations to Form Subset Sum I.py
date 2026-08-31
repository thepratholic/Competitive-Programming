from functools import lru_cache


class Solution:
    def minOperations(self, nums: list[int], sum: int) -> int:
        n = len(nums)
        INF = float('inf')

        def options(x):
            res = [(0, 0)]

            v, c = x, 0

            while v <= sum:
                res.append((v, c))
                v *= 2
                c += 1

            v, c = x, 0
            while v:
                v //= 2
                c += 1
                res.append((v, c))
    
            return res

        choices = [options(x) for x in nums]

        @lru_cache(None)
        def f(idx, rem):
            if rem == 0:
                return 0

            if idx == n:
                return INF

            ans = f(idx + 1, rem)

            for val, cost in choices[idx]:
                if val <= rem:
                    ans = min(ans, cost + f(idx + 1, rem - val))

            return ans

        ans = f(0, sum)

        return ans if ans != INF else -1