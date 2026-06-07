from collections import deque
from typing import List


class Solution:
    def maximumSum(self, nums: List[int], m: int, l: int, r: int) -> int:
        n = len(nums)

        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]

        neg = -10 ** 18

        dp = [[neg] * (n + 1) for _ in range(m + 1)]

        for i in range(n + 1):
            dp[0][i] = 0

        ans = neg

        for t in range(1, m + 1):
            dq = deque()

            for i in range(n, -1, -1):
                add = i + l

                if add <= n:
                    val = pref[add] + dp[t - 1][add]

                    while dq and dq[-1][1] <= val:
                        dq.pop()

                    dq.append((add, val))

                while dq and dq[0][0] > i + r:
                    dq.popleft()

                take = neg

                if dq:
                    take = dq[0][1] - pref[i]

                skip = neg
                if i < n:
                    skip = dp[t][i + 1]

                dp[t][i] = max(skip, take)

            ans = max(ans, dp[t][0])
        return ans