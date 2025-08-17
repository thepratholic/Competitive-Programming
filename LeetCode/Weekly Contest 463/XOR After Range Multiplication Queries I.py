from typing import List


class Solution:
    def xorAfterQueries(self, nums: List[int], queries: List[List[int]]) -> int:
        mod = 10**9 + 7


        for l, r, k, v in queries:

            while l <= r:

                nums[l] = (nums[l] * v) % mod
                l += k


        xr = 0

        for i in nums:
            xr ^= i

        return xr