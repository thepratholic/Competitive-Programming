from collections import deque
from typing import List


class Solution:
    def f(self, adj, topo, minimum, k, n):
        dist = [float('inf')] * n
        dist[0] = 0

        for u in topo:
            if dist[u] > k:
                continue

            for v, cost in adj[u]:
                if cost >= minimum:
                    dist[v] = min(dist[v], dist[u] + cost)

        return dist[n - 1] <= k

    def findMaxPathScore(self, edges: List[List[int]], online: List[bool], k: int) -> int:
        n = len(online)

        adj = [[] for _ in range(n)]
        indegree = [0] * n

        for u, v, cost in edges:
            if online[u] and online[v]:
                adj[u].append((v, cost))
                indegree[v] += 1


        topo = []
        q = deque()

        for i in range(n):
            if indegree[i] == 0 and online[i]:
                q.append(i)

        while q:
            u = q.popleft()
            topo.append(u)
            for v, cost in adj[u]:
                indegree[v] -= 1
                if indegree[v] == 0:
                    q.append(v)

                
        # binary search will start from here
        low, high, ans = 0, k, -1

        while low <= high:
            mid = (low + high) >> 1

            if self.f(adj, topo, mid, k, n):
                ans = mid
                low = mid + 1

            else:
                high = mid - 1

        return ans