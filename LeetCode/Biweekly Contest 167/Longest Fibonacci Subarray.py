from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        n = len(nums)

        ans = 2
        cur = 0
        for i in range(2, n):
            # cur = 0
            if nums[i - 2] + nums[i - 1] == nums[i]:
                if cur == 0:
                    cur += 3
                else:
                    cur += 1

            else:
                cur = 0

            ans = max(ans, cur)

        return ans