class Solution:
    def sumOfPrimesInRange(self, n: int) -> int:
        r = int(str(n)[::-1])

        l = min(n, r)
        h = max(n, r)

        sieve = [True] * (h + 1)

        if h >= 0:
            sieve[0] = False

        if h >= 1:
            sieve[1] = False

        i = 2
        while i * i <= h:
            if sieve[i]:
                j = i * i

                while j <= h:
                    sieve[j] = False
                    j += i

            i += 1

        ans = 0
        for i in range(l, h + 1):
            if sieve[i]:
                ans += i

        return ans