from typing import List


class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        ans = float('-inf')

        for i in range(1, m - 1):
            for j in range(1, n - 1):
                ans = max(ans, grid[i][j])

        for i in range(m):
            mx = float('-inf')
            sum = grid[i][0]

            for j in range(1, n):
                mx = max(mx, sum + grid[i][j])
                sum = max(grid[i][j], sum + grid[i][j])

            ans = max(ans, mx)

        for j in range(n):
            mx = float('-inf')
            sum = grid[0][j]

            for i in range(1, m):
                mx = max(mx, sum + grid[i][j])
                sum = max(grid[i][j], sum + grid[i][j])

            ans = max(ans, mx)

        return ans