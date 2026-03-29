from functools import lru_cache


class Solution:
    def minCost(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        @lru_cache(None)
        def f(i, j):
            if i >= m or j >= n:
                return set()

            if i == m - 1 and j == n - 1:
                return {grid[i][j]}

            cur = grid[i][j]
            res = set()

            right = f(i, j + 1)
            down = f(i + 1, j)

            for val in right:
                res.add(val ^ cur)

            for val in down:
                res.add(val ^ cur)

            return res

        return min(f(0, 0))