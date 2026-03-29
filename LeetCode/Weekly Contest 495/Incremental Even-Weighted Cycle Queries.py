from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * (n)
        self.parity = [0] * (n)

    def findUPar(self, node): # do the path compression
        if node == self.parent[node]:
            return node

        par = self.parent[node]
        self.parent[node] = self.findUPar(self.parent[node])
        self.parity[node] ^= self.parity[par]
        return self.parent[node]

    def union(self, u, v, wt):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v: return (self.parity[u] ^ self.parity[v] ^ wt) == 0
            
        elif self.size[ulp_u] < self.size[ulp_v]:
            ulp_u, ulp_v = ulp_v, ulp_u
            u, v = v, u

        self.parent[ulp_v] = ulp_u
        self.parity[ulp_v] = self.parity[v] ^ self.parity[u] ^ wt
        self.size[ulp_u] += self.size[ulp_v]

        return True

    # my own DSU class, copied from github

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:

        dsu = DSU(n)
        ans = 0
        for u, v, wt in edges:
            if dsu.union(u, v, wt):
                ans += 1

        return ans