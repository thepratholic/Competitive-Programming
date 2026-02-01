from bisect import bisect_left
from typing import List


class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        ans = 0
        n = len(nums)

        for bit in range(31):
            lis = []

            for x in nums:
                if (x >> bit) & 1:
                    pos = bisect_left(lis, x)
                    if pos == len(lis):
                        lis.append(x)

                    else:
                        lis[pos] = x

            ans = max(ans, len(lis))

        return ans