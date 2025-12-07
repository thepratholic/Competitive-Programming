class Solution:
    def largestPrime(self, n: int) -> int:

        def sieve_fast(limit):
            if limit < 2:
                return bytearray(b'\x00') * (limit + 1)
            is_prime = bytearray(b'\x01') * (limit + 1)
            is_prime[0] = is_prime[1] = 0
            import math
            r = int(math.isqrt(limit))
            for i in range(2, r + 1):
                if is_prime[i]:
                    start = i * i
                    is_prime[start:limit+1:i] = b'\x00' * (((limit - start) // i) + 1)
            return is_prime

        if n < 2:
            return 0

        LIMIT = n 
        primes = sieve_fast(LIMIT)

        ans = 0

        pref = 0
        for i in range(2, LIMIT + 1):
            if primes[i]:
                pref += i
            if pref > n:
                break
            if pref >= 2 and primes[pref]:
                ans = pref

        return ans
