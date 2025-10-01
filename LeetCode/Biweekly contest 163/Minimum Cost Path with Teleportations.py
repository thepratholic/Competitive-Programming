from typing import List

class Solution:
    def minCost(self, grid: List[List[int]], k: int) -> int:
        m, n = len(grid), len(grid[0])
        INF = 10**18 

        dp = [[INF] * n for _ in range(m)]
        dp[0][0] = 0
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0: 
                    continue
                if i > 0:
                    dp[i][j] = min(dp[i][j], dp[i-1][j] + grid[i][j])
                if j > 0:
                    dp[i][j] = min(dp[i][j], dp[i][j-1] + grid[i][j])

        MAX = 10000 
        
        for _ in range(k):
            best = [INF] * (MAX+2)

            for i in range(m):
                for j in range(n):
                    val = grid[i][j]
                    best[val] = min(best[val], dp[i][j])

            for v in range(MAX-1, -1, -1):
                best[v] = min(best[v], best[v+1])

            ndp = [[INF] * n for _ in range(m)]
            ndp[0][0] = 0
            for i in range(m):
                for j in range(n):
                    if i == 0 and j == 0:
                        continue

                    val = grid[i][j]

                    ndp[i][j] = min(ndp[i][j], best[val])

                    if i > 0:
                        ndp[i][j] = min(ndp[i][j], ndp[i-1][j] + val)
                    if j > 0:
                        ndp[i][j] = min(ndp[i][j], ndp[i][j-1] + val)

            dp = ndp 

        return dp[m-1][n-1]
