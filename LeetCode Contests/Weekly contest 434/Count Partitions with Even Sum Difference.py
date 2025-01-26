from typing import List


class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        count = 0
        n = len(nums)
        total = sum(nums)
        left_sum = 0
        for i in range(n - 1):

            left_sum += nums[i]
            right_sum = total - left_sum

            if (left_sum - right_sum) % 2 == 0:
                count += 1

        return count