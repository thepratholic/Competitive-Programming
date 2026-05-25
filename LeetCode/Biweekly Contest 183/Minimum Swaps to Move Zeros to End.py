class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        n = len(nums)

        l, r = 0, n - 1
        ans = 0

        while l < r:

            while l < r and nums[l] != 0:
                l += 1

            while l < r and nums[r] == 0:
                r -= 1

            if l < r:
                ans += 1
                l += 1
                r -= 1

        return ans

