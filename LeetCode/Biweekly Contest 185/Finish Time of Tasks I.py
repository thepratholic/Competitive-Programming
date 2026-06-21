from typing import List


class Solution:
    def finishTime(self, n: int, edges: List[List[int]], baseTime: List[int]) -> int:
        g = [[] for _ in range(n)]

        for u, v in edges:
            g[u].append(v)

        def f(node):
            if not g[node]:
                return baseTime[node]

            mn = float('inf')
            mx = 0

            for child in g[node]:
                t = f(child)
                mn = min(t, mn)
                mx = max(mx, t)

            return mx + (mx - mn) + baseTime[node]

        return f(0)
                