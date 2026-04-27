class Solution:
    def minOperations(self, nums: list[int]) -> int:
        ans = 0

        n = len(nums)

        for i in range(n - 1):
            if nums[i] > nums[i + 1]:
                ans += nums[i] - nums[i + 1]

        return ans