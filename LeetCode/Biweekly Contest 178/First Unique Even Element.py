from typing import DefaultDict


class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        n = len(nums)

        mpp = DefaultDict(int)

        for i, v in enumerate(nums):
            if v % 2 == 0:
                mpp[v] += 1


        for x in nums:
            if mpp[x] == 1:
                return x

        return -1