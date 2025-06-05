import heapq
from typing import List

class Solution:

    def isValid(self, i, j, m, n):
        if i < 0 or i >= m: return False
        if j < 0 or j >= n: return False
        return True

    def minMoves(self, classroom: List[str], energy: int) -> int:
        m, n = len(classroom), len(classroom[0])
        litterMap = {}
        startRow, startCol = -1, -1
        litterIndex = 0

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    startRow, startCol = i, j

                elif classroom[i][j] == 'L':
                    litterMap[(i, j)] = litterIndex
                    litterIndex += 1

        if len(litterMap) == 0:
            return 0

        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # directions
        heap = []

        heapq.heappush(heap, (0, startRow, startCol, energy, 0))

        vis = {}

        while heap:
            moves, r, c, energy_left, mask = heapq.heappop(heap)

            if mask == (1 << len(litterMap)) - 1:
                return moves

            state_key = (r, c, mask)

            if state_key in vis and vis[state_key] >= energy_left:
                continue

            vis[state_key] = energy_left

            for dx, dy in directions:
                nr, nc = r + dx, c + dy

                if not self.isValid(nr, nc, m, n) or classroom[nr][nc] == 'X' or energy_left == 0:
                    continue

                nextEnergy = energy if classroom[nr][nc] == 'R' else energy_left - 1
                if nextEnergy < 0:
                    continue


                next_mask = mask
                if classroom[nr][nc] == 'L' and (nr, nc) in litterMap:
                    next_mask |= (1 << litterMap[(nr, nc)])

                heapq.heappush(heap, (moves + 1, nr, nc, nextEnergy, next_mask))

        return -1             