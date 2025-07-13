from typing import List


class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        parent = list(range(n))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
    
        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return False
            parent[py] = px
            return True
    
        edges.sort(key=lambda x: x[2])
        mst_weights = []
    
        for u, v, w in edges:
            if union(u, v):
                mst_weights.append(w)
    
        mst_weights.sort(reverse=True)
    
        if k - 1 >= len(mst_weights):
            return 0
    
        return max(mst_weights[k - 1:])