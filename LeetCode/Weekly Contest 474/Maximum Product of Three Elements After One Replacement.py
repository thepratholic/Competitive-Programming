from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        negs = 0
        n = len(nums)

        extra = (10 ** 5)


        nums = [abs(x) for x in nums]
        nums.sort()

        return nums[-1] * nums[-2] * extra