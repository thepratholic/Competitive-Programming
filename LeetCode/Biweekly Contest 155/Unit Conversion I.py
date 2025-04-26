from collections import deque
from typing import List


class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7
        n = 0
        for source, target, _ in conversions:
            n = max(n, source, target)
        n += 1
        graph = [[] for _ in range(n)]

        for source, target, factor in conversions:
            graph[source].append((target, factor))
            graph[target].append((source, -factor))  

    
        result = [-1] * n
        result[0] = 1  

        queue = deque([0])

        while queue:
            u = queue.popleft()

            for v, factor in graph[u]:
                if result[v] == -1:
                    if factor > 0:
                        result[v] = (result[u] * factor) % MOD
                    else:
                        result[v] = (result[u] * self.mod_inverse(-factor, MOD)) % MOD
                    queue.append(v)
        return [x % MOD for x in result]

    def mod_inverse(self, a, mod):
        return pow(a, mod - 2, mod)