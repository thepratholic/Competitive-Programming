from typing import List


class Solution:
    def countStableSubarrays(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        n = len(nums)
        q = len(queries)
        ans = [-1] * q

        next_break = [-1] * n
        next_break[-1] = n
        count = [0] * n

        for i in range(n - 2, -1, -1):
            if nums[i] <= nums[i + 1]:
                next_break[i] = next_break[i + 1]

            else:
                next_break[i] = i + 1

        
        p = 2
        count[0] = 1 # coz pehla element ek hi length ka subarray create krega

        for i in range(1, n):
            if next_break[i] == next_break[i - 1]:
                count[i] = count[i - 1] + p

            else:
                p = 1
                count[i] = count[i - 1] + p

            p += 1

        for i, (l, r) in enumerate(queries):

            cut = min(next_break[l], r + 1)

            if cut > 0:
                ans[i] = count[r] - count[cut - 1]

            left = cut - l

            ans[i] += (left * (left + 1) // 2)

        return ans