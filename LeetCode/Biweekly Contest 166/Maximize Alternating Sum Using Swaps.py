from collections import defaultdict
from typing import List


class DSU:
    def __init__(self, n: int):
        self.parent = list(range(n + 1))
        self.size = [1] * (n + 1)

    def findUPar(self, node):
        if node == self.parent[node]:
            return node

        self.parent[node] = self.findUPar(self.parent[node])
        return self.parent[node]
        
    def find(self, u: int, v: int) -> bool:
        return self.findUPar(u) == self.findUPar(v)

    def union(self, u: int, v: int) -> None:
        ulp_u = self.findUPar(u)
        ulp_v = self.findUPar(v)

        if ulp_u == ulp_v: return
        elif self.size[ulp_u] < self.size[ulp_v]:
            self.parent[ulp_u] = ulp_v
            self.size[ulp_v] += self.size[ulp_u]

        elif self.size[ulp_v] < self.size[ulp_u]:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += self.size[ulp_v]

        else:
            self.parent[ulp_v] = ulp_u
            self.size[ulp_u] += 1
        

class Solution:
    def maxAlternatingSum(self, nums: List[int], swaps: List[List[int]]) -> int:
        n = len(nums)

        dsu = DSU(n)
        for p, q in swaps:
            dsu.union(p, q)

        parents_to_values = defaultdict(list)

        for i in range(n):
            parents_to_values[dsu.findUPar(i)].append(i)

        ans = 0

        for k, v in parents_to_values.items():
            if not v:
                continue

            c = 0

            vals = []
            for i in v:
                if i & 1:
                    c += 1
                vals.append(nums[i])

            vals.sort()

            cnt = 0
            for i in vals:
                if cnt < c:
                    cnt += 1
                    ans -= i

                else:
                    ans += i

        return ans