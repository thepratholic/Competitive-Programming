from typing import List
from collections import defaultdict
from heapq import heappop, heappush


class Solution:
    def minTimeMaxPower(self, n: int, edges: List[List[int]], power: int, cost: List[int], source: int, target: int) -> List[int]:
        if source == target:
            return [0, power]

        graph = defaultdict(list)
        for u, v, t in edges:
            graph[u].append((v, t))

        INF = float('inf')
        dist = [[INF] * (power + 1) for _ in range(n)]

        dist[source][power] = 0

        heap = []
        heappush(heap, (0, -power, source)) # min heap as (time, mx power, node)

        while heap:
            t, neg, u = heappop(heap)

            rem = -neg

            if t > dist[u][rem]:
                continue

            if rem < cost[u]:
                continue

            nxt_power = rem - cost[u]

            for nei, time in graph[u]:
                nxt_time = time + t

                if nxt_time < dist[nei][nxt_power]:

                    if nxt_time < dist[nei][nxt_power]:
                        dist[nei][nxt_power] = nxt_time
                        heappush(heap, (nxt_time, -nxt_power, nei))


        best_time = INF
        best_pow = -1

        for p in range(power + 1):
            t = dist[target][p]

            if t < best_time:
                best_time = t
                best_pow = p

            elif t == best_time:
                best_pow = max(best_pow, p)

        if best_time == INF:
            return [-1, -1]

        return [best_time, best_pow]