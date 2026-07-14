from typing import List


class Solution:
    def maxConsistentColumns(self, grid: List[List[int]], limit: int) -> int:
        m = len(grid)
        n = len(grid[0])

        dp = [1] * n

        for j in range(n):
            for i in range(j):
                ok = True

                for r in range(m):
                    if abs(grid[r][j] - grid[r][i]) > limit:
                        ok = False
                        break

                if ok:
                    dp[j] = max(dp[i] + 1, dp[j])

        return max(dp)