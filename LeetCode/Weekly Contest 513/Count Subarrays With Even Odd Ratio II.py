from bisect import bisect_right
from sortedcontainers import SortedList


class Solution:
    def countRatioSubarrays(self, nums: list[int], a: int, b: int) -> int:
        sl = SortedList([0])
        ans = 0
        pref = 0

        for x in nums:
            if x & 1:
                pref += a

            else:
                pref -= b

            ans += bisect_right(sl, pref)
            sl.add(pref)

        return ans