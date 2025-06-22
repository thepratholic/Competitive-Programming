from typing import Counter, List


class Solution:
    def isPrime(self, n):
        if n == 1:
            return False
        count = 0
        for i in range(1, n+1):
            if n % i == 0:
                count += 1
        if count == 2: return True
        return False
        
    def checkPrimeFrequency(self, nums: List[int]) -> bool:
        freq = Counter(nums)

        for k, v in freq.items():
            if self.isPrime(v):
                return True

        return False