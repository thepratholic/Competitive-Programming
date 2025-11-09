from functools import lru_cache
from typing import List


class Solution:
    def maxPathScore(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        
        @lru_cache(None)
        def f(i, j, cost):
            if i >= m or j >= n:
                return -1

            new_cost = cost + (0 if grid[i][j] == 0 else 1)
            if new_cost > k:
                return -1

            if i == m - 1 and j == n - 1:
                return grid[i][j]

            right = f(i, j + 1, new_cost)
            down = f(i + 1, j, new_cost)

            best = max(right, down)
            if best == -1:
                return -1
            return grid[i][j] + best

        return f(0, 0, 0)