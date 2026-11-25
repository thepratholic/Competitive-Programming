class Solution:
    def earliestActivationTimes(self, n: int, edges: list[list[int]], requiredSignals: list[int]) -> list[int]:
        g = [[] for _ in range(n)]

        for u, v, d in edges:
            g[u].append([d, v])

        res = [-1] * n
        res[0] = 0

        q = g[0][:]
        heapify(q)

        while q:
            t, node = heappop(q)

            if res[node] >= 0: continue

            requiredSignals[node] -= 1
            if requiredSignals[node] == 0:
                res[node] = t

                for d, v in g[node]:
                    if res[v] < 0:
                        heappush(q, [t + d, v])

        return res