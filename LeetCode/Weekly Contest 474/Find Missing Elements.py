from typing import List


class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        small = min(nums)
        large = max(nums)
        n = len(nums)

        ans = []
        for i in range(small + 1, large):
            if i not in nums:
                ans.append(i)


        return ans