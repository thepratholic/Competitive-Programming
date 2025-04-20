class Solution:
    def maximumPossibleSize(self, nums: List[int]) -> int:
        stack = []

        for num in nums:
            while stack and stack[-1] > num:
                num = max(num, stack.pop())
            stack.append(num)

        return len(stack)