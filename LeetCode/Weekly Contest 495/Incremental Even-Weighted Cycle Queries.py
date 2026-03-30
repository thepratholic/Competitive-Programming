from typing import List


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.parity = [0] * n

    def find(self, node):
        if node == self.parent[node]:
            return node

        original_par = self.parent[node]
        root = self.find(original_par)

        self.parity[node] ^= self.parity[original_par]
        self.parent[node] = root

        return self.parent[node]

    def union(self, u, v, wt):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u == root_v:
            return

        if self.size[root_u] < self.size[root_v]:
            self.size[root_v] += self.size[root_u]
            self.parent[root_u] = root_v
            self.parity[root_u] = self.parity[u] ^ wt ^ self.parity[v]

        else:
            self.size[root_u] += self.size[root_v]
            self.parent[root_v] = root_u
            self.parity[root_v] = self.parity[v] ^ wt ^ self.parity[u]

    
    def get_parity(self, node):
        return self.parity[node]

class Solution:
    def numberOfEdgesAdded(self, n: int, edges: List[List[int]]) -> int:
        dsu = DSU(n)

        ans = 0
        for u, v, wt in edges:
            root_u = dsu.find(u)
            root_v = dsu.find(v)

            if root_u == root_v:
                path_sum_from_u = dsu.get_parity(u)
                path_sum_from_v = dsu.get_parity(v)

                if path_sum_from_u ^ path_sum_from_v ^ wt == 0:
                    ans += 1

            else:
                ans += 1
                dsu.union(u, v, wt)

        return ans