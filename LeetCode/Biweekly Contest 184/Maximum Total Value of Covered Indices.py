from typing import List


class Solution:
    def maxTotal(self, nums: List[int], s: str) -> int:
        n = len(s)
        dp = [[-1] * 2 for _ in range(n)]

        def solve(i, taken):
            if i >= n:
                return 0

            if dp[i][taken] != -1:
                return dp[i][taken]

            ans = solve(i + 1, 0)

            if s[i] == '1' and not taken:
                ans = max(ans, nums[i] + solve(i + 1, 0))

            if i + 1 < n and s[i + 1] == '1':
                ans = max(ans, nums[i] + solve(i + 1, 1))

            dp[i][taken] = ans
            return ans

        return solve(0, 0)