from typing import List


class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2:
            return 0

        increasing_lengths = [1] * n
        for i in range(1, n):
            if nums[i] > nums[i - 1]:
                increasing_lengths[i] = increasing_lengths[i - 1] + 1

        left, right = 1, n // 2
        result = 0

        while left <= right:
            mid = (left + right) // 2
            found = False
            for i in range(n - 2 * mid + 1):
                if increasing_lengths[i + mid - 1] >= mid and increasing_lengths[i + 2 * mid - 1] >= mid:
                    found = True
                    break

            if found:
                result = mid
                left = mid + 1
            else:
                right = mid - 1

        return result