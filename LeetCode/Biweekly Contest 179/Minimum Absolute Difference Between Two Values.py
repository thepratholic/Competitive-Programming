class Solution:
    def minAbsoluteDifference(self, nums: list[int]) -> int:
        n = len(nums)

        mn = float('inf')

        for i in range(n):
            if nums[i] == 1:
                for j in range(n):
                    if nums[j] == 2:
                        mn = min(mn, abs(i - j))

        return mn if mn != float('inf') else -1