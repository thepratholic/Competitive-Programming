from typing import List
from collections import deque

class Solution:
    def isValid(self, i, j, n, m):
        return 0 <= i < n and 0 <= j < m

    def bfs(self, row, col, vis, grid, k):
        if grid[row][col] == 0:
            return 0

        n, m = len(grid), len(grid[0])
        vis[row][col] = True
        q = deque()
        q.append((row, col))
        island_sum = grid[row][col]
        
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        while q:
            x, y = q.popleft()

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if self.isValid(nx, ny, n, m) and not vis[nx][ny] and grid[nx][ny] > 0:
                    vis[nx][ny] = True
                    island_sum += grid[nx][ny]
                    q.append((nx, ny))

        return 1 if island_sum % k == 0 else 0

    def countIslands(self, grid: List[List[int]], k: int) -> int:
        n, m = len(grid), len(grid[0])
        vis = [[False] * m for _ in range(n)]
        ans = 0

        for i in range(n):
            for j in range(m):
                if not vis[i][j] and grid[i][j] > 0:
                    ans += self.bfs(i, j, vis, grid, k)

        return ans
