from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumThreshold(self, n: int, edges: List[List[int]], source: int, target: int, k: int) -> int:
        graph = defaultdict(list)
        mx = 0
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))

            mx = max(mx, w)

        def check(mid):
            q = deque()
            dist = [float('inf')] * n
            dist[source] = 0

            q.append(source)

            while q:
                node = q.popleft()

                for nei, wt in graph[node]:
                    c = 0 if wt <= mid else 1
                    nd = dist[node] + c

                    if nd < dist[nei]:
                        dist[nei] = nd

                        if c == 0:
                            q.appendleft(nei)

                        else:
                            q.append(nei)

            return dist[target] <= k

        if not check(mx):
            return -1

        low = 0
        high = mx
        ans = mx

        while low <= high:
            mid = (low + high) >> 1

            if check(mid):
                ans = mid
                high = mid - 1

            else:
                low = mid + 1

        return ans