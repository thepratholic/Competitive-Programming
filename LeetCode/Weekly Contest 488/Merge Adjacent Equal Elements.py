from typing import List


class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        n = len(nums)

        if len(set(nums)) == n:
            return nums

        stack = []
        for x in nums:
            stack.append(x)

            while len(stack) >= 2 and stack[-1] == stack[-2]:
                val = stack.pop()
                stack.pop()
                stack.append(val * 2)

        return stack