from heapq import heappop, heappush
from typing import List


class Solution:
    def minCost(self, m: int, n: int, penalty: List[List[int]]) -> int:
        INF = 10 ** 30

        dist = [[[INF] * 2 for _ in range(n)] for _ in range(m)]

        dist[0][0][1] = 1
        start = 1

        pq = [(start, 0, 0, 1)] # (cost, row, col, parity)

        dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        def isValid(i, j):
            return i >= 0 and i < m and j >= 0 and j < n

        while pq:
            cost, r, c, p = heappop(pq)

            if cost != dist[r][c][p]:
                continue

            if r == m - 1 and c == n - 1:
                return cost

            ncost = cost + penalty[r][c]
            if ncost < dist[r][c][p ^ 1]:
                heappush(pq, (ncost, r, c, p ^ 1))
                dist[r][c][p ^ 1] = ncost

            for dx, dy in dirs:
                nr = r + dx
                nc = c + dy

                if not isValid(nr, nc): continue

                ok = False

                if p == 1:
                    if (dx, dy) in ((1, 0), (0, 1)):
                        ok = True

                else:
                    if (dx, dy) in ((-1, 0), (0, -1)):
                        ok = True

                nxt_enter = (nr + 1) * (nc + 1)

                if ok:
                    ncost = cost + nxt_enter

                else:
                    ncost = cost + nxt_enter + penalty[r][c]

                if dist[nr][nc][p ^ 1] > ncost:
                    heappush(pq, (ncost, nr, nc, p ^ 1))
                    dist[nr][nc][p ^ 1] = ncost

        return -1