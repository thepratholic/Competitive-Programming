from heapq import heappush, heappop
from math import inf
from typing import List

class Solution:
    def minJumps(self, arr: List[int]) -> int:
        def prime_factors(n):
            factors = set()
            d = 2
            while d * d <= n:
                while n % d == 0:
                    factors.add(d)
                    n //= d
                d += 1
            if n > 1:
                factors.add(n)
            return factors

        n = len(arr)
        gr = {}
        for i in range(n):
            fac = prime_factors(arr[i])
            for ele in fac:
                if ele in gr:
                    gr[ele].append(i)
                else:
                    gr[ele] = [i]

        h = [[0, -0]]  # distance, -index
        dis = [inf] * n
        dis[0] = 0

        while h:
            val, node = heappop(h)
            if node == -(n - 1):
                return val
            node = -node

            for nei in [node - 1, node + 1]:
                if 0 <= nei < n and dis[nei] > val + 1:
                    dis[nei] = val + 1
                    heappush(h, [val + 1, -nei])

            if arr[node] in gr:
                for nei in gr[arr[node]]:
                    if dis[nei] > val + 1:
                        dis[nei] = val + 1
                        heappush(h, [val + 1, -nei])
