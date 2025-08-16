from typing import List


class Solution:
    def perfectPairs(self, nums: List[int]) -> int:
        nums = [abs(x) for x in nums]
        nums.sort()
        n = len(nums)
        ans = 0
        j = 0
        for i in range(n - 1):
            a = nums[i]

            while j < n and nums[j] <= 2 * a:
                j += 1

            ans += (j - i - 1)

        return ans