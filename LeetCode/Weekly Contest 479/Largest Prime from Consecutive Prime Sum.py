class Solution:
    def largestPrime(self, n: int) -> int:
        def sieve(n=10**5):
            prime = [True] * (n + 1)
            prime[0] = prime[1] = False
        
            i = 2
            while i * i <= n:
                if prime[i]:
                    j = i * i
                    while j <= n:
                        prime[j] = False
                        j += i
                i += 1
        
            return prime
        
        primes = sieve(n)

        prime_nos = [i for i in range(2, n + 1) if primes[i]]

        sum = 0
        ans = 0

        for p in prime_nos:
            sum += p

            if sum > n: break

            if primes[sum]:
                ans = sum

        return ans