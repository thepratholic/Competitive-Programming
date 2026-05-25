from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        ans = float('inf')

        if n == 1:
            return 0

        idx = nums.index(0)

        asc = True
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] + 1) % n:
                asc = False
                break

        des = True
        for i in range(n):
            if nums[(i + 1) % n] != (nums[i] - 1) % n:
                des = False
                break

        if asc:
            ans = min(ans, idx)
            ans = min(ans, 2 + (n - idx) % n)

        if des:
            ans = min(ans, n - idx)
            ans = min(ans, (idx + 1) % n + 1)

        return ans if ans != float('inf') else -1