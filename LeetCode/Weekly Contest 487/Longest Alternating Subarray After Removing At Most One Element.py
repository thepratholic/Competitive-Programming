from typing import List


class Solution:
    def longestAlternating(self, nums: List[int]) -> int:
        n = len(nums)
        
        left = [[1, 1] for _ in range(n)]
        right = [[1, 1] for _ in range(n)]
        ans = 1
        # without deletion wala case compute karo
        for i in range(1, n):
            if nums[i - 1] < nums[i]:
                left[i][0] = left[i - 1][1] + 1

            elif nums[i - 1] > nums[i]:
                left[i][1] = left[i - 1][0] + 1

            ans = max(ans, left[i][0], left[i][1])

        # ab right side se compute karo
        for i in range(n - 2, -1, -1):
            if nums[i] > nums[i + 1]:
                right[i][0] = right[i + 1][1] + 1

            elif nums[i] < nums[i + 1]:
                right[i][1] = right[i + 1][0] + 1

        for i in range(1, n - 1):
            if nums[i - 1] < nums[i + 1]:
                ans = max(ans, left[i - 1][1] + right[i + 1][0])

            elif nums[i - 1] > nums[i + 1]:
                ans = max(ans, left[i - 1][0] + right[i + 1][1])

        return ans