from typing import List


class Solution:
    def longestBalanced(self, nums: List[int]) -> int:
        n = len(nums)

        maxi = 0

        for i in range(n):
            even, odd = set(), set()

            for j in range(i, n):

                if nums[j] & 1:
                    odd.add(nums[j])
                else:
                    even.add(nums[j])


                if len(odd) == len(even):
                    maxi = max(maxi, j - i + 1)


        return maxi