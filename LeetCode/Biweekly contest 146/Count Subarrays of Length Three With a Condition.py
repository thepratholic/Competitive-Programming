from typing import List

class Solution:
    def countSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        count = 0
        if n < 3: return 0
        l, r = 0, 2


        while r < n:
            if (nums[r] + nums[l]) == nums[r-1] / 2:
                count += 1

            r += 1
            l += 1

        return count