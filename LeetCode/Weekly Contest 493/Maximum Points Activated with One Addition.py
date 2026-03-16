class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]

    def union(self, u, v):
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v:
            return

        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

class Solution:
    def maxActivated(self, points: list[list[int]]) -> int:
        n = len(points)
        dsu = DSU(n)

        xmap = {}
        ymap = {}

        for i, (x, y) in enumerate(points):
            if x in xmap:
                dsu.union(i, xmap[x])
            else:
                xmap[x] = i

            if y in ymap:
                dsu.union(i, ymap[y])

            else:
                ymap[y] = i


        sizes = [dsu.size[node] for node in range(n) if dsu.parent[node] == node]
        sizes.sort(reverse = True)

        c1 = sizes[0] if len(sizes) > 0 else 0
        c2 = sizes[1] if len(sizes) > 1 else 0
        return c1 + c2 + 1