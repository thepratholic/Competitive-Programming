from typing import DefaultDict


class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        n = len(nums)

        graph = DefaultDict(list)

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        ans = 0

        # seeing constraints, we can try all possible sebsets, bitmask
        for mask in range(1, (1 << n)):
            nodes = []

            total = 0

            for node in range(n):
                if mask & (1 << node):
                    nodes.append(node)
                    total += nums[node]

            if total % 2:
                continue

            start = nodes[0]
            vis = set()

            def dfs(node):
                vis.add(node)

                for child in graph[node]:
                    if (mask & (1 << child)) and child not in vis:
                        dfs(child)

            dfs(start)

            if len(vis) == len(nodes):
                ans += 1

        return ans