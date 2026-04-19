class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        n = len(nums)

        ans = -1

        for i in range(n):
            mx = float('-inf')
            mn = float('inf')

            for j in range(0, i + 1):
                mx = max(mx, nums[j])

            for j in range(i, n):
                mn = min(mn, nums[j])

            if mx - mn <= k:
                return i

        return -1