import math
from typing import List


class Solution:
    def isPrime(self, n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.sqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True

        
    def splitArray(self, nums: List[int]) -> int:
        a, b = [], []
        n = len(nums)
        for i in range(n):
            if self.isPrime(i):
                a.append(nums[i])
            else:
                b.append(nums[i])

        return abs(sum(a) - sum(b))