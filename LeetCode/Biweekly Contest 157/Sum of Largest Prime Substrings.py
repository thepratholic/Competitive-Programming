class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True
        
    def sumOfLargestPrimes(self, s: str) -> int:
        primes = []

        for i in range(len(s)):
            for j in range(i + 1, len(s) + 1):
                num = int(s[i:j])
                if self.isPrime(num):
                    primes.append(num)

        primes = list(set(primes)) 
        primes.sort(reverse=True)

        return sum(primes[:3])