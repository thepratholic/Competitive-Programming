import heapq
from typing import List

class Solution:
    def minTime(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        vis = [False] * n
        pq = []

        for u, v, start, end in edges:
            adj[u].append((v, start, end))

        heapq.heappush(pq, (0, 0)) # time, node

        while pq:
            time, node = heapq.heappop(pq)

            if node == n - 1:
                return time

            if vis[node]:
                continue

            vis[node] = True

            for adjNode, start, end in adj[node]:
                if time <= end and not vis[adjNode]:
                    heapq.heappush(pq, (max(time, start) + 1, adjNode))

        return -1