from typing import List
from heapq import heappush, heappop

class Solution:
    def minCost(self, n: int, prices: List[int], roads: List[List[int]]) -> List[int]:
        empty = [[] for _ in range(n)]
        carry = [[] for _ in range(n)]

        for u, v, cost, tax in roads:

            empty[u].append((v, cost))
            empty[v].append((u, cost))

            carry_cost = cost * tax

            carry[u].append((v, carry_cost))
            carry[v].append((u, carry_cost))

        INF = 10 ** 18
        ans = [0] * n

        empty_dist = [INF] * n
        carry_dist = [INF] * n

        for src in range(n):

            for i in range(n):
                empty_dist[i] = INF

            pq = [(0, src)] # (dist, node)
            empty_dist[src] = 0

            while pq:
                dist, cur = heappop(pq)

                for nei, wt in empty[cur]:
                    if dist + wt < empty_dist[nei]:
                        empty_dist[nei] = dist + wt
                        heappush(pq, (empty_dist[nei], nei))

            # ab for carrying apples wale graph pe, from src to all other nodes compute karo shortest path
            for i in range(n):
                carry_dist[i] = INF

            carry_dist[src] = 0

            pq = [(0, src)]

            while pq:
                dist, cur = heappop(pq)

                for nei, wt in carry[cur]:
                    if dist + wt < carry_dist[nei]:
                        carry_dist[nei] = dist + wt
                        heappush(pq, (carry_dist[nei], nei))

            
            best = prices[src] # current shop se buy karlia, ab check karo baaki sab shops se

            for shop in range(n):
                if empty_dist[shop] == INF or carry_dist[shop] == INF:
                    continue

                total = empty_dist[shop] + prices[shop] + carry_dist[shop]

                best = min(best, total)

            ans[src] = best

        return ans