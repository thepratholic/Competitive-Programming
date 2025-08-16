import heapq
from collections import defaultdict
from typing import List

class Solution:
    def minCost(self, n: int, edges: List[List[int]]) -> int:
        adj = defaultdict(list)
        
        for u, v, cost in edges:
            adj[u].append((v, cost))
            adj[u + n].append((v, cost))
            adj[v + n].append((u, 2 * cost))

        for i in range(n):
            adj[i].append((i + n, 0))

        dist = [float('inf')] * (2 * n)
        dist[0] = 0
        pq = [(0, 0)]

        while pq:
            cur_dist, u = heapq.heappop(pq)

            if cur_dist > dist[u]:
                continue

            for v, weight in adj[u]:
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    heapq.heappush(pq, (dist[v], v))

        min_cost = min(dist[n - 1], dist[n - 1 + n])

        return min_cost if min_cost != float('inf') else -1