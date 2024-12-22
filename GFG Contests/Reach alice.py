class Solution:
    def numWays(self, s : str) -> int:
        n = len(s)
        MOD = 10**9 + 7

        dp = [0] * n
        dp[0] = 1

        for i in range(n):
            if dp[i] == 0:
                continue

            if i + 1 < n:
                dp[i + 1] = (dp[i + 1] + dp[i]) % MOD

            if i + 2 < n and s[i] == '0':
                dp[i + 2] = (dp[i + 2] + dp[i]) % MOD

        return dp[n - 1]