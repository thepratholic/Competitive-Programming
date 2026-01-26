from collections import defaultdict, deque
from typing import List


class Solution:
    def minimumFlips(self, n: int, edges: List[List[int]], start: str, target: str) -> List[int]:
        
        def toggle(x):
            return '1' if x == '0' else '0'

        adj = defaultdict(set)
        for ei, (u, v) in enumerate(edges):
            adj[u].add((v, ei))
            adj[v].add((u, ei))

        start = list(start)
        target = list(target)

        q = deque()
        for i in range(n):
            if len(adj[i]) == 1:
                q.append(i)

        ans = []

        while q:
            u = q.popleft()

            if not adj[u]:
                continue

            v, ei = next(iter(adj[u]))

            if start[u] != target[u]:
                start[u] = toggle(start[u])
                target[v] = toggle(target[v])

                ans.append(ei)

            adj[u].discard((v, ei))
            adj[v].discard((u, ei))

            if len(adj[v]) == 1:
                q.append(v)

        if start != target:
            return [-1]

        ans.sort()
        return ans