from typing import List


class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            digit = nums[i]

            ans = 0
            while digit > 0:
                ld = digit % 10
                ans += (ld)
                digit //= 10

            if ans == i:
                return i


        return -1