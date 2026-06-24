from typing import List
from heapq import heappop, heappush


class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], labels: str, k: int) -> int:
        adj = [[] for _ in range(n)]

        for u, v, w in edges:
            adj[u].append((v, w))

        INF = float('inf')
        dist = [[INF] * (k + 1) for _ in range(n)]

        dist[0][1] = 0 # distance of node 0 with streak 1 is 0
        pq = []
        heappush(pq, (0, 0, 1)) # (dist, node, streak)

        while pq:
            cost, node, streak = heappop(pq)

            if cost > dist[node][streak]:
                continue

            if node == n - 1:
                return cost

            for nei, wt in adj[node]:
                if labels[nei] == labels[node]:
                    new_streak = streak + 1

                else:
                    new_streak = 1

                if new_streak > k:
                    continue

                new_cost = cost + wt

                if dist[nei][new_streak] > new_cost:
                    dist[nei][new_streak] = new_cost
                    heappush(pq, (new_cost, nei, new_streak))

        return -1