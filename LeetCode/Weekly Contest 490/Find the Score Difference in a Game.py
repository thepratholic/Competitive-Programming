from typing import List


class Solution:
    def scoreDifference(self, nums: List[int]) -> int:
        n = len(nums)

        first, second = 0, 0

        active_first = True

        for i in range(n):
            if (i + 1) % 6 == 0:
                active_first = not active_first

            if nums[i] & 1:
                active_first = not active_first


            if active_first:
                first += nums[i]

            else:
                second += nums[i]

        return first - second