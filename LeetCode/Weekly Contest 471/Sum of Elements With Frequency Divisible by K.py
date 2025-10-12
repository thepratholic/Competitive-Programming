from typing import Counter, List


class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:
        freq = Counter(nums)

        ans = 0

        for key, val in freq.items():
            if val % k == 0:
                ans += (key * val)

        return ans