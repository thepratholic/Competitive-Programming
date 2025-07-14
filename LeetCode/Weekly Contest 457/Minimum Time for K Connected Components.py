from typing import List


class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def find(self, u, v):
        return self.findUPar(u) == self.findUPar(v)

    def unionBySize(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v: return False
        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        elif self.size[ulp_v] < self.size[ulp_u]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += 1

        return True



class Solution:
    def minTime(self, n: int, edges: List[List[int]], k: int) -> int:

        dsu = DisjointSet(n)
        target = n - k + 1
        edges.sort(key = lambda x: x[2])
        
        while edges and target:

            nodeA, nodeB, time = edges.pop()
            if dsu.unionBySize(nodeA, nodeB): 
                target-= 1

            if not target: 
                return time

        return 0
        