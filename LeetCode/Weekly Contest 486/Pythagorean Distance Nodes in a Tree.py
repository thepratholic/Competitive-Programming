from collections import defaultdict, deque
from typing import List


class Solution:
    def specialNodes(self, n: int, edges: List[List[int]], x: int, y: int, z: int) -> int:
        g = defaultdict(list)

        for u, v in edges:
            g[u].append(v)
            g[v].append(u)

        def bfs(src):
            dist = [-1] * n
            q = deque()
            q.append(src)
            dist[src] = 0

            while q:
                node = q.popleft()

                for adjNode in g[node]:
                    if dist[adjNode] == -1:
                        dist[adjNode] = dist[node] + 1

                        q.append(adjNode)

            return dist

        dx = bfs(x)
        dy = bfs(y)
        dz = bfs(z)
        ans = 0
        for i in range(n):
            a = dx[i]
            b = dy[i]
            c = dz[i]

            a, b, c = sorted([a, b, c])

            if a * a + b * b == c * c:
                ans += 1

        return ans