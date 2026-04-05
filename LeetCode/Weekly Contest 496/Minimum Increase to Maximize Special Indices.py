from functools import lru_cache


class Solution:
    def minIncrease(self, nums) -> int:
        n = len(nums)

        if n & 1:
            ans = 0
            for i in range(1, n - 1, 2):
                ans += max(0, max(nums[i - 1], nums[i + 1]) + 1 - nums[i])

            return ans

        @lru_cache(None)
        def f(idx, skip):
            if idx >= n - 1:
                return 0

            cost = max(0, max(nums[idx - 1], nums[idx + 1]) + 1 - nums[idx])

            if skip:
                return cost + f(idx + 2, True)

            else:
                return cost + min(f(idx + 2, False), f(idx + 3, True))

        return min(f(1, False), f(2, True))