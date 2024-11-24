from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
         n = len(nums)
         min_sum = float('inf')  # Initialize to infinity for comparison

         for start in range(n):
            current_sum = 0

            for end in range(start, min(start + r, n)):
                current_sum += nums[end]

                if l <= (end - start + 1) <= r and current_sum > 0:
                    min_sum = min(min_sum, current_sum)


         return min_sum if min_sum != float('inf') else -1