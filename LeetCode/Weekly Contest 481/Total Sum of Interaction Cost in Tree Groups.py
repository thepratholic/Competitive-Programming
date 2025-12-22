from collections import defaultdict
from typing import List


class Solution:
    def interactionCosts(self, n: int, edges: List[List[int]], group: List[int]) -> int:
        ans = 0
        adj = defaultdict(list)
        gcnts = [0] * 21

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        for g in group:
            gcnts[g] += 1

        def dfs(node, par):
            nonlocal ans
            res = [0] * 21
            res[group[node]] += 1

            for adjNode in adj[node]:
                if adjNode == par: continue
                ycnts = dfs(adjNode, node)

                for i in range(1, 21):
                    res[i] += ycnts[i]
                    cin = ycnts[i]
                    cout = gcnts[i] - cin
                    ans += cin * cout

            return res


        dfs(0, -1)
        return ans