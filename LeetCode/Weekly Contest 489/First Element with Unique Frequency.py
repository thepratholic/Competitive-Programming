from collections import Counter
from typing import List


class Solution:
    def firstUniqueFreq(self, nums: List[int]) -> int:
        n = len(nums)

        freq = Counter(nums)

        mpp = Counter(freq.values())

        for x in nums:
            if mpp[freq[x]] == 1:
                return x

        return -1

        