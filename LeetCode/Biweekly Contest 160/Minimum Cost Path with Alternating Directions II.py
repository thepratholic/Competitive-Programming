import heapq
from typing import List

class Solution:
    def isValid(self, i, j, m, n):
        return 0 <= i < m and 0 <= j < n

    def minCost(self, m: int, n: int, waitCost: List[List[int]]) -> int:
        pq = []
        heapq.heappush(pq, (1, 0, 0, 1))  # cost, row, col, time

        directions = [(1, 0), (0, 1)]
        visited = dict()

        while pq:
            cost, row, col, time = heapq.heappop(pq)

            if (row, col) == (m - 1, n - 1):
                return cost

            state = (row, col, time % 2)
            if state in visited and visited[state] <= cost:
                continue

            visited[state] = cost

            if time % 2 == 1:
                # move to down and right
                for dx, dy in directions:
                    nrow, ncol = row + dx, col + dy
                    if self.isValid(nrow, ncol, m, n):
                        entry_cost = (nrow + 1) * (ncol + 1)
                        heapq.heappush(pq, (entry_cost + cost, nrow, ncol, time + 1))
            else:
                wait_cost = waitCost[row][col]
                heapq.heappush(pq, (cost + wait_cost, row, col, time + 1))

        return -1
