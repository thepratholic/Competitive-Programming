from collections import deque

class Solution:
    def colorGrid(self, n, m, sources):
        sources.sort(key=lambda v: -v[2])
        
        grid = [[0] * m for _ in range(n)]
        q = deque()
        
        for i, j, color in sources:
            grid[i][j] = color
            q.append((i, j))
        
        directions = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        
        while q:
            i, j = q.popleft()
            
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if ni < 0 or ni >= n or nj < 0 or nj >= m:
                    continue
                if grid[ni][nj] != 0:
                    continue
                
                grid[ni][nj] = grid[i][j]
                q.append((ni, nj))
        
        return grid