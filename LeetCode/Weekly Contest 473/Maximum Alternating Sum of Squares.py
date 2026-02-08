from collections import deque
from typing import List


class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(n): nums[i] = abs(nums[i])
            
        q = deque(sorted(nums))

        ans = 0
        pos = True
        while q:
            if pos:
                val = q.pop()
                ans += (val * val)

            else:
                val = q.popleft()
                ans -= (val * val)

            pos = not pos

        return ans