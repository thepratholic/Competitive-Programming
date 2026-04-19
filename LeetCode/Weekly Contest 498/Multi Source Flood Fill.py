from collections import deque


class Solution:
    def colorGrid(self, n: int, m: int, sources: list[list[int]]) -> list[list[int]]:
        grid = [[0] * m for _ in range(n)]
        time = [[float('inf')] * m for _ in range(n)]

        q = deque()

        for r, c, color in sources:
            q.append((r, c))
            grid[r][c] = color
            time[r][c] = 0

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isValid(i, j):
            return i >= 0 and i < n and j >= 0 and j < m

        while q:
            r, c = q.popleft()

            for dx, dy in dirs:
                nrow, ncol = dx + r, c + dy

                if isValid(nrow, ncol):

                    if time[nrow][ncol] == float('inf'):
                        time[nrow][ncol] = time[r][c] + 1
                        q.append((nrow, ncol))

                        grid[nrow][ncol] = grid[r][c]

                    elif time[nrow][ncol] == time[r][c] + 1:
                        grid[nrow][ncol] = max(grid[nrow][ncol], grid[r][c])

        return grid