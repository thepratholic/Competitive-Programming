from typing import List


class Solution:
    def lastVisitedCell(self, grid: List[List[str]]) -> List[int]:
        m = len(grid)
        n = len(grid[0])

        vis = [[False] * n for _ in range(m)]

        r, c = 0, 0
        vis[r][c] = True

        while True:
            nr, nc = r, c

            if grid[r][c] == 'L':
                nc -= 1
            elif grid[r][c] == 'R':
                nc += 1
            elif grid[r][c] == 'U':
                nr -= 1
            elif grid[r][c] == 'D':
                nr += 1

            if nr < 0 or nr >= m or nc < 0 or nc >= n:
                break

            if vis[nr][nc]:
                break

            r, c = nr, nc
            vis[r][c] = True

        return [r, c]