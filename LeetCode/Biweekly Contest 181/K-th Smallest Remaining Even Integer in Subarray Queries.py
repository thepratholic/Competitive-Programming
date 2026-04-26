from bisect import *

class Solution:
    def kthRemainingInteger(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        n = len(nums)

        even_vals = []
        even_idx = []

        for i, x in enumerate(nums):
            if x & 1: continue
            else:
                even_vals.append(x)
                even_idx.append(i)

        res = []

        for l, r, k in queries:

            left = bisect_left(even_idx, l)
            right = bisect_right(even_idx, r)

            removed_total = right - left # itne humko remove karne hai range mein

            low, high = 2, 2 * (k + removed_total)
            ans = high

            while low <= high:
                mid = (low + high) >> 1

                if mid & 1:
                    mid -= 1

                # if mid < 2:
                #     mid = 2

                total_evens = mid // 2

                removed_till_mid = bisect_right(even_vals, mid, left, right) - left

                remaining_evens = total_evens - removed_till_mid

                if remaining_evens >= k:
                    ans = mid
                    high = mid - 2

                else:
                    low = mid + 2

            res.append(ans)

        return res