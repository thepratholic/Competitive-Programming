from typing import List


class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])

        res = 0
        for j in range(m):
            for i in range(n-1):
                if grid[i][j] >= grid[i+1][j]:
                    diff = grid[i][j] - grid[i+1][j] + 1

                    res += diff
                    grid[i+1][j] += diff
        return res
            