from bisect import bisect_left


class Solution:
    def minOperations(self, nums: list[int]) -> int:
        n = len(nums)

        mx = 200000

        sieve = [True] * (mx + 1)

        sieve[0] = sieve[1] = False
        for i in range(2, int(mx ** 0.5) + 1):
            if sieve[i]:
                for j in range(i * i, mx + 1, i):
                    sieve[j] = False

        primes = [i for i in range(2, mx + 1) if sieve[i]]

        def make(x):
            if sieve[x]:
                return 0

            idx = bisect_left(primes, x)
            return primes[idx] - x

        def not_make(x):
            if not sieve[x]:
                return 0

            y = x
            while sieve[y]:
                y += 1

            return y - x

        ans = 0
        for i, x in enumerate(nums):
            if i & 1:
                ans += not_make(x)

            else:
                ans += make(x)

        return ans