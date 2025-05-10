from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        stack = [0]

        for i in nums:
            while stack[-1] > i:
                stack.pop()
                ans += 1

            if stack[-1] < i:
                stack.append(i)

        ans += len(stack) - 1

        return ans