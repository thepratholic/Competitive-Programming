from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        n = len(nums)

        rem = {0: [], 1: [], 2: []}

        for x in nums:
            rem[x % 3].append(x)

        for r in rem:
            rem[r].sort(reverse=True)

        ans = 0

        if len(rem[0]) >= 3:
            ans = max(ans, sum(rem[0][:3]))

        if len(rem[1]) >= 3:
            ans = max(ans, sum(rem[1][:3]))

        if len(rem[2]) >= 3:
            ans = max(ans, sum(rem[2][:3]))

        if rem[0] and rem[1] and rem[2]:
            ans = max(ans, rem[0][0] + rem[1][0] + rem[2][0])

        return ans