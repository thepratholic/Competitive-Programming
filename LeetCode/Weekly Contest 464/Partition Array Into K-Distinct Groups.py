from collections import Counter
from typing import List


class Solution:
    def partitionArray(self, nums: List[int], k: int) -> bool:
        f = Counter(nums)

        if len(nums) % k != 0:
            return False

        g = len(nums) // k
        for freq in f.values():
            if freq > g:
                return False

        return True