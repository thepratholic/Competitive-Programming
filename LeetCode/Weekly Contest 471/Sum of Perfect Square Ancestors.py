from collections import defaultdict
from typing import List


class Solution:
    def sumOfAncestors(self, n: int, edges: List[List[int]], nums: List[int]) -> int:
        
        def strip(v):
            ans = 1
            i = 2

            while i * i <= v:
                cnt = 0

                while v % i == 0:
                    v //= i
                    cnt += 1

                if cnt & 1:
                    ans *= i
                i += 1

            if v > 1:
                ans *= v

            return ans

        def dfs(node, parent):
            s = strip(nums[node])
            ans[0] += cnt[s]

            cnt[s] += 1

            for adjNode in adj[node]:
                if adjNode == parent:
                    continue

                dfs(adjNode, node)

            cnt[s] -= 1

        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        cnt = defaultdict(int)
        ans = [0]

        dfs(0, -1)
        return ans[0]