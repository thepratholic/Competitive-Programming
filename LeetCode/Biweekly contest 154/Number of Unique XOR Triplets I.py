import math
from typing import List


class Solution:
    def uniqueXorTriplets(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return n
        L = math.floor(math.log2(n)) + 1
        return 1 << L  