class Solution:
    def minDeletions(self, nums: list[int]) -> int:
        ans = 0
        n = len(nums)

        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                ans += 1

        return ans