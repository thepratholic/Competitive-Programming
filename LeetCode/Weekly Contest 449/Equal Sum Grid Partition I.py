from typing import List


class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        n = len(grid)
        m = len(grid[0])

        row = [0] * n
        col = [0] * m
        sum = 0

        for i in range(n):
            for j in range(m):
                sum += grid[i][j]

            row[i] = sum

        sum = 0
        for j in range(m):
            for i in range(n):
                sum += grid[i][j]
            col[j] = sum

        for i in range(n):
            s = row[i]
            rs = sum - s

            if s == rs: return True

        for j in range(m):
            s = col[j]
            cs = sum - s
            if s == cs:
                return True

        return False