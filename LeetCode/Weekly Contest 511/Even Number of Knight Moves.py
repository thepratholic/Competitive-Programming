from collections import deque

class Solution:
    def canReach(self, start: list[int], target: list[int]) -> bool:
        dirs = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

        vis = set()

        q = deque()

        sx, sy = start
        tx, ty = target

        q.append((sx, sy, 0))
        vis.add((sx, sy))

        while q:
            x, y, m = q.popleft()

            if (x, y) == (tx, ty):
                return m & 1 == 0

            for dx, dy in dirs:
                nRow, nCol = dx + x, dy + y

                if nRow >= 0 and nRow < 8 and nCol >= 0 and nCol < 8 and (nRow, nCol) not in vis:
                    vis.add((nRow, nCol))
                    q.append((nRow, nCol, m + 1))

        return False
                    